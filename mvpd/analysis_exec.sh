#!/bin/bash

source "./analysis_spec.py"

for run in $(seq 1 $total_run)
do
    case $model_type in
    "NN_1layer")
       echo "MVPD - 1-layer Neural Network"  
       python3 MVPD_neural_net.py $run
       ;;
    "NN_5layer")
       echo "MVPD - 5-layer Neural Network"
       python3 MVPD_neural_net.py $run
       ;;
    "NN_5layer_dense")
       echo "MVPD - 5-layer Dense Neural Network"
       python3 MVPD_neural_net.py $run
       ;;
    "PCA_LR")
       echo "MVPD - PCA + Linear Regression"
       python3 MVPD_PCA_LR.py $run
       ;;
    "L2_LR")
       echo "MVPD - L2 Regularized Linear Regression"
       python3 MVPD_L2_LR.py $run
       ;;
    esac
done

case $model_type in
"NN_1layer"|"NN_5layer"|"NN_5layer_dense")
   echo "MVPD - Average Across Runs"
   python3 avgrun_neural_net.py
   ;;
"PCA_LR"|"L2_LR")
   echo "MVPD - Average Across Runs"
   python3 avgrun_regression.py
   ;;
esac

