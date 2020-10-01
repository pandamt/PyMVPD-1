"""
Average variance explained across runs for neural networks.
"""
import numpy as np
import nibabel as nib
from viz import viz_map
from analysis_spec import sub, total_run, filepath_mask2, results_save_dir, model_type, num_epochs, save_freq

for epoch in range(save_freq, num_epochs+1, save_freq):
    var_data_total = []
    for testrun in range(1, total_run+1):
        results_save_dir_run = results_save_dir+sub+'_'+model_type+'_testrun'+str(testrun)+'/'
        data_dir = results_save_dir_run+sub+'_var_expl_'+model_type+'_testrun'+str(testrun)+'_'+str(epoch)+'epochs.npy'
        var_data = np.load(data_dir)
        var_data_total.append(var_data)

    var_data_avg = np.mean(var_data_total, 0)
    var_map_avg, var_img_avg = viz_map.cmetric_to_map(filepath_mask2, var_data_avg)

    np.save(results_save_dir_run+sub+'_var_expl_'+model_type+'_avgruns_'+str(epoch)+'epochs.npy', var_data_avg)
    np.save(results_save_dir+sub+'_var_expl_map_'+model_type+'_avgruns_'+str(epoch)+'epochs.npy', var_map_avg)
    nib.save(var_img_avg, results_save_dir+sub+'_var_expl_map_'+model_type+'_avgruns_'+str(epoch)+'epochs.nii.gz')

    







