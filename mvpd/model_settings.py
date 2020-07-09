# MVPD Model 
mode='NN_1layer' # ['PCA_LR', 'L2_LR', 'NN_1layer', 'NN_5layer', 'NN_5layer_dense']

sub='sub-01'
total_run=8
test_run=1

# Functional Data
roi_1_name='FFA'
roi_2_name='GM'

filepath_func = []
for run in range(1, total_run+1):
    filepath_func.append('/gsfs0/data/fangmg/PyMVPD/mvpd/example_data/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run'+str(run)+'.nii.gz')

# Predictor Mask
filepath_mask1='/gsfs0/data/fangmg/PyMVPD/mvpd/example_data/'+sub+'/'+sub+'_FFA_80vox_bin.nii.gz'
# Target Mask
filepath_mask2='/gsfs0/data/fangmg/PyMVPD/mvpd/example_data/GM_thr0.1_bin.nii.gz'
# Save Directory
roi_save_dir = '/gsfs0/data/fangmg/PyMVPD/mvpd/example_data/roi_data/'
model_save_dir='/gsfs0/data/fangmg/PyMVPD/mvpd/test/'

# Modeling
# PCA + Linear Regression
num_pc=3 # number of principal component used

# L2 Regularized Linear Regression
alpha=0.01 # regularization strength

# Neural Network
input_size=80
output_size=53539
hidden_size=100 # number of units per hidden layer
num_epochs=5000 # number of epochs for training
save_freq=1000 # checkpoint saving frequency
print_freq=50 # print out frequency
batch_size=32 
learning_rate=1e-3
momentum_factor=0.9  
w_decay=0 # weight decay (L2 penalty)


