# PyMVPD

PyMVPD: MultiVariate Pattern Dependence in Python

## MVPD Model Family
1. Linear Regression Models
* L2_LR: linear regression model with L2 regularization
* PCA_LR: linear regression model with no regularization after principal component analysis (PCA)

2. Neural Network Models
* NN_1layer: 1-layer fully-connected linear neural network model
* NN_5layer: 5-Layer fully-connected linear neural network model
* NN_5layer_dense: 5-Layer fully-connected linear neural network model with dense connections

##  Example Dataset
Data from sub-01 in [_StudyForrest_](http://studyforrest.org): FFA - fusiform face area, PPA - parahippocampal place area, GM - grey matter

##  Example Analyses and Scripts
1. Choose one MVPD model, set model parameters, input functional data and ROI masks, set output directory in [model/model_settings.py](model/model_settings.py);
2. Run [data_prep.py](mvpd/data_prep.py) to preprocess functional data;
```
python3 data_prep.py
```
3. Run MVPD model: 
```
sh runMVPD.sh
```
     


