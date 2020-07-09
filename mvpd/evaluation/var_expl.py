"""
MVPD base processing workflows
"""
import numpy as np

# Model Evaluation
def eval_var_expl(error, ROI_2_test):
    """
    Calculate the proportion of variance explained.
    """
    var_expl = 1 - error.var(axis=0)/ROI_2_test.var(axis=0)
    var_expl = np.maximum(0, var_expl) # replace negative values with zeros
    return var_expl
