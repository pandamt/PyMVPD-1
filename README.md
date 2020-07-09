# PyMVPD

PyMVPD: MultiVariate Pattern Dependence in Python

## MVPD Model Family
### Linear Regression Model
1. L2_LR:
2. PCA_LR:

### Neural Network Model
1. NN_1layer:
2. NN_5layer:
3. NN_5layer_dense:

##  Example Dataset
Data from sub-01 in [_StudyForrest_](http://studyforrest.org): FFA - fusiform face area, PPA - parahippocampal place area, GM - grey matter

##  Example Analyses and Scripts
1. Choose one MVPD model, set model parameters, input functional data and ROI masks in [model/model_settings.py](model/model_settings.py);
2. [Preprocess](mvpd/data_prep.py) functional data with ROI masks;
3. Run MVPD model: 
     
     sh runMVPD.sh
     


