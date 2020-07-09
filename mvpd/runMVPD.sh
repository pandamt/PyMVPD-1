#!/bin/bash

source "/gsfs0/data/fangmg/PyMVPD/mvpd/model_settings.py"

case $mode in
"NN_1layer")
   echo "MVPD - 1-layer Neural Network"
   python3 MVPD_neural_net.py $test_run
   ;;
"NN_5layer")
   echo "MVPD - 5-layer Neural Network"
   python3 MVPD_neural_net.py $test_run
   ;;
"NN_5layer_dense")
   echo "MVPD - 5-layer Dense Neural Network"
   python3 MVPD_neural_net.py $test_run
   ;;
"PCA_LR")
   echo "MVPD - PCA + Linear Regression"
   python3 MVPD_PCA_LR.py $test_run
   ;;
"L2_LR")
   echo "MVPD - L2 Regularized Linear Regression"
   python3 MVPD_L2_LR.py $test_run
   ;;
esac


