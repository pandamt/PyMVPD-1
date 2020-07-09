# PyMVPD

PyMVPD: MultiVariate Pattern Dependence in Python

## MVPD Model Family
1. Linear Regression Models
* L2_LR:
* PCA_LR:

2. Neural Network Models
* NN_1layer:
* NN_5layer:
* NN_5layer_dense:

##  Example Dataset
Data from sub-01 in [_StudyForrest_](http://studyforrest.org): FFA - fusiform face area, PPA - parahippocampal place area, GM - grey matter

##  Example Analyses and Scripts
1. Choose one MVPD model, set model parameters, input functional data and ROI masks in [model/model_settings.py](model/model_settings.py);
2. Run [data_prep.py](mvpd/data_prep.py) to preprocess functional data;
3. Run MVPD model: 
          sh runMVPD.sh
     


