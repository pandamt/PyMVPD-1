# MVPD - Neural Network Model
import sys, os
import importlib
import nibabel as nib
import numpy as np
import itertools as it
import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torch.autograd import Variable
from dataloader.loader_neural_net import ROI_Dataset
from evaluation import var_expl
from viz import viz_map
from model_settings import mode, input_size, output_size, hidden_size, total_run, sub, num_epochs, save_freq, print_freq, batch_size, learning_rate, momentum_factor, w_decay, model_save_dir, filepath_func, filepath_mask1, filepath_mask2

NN_module = importlib.import_module('func_neural_net.%s'%(mode))
NN_model = getattr(NN_module, mode)

sys.argv = [sys.argv[0], sys.argv[1]]
this_run = int(sys.argv[1])
print("this_run:", this_run)

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# create output folder if not exists
if not os.path.exists(model_save_dir):
       os.mkdir(model_save_dir)

model_save_dir_run = model_save_dir + sub + '_' + mode + '_testrun' + str(this_run) + '/'

if not os.path.exists(model_save_dir_run):
       os.mkdir(model_save_dir_run)

def save_model(net, optim, epoch, ckpt_fname):
    state_dict = net.state_dict()
    for key in state_dict.keys():
        state_dict[key] = state_dict[key].cpu()
    torch.save({
        'epoch': epoch,
        'state_dict': state_dict,
        'optimizer': optim},
        ckpt_fname)

def NN_train(net, trainloader, criterion, optimizer, epoch, print_freq, save_freq, model_save_dir):
    net.train()
    running_loss = 0.0
    for i, data in enumerate(trainloader):
        # get the inputs
        ROIs_1 = data['ROI_1']
        ROIs_2 = data['ROI_2']
        
        if torch.cuda.is_available():
           ROIs_1, ROIs_2 = Variable(ROIs_1.cuda()), Variable(ROIs_2.cuda())
        else:
           ROIs_1, ROIs_2 = Variable(ROIs_1), Variable(ROIs_2)
        # zero the parameter gradients
        optimizer.zero_grad()
        # forward + backward + optimize
        outputs = net(ROIs_1)
        loss = criterion(outputs, ROIs_2)
        loss.backward()
        optimizer.step()
        # print statistics
        loss.item()
        running_loss += loss.data
        # print every print_freq mini-batches 
        if i % print_freq == (print_freq-1):
            print('[%d, %5d] loss: %.3f' %
                  (epoch, i + 1, running_loss / print_freq))
            running_loss = 0.0

    if epoch % save_freq == 0:
        save_model(net, optimizer, epoch, os.path.join(model_save_dir, 'MVPD_'+mode+'_%03d.ckpt' % epoch))
        print("Model saved in file: " + model_save_dir + "MVPD_"+mode+"_%03d.ckpt" % epoch)

def NN_test(net, output_size, testloader, epoch, model_save_dir):
    net.eval()
    score = []
    ROI_2_pred = []
    ROI_2_target = []
    ROI_2_pred = np.reshape(ROI_2_pred, [-1, output_size])
    ROI_2_target = np.reshape(ROI_2_target, [-1, output_size])

    for i, data in enumerate(testloader):
            # get the inputs
            ROIs_1 = data['ROI_1']
            ROIs_2 = data['ROI_2']
            # wrap them in Variable
            if torch.cuda.is_available():
               ROIs_1, ROIs_2 = Variable(ROIs_1.cuda()), Variable(ROIs_2.cuda())
            else:
               ROIs_1, ROIs_2 = Variable(ROIs_1),  Variable(ROIs_2)
            # forward + backward + optimize
            outputs = net(ROIs_1)
            outputs_numpy = outputs.cpu().data.numpy()
            ROI_2_pred = np.concatenate([ROI_2_pred, outputs_numpy], 0)
            ROIs_2_numpy = ROIs_2.cpu().data.numpy()
            ROI_2_target = np.concatenate([ROI_2_target, ROIs_2_numpy], 0)

    err_NN = ROI_2_pred - ROI_2_target
    print("ROI_2_pred:", ROI_2_pred)
    print("ROI_2_target:", ROI_2_target)
    print("err_NN:", err_NN)

    return err_NN, ROI_2_target

if __name__ == "__main__":
    # Load functioanl data and ROI masks 
    # Training 
    roi_train = ROI_Dataset()
    roi_train.get_train(this_run, total_run)
    trainloader = DataLoader(roi_train, batch_size, shuffle=True, num_workers=0, pin_memory=True) 
    # Testing 
    roi_test = ROI_Dataset()
    roi_test.get_test(this_run, total_run)
    testloader = DataLoader(roi_test, batch_size, shuffle=False, num_workers=0, pin_memory=True) 
   
    net = NN_model(input_size, hidden_size, output_size).to(device)
    
    # Loss and optimizer
    criterion = nn.MSELoss() # mean squared error
    optimizer = optim.SGD(net.parameters(), lr=learning_rate, momentum=momentum_factor, weight_decay=w_decay)

    for epoch in range(num_epochs+1):  # loop over the dataset multiple times
        NN_train(net, trainloader, criterion, optimizer, epoch, print_freq, save_freq, model_save_dir_run)
        if (epoch != 0) & (epoch % save_freq == 0):
            err_NN, ROI_2_test = NN_test(net, output_size, testloader, epoch, model_save_dir_run)
            # Evaluation: variance explained
            var_expl = var_expl.eval_var_expl(err_NN, ROI_2_test)
            print("max_vari:", max(var_expl))
            # save variance to file 
            np.save(model_save_dir_run+sub+'_var_expl_'+mode+'_testrun'+str(this_run)+'_%depochs.npy' % epoch, var_expl)

            # Visualization
            var_expl_map, var_expl_img = viz_map.cmetric_to_map(filepath_mask2, var_expl)
            np.save(model_save_dir_run+sub+'_var_expl_map_'+mode+'_testrun'+str(this_run)+'_%depochs.npy' % epoch, var_expl_map)
            nib.save(var_expl_img, model_save_dir_run+sub+'_var_expl_map_'+mode+'_testrun'+str(this_run)+'_%depochs.nii.gz' % epoch)


