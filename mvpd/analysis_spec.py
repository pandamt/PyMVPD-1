# Subject/Participant
sub='sub-01'
# Total number of experimental runs
total_run=3
# Left-out run for testing
test_run=1

# Predictor ROI
roi_1_name='FFA'
# Target ROI
roi_2_name='GM'

# Functional Data
filepath_func=[]
filepath_func+=['./example_data/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run1.nii.gz']
filepath_func+=['./example_data/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run2.nii.gz']
filepath_func+=['./example_data/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run3.nii.gz']
filepath_func+=['./example_data/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run4.nii.gz']
filepath_func+=['./example_data/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run5.nii.gz']
filepath_func+=['./example_data/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run6.nii.gz']
filepath_func+=['./example_data/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run7.nii.gz']
filepath_func+=['./example_data/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run8.nii.gz']

# Predictor ROI Mask
filepath_mask1='./example_data/'+sub+'/'+sub+'_FFA_80vox_bin.nii.gz'
# Target ROI Mask
filepath_mask2='./example_data/GM_thr0.1_bin.nii.gz'
# Output Directory
roidata_save_dir='./example_data/roi_data/'
results_save_dir='./test/'

# MVPD Model
model_type='NN_1layer' # ['PCA_LR', 'L2_LR', 'NN_1layer', 'NN_5layer', 'NN_5layer_dense']
# PCA + Linear Regression
num_pc=3 # number of principal component used

# L2 Regularized Linear Regression
alpha=0.01 # regularization strength

# Neural Network
input_size=80
output_size=53539
hidden_size=100 # number of units per hidden layer
num_epochs=50 # number of epochs for training
save_freq=10 # checkpoint saving frequency
print_freq=10 # print out frequency
batch_size=32 
learning_rate=1e-3
momentum_factor=0.9  
w_decay=0 # weight decay (L2 penalty)


