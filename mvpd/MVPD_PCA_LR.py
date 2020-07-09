# MVPD - Principal Component Analysis (PCA) + Linear Regression Model
import sys, os
import numpy as np
import nibabel as nib
import itertools as it
from dataloader.loader_regression import ROI_Dataset
from dimension_reduction import DR_PCA
from func_regression.PCA_LR import PCA_LR
from evaluation import var_expl
from viz import viz_map
from model_settings import mode, sub, total_run, num_pc, filepath_func, filepath_mask1, filepath_mask2, model_save_dir

sys.argv = [sys.argv[0], sys.argv[1]]
this_run = int(sys.argv[1])
print("this_run:", this_run)

# create output folder if not exists
if not os.path.exists(model_save_dir):
       os.mkdir(model_save_dir)

if __name__ == "__main__":
    # Load functioanl data and ROI masks
    # Training 
    roi_train = ROI_Dataset()
    roi_train.get_train(this_run, total_run)
    ROI_1_train = roi_train[:]['ROI_1']
    ROI_2_train = roi_train[:]['ROI_2']
    # Testing 
    roi_test = ROI_Dataset()
    roi_test.get_test(this_run, total_run)
    ROI_1_test = roi_test[:]['ROI_1']
    ROI_2_test = roi_test[:]['ROI_2']

    # Dimensionality reduction: PCA
    ROI_1_train_pca, ROI_2_train_pca, ROI_1_test_pca, ROI_2_test_pca = DR_PCA(num_pc, ROI_1_train, ROI_2_train, ROI_1_test, ROI_2_test)

    # Linear regresson model
    predict_ROI_2_test, err_LR = PCA_LR(ROI_1_train_pca, ROI_2_train_pca, ROI_1_test_pca, ROI_2_train, ROI_2_test, num_pc) 

    # Evaluation: variance explained
    var_expl = var_expl.eval_var_expl(err_LR, ROI_2_test)
    # save variance to file 
    np.save(model_save_dir+sub+'_var_expl_'+mode+'_testrun'+str(this_run)+'.npy', var_expl)

    # Visualization
    var_expl_map, var_expl_img = viz_map.cmetric_to_map(filepath_mask2, var_expl)
    np.save(model_save_dir+sub+'_var_expl_map_'+mode+'_testrun'+str(this_run)+'.npy', var_expl_map)
    nib.save(var_expl_img, model_save_dir+sub+'_var_expl_map_'+mode+'_testrun'+str(this_run)+'.nii.gz')



