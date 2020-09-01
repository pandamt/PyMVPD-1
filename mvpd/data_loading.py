"""
Create ROI data by applying masks on functional data.
"""
import os
import numpy as np
from preprocessing.dataset_processing import apply_mask, roi_array
from model_settings import sub, total_run, roi_1_name, roi_2_name, filepath_func, filepath_mask1, filepath_mask2, roi_save_dir

# create output folder if not exists
if not os.path.exists(roi_save_dir):
       os.mkdir(roi_save_dir)

for run in range(1, total_run+1):
    roi_save_dir_run = roi_save_dir + 'roi_run_' + str(run) + '/'
    
    if not os.path.exists(roi_save_dir_run):
           os.mkdir(roi_save_dir_run)
     
    filepath_func_run = filepath_func[run-1]
    roi_1_mask, roi_2_mask = apply_mask(filepath_func_run, filepath_mask1, filepath_mask2) # functional data in masks
    roi_1_data_run = roi_array(roi_1_mask)
    roi_2_data_run = roi_array(roi_2_mask)

    np.save(roi_save_dir_run+roi_1_name+'_data_run_'+str(run)+'.npy', roi_1_data_run)
    np.save(roi_save_dir_run+roi_2_name+'_data_run_'+str(run)+'.npy', roi_2_data_run)




