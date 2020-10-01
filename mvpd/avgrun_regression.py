"""
Average variance explained across runs for regression models.
"""
import numpy as np
import nibabel as nib
from viz import viz_map
from analysis_spec import sub, total_run, filepath_mask2, results_save_dir, model_type

var_data_total = []

for testrun in range(1, total_run+1):
    data_dir = results_save_dir+sub+'_var_expl_'+model_type+'_testrun'+str(testrun)+'.npy'
    var_data = np.load(data_dir)
    var_data_total.append(var_data)

var_data_avg = np.mean(var_data_total, 0)
var_map_avg, var_img_avg = viz_map.cmetric_to_map(filepath_mask2, var_data_avg)

np.save(results_save_dir+sub+'_var_expl_'+model_type+'_avgruns.npy', var_data_avg)
np.save(results_save_dir+sub+'_var_expl_map_'+model_type+'_avgruns.npy', var_map_avg)
nib.save(var_img_avg, results_save_dir+sub+'_var_expl_map_'+model_type+'_avgruns.nii.gz')

    







