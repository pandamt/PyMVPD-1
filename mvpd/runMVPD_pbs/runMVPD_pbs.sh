#!/bin/bash

source "/gsfs0/data/username/PyMVPD/mvpd/model_settings.py"

sed -i -e 's/MODENAME/'$mode'/g' runMVPD.pbs

for thisr in 1 2 3 4 5 6 7 8
do
    \cp runMVPD.pbs tmp_runMVPD.pbs
    sed -i -e 's/thistestrun/ChangeThisRun/g' tmp_runMVPD.pbs

    \cp tmp_runMVPD.pbs output_pbs/$sub-$mode-thistestrun$thisr.pbs
    sed -i -e 's/ChangeThisRun/'$thisr'/g' output_pbs/$sub-$mode-thistestrun$thisr.pbs
    qsub output_pbs/$sub-$mode-thistestrun$thisr.pbs
done
