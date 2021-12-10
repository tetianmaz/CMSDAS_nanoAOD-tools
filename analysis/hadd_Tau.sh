#!/bin/bash

setenv CURRENTDIR "$PWD"
echo $CURRENTDIR

cp ../scripts/haddnano.py /uscmst1b_scratch/lpc1/3DayLifetime/fojensen/
cd /uscmst1b_scratch/lpc1/3DayLifetime/fojensen

setenv OUTPUTDIR "root://cmseos.fnal.gov//store/user/fojensen/cmsdas_10122021/"

python haddnano.py Tau_2018A.root `xrdfsls -u | grep \.root`
xrdcp -f Tau_2018A.root $OUTPUTDIR

python haddnano.py Tau_2018B.root `xrdfsls -u | grep \.root`
xrdcp -f Tau_2018B.root $OUTPUTDIR

python haddnano.py Tau_2018C.root `xrdfsls -u | grep \.root`
xrdcp -f Tau_2018C.root $OUTPUTDIR

python haddnano.py Tau_2018D.root `xrdfsls -u | grep \.root`
xrdcp -f Tau_2018D.root $OUTPUTDIR

cd ${CURRENTDIR}
