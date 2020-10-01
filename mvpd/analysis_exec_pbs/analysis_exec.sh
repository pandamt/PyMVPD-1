#!/bin/bash

source "/path/to/your/folder/PyMVPD/mvpd/analysis_spec.py"

sed -i -e 's/MODENAME/'$mode'/g' runMVPD.pbs

for thisr in $(seq 1 $total_run)
do
    \cp runMVPD.pbs tmp_runMVPD.pbs
    sed -i -e 's/thistestrun/ChangeThisRun/g' tmp_runMVPD.pbs

    \cp tmp_runMVPD.pbs output_pbs/$sub-$mode-thistestrun$thisr.pbs
    sed -i -e 's/ChangeThisRun/'$thisr'/g' output_pbs/$sub-$mode-thistestrun$thisr.pbs
    qsub output_pbs/$sub-$mode-thistestrun$thisr.pbs
done
