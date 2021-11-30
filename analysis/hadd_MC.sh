#!/bin/bash

setenv CURRENTDIR "$PWD"
echo $CURRENTDIR

cp ../scripts/haddnano.py /uscmst1b_scratch/lpc1/3DayLifetime/fojensen/
cd /uscmst1b_scratch/lpc1/3DayLifetime/fojensen

setenv OUTPUTDIR "root://cmseos.fnal.gov//store/user/cmsdas/2022/short_exercises/Tau/"

python haddnano.py DYJetsToLL_M50.0.root `xrdfsls -u | grep \.root`
python haddnano.py DYJetsToLL_M50.1.root `xrdfsls -u | grep \.root`
python haddnano.py DYJetsToLL_M50.root DYJetsToLL_M50.0.root DYJetsToLL_M50.1.root
xrdcp -f DYJetsToLL_M50.root $OUTPUTDIR

python haddnano.py TTToSemiLeptonic.root `xrdfsls -u | grep \.root`
xrdcp -f TTToSemiLeptonic.root $OUTPUTDIR

python haddnano.py TTTo2L2Nu.root `xrdfsls -u | grep \.root`
xrdcp -f TTTo2L2Nu.root $OUTPUTDIR

python haddnano.py WJetsToLNu.root `xrdfsls -u | grep \.root`
xrdcp -f WJetsToLNu.root $OUTPUTDIR

python haddnano.py QCD_Mu15.root `xrdfsls -u | grep \.root`
xrdcp -f QCD_Mu15.root $OUTPUTDIR

cd ${CURRENTDIR}
