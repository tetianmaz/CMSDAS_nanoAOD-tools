#!/bin/bash

setenv CURRENTDIR "$PWD"
echo $CURRENTDIR

cp ../scripts/haddnano.py /uscmst1b_scratch/lpc1/3DayLifetime/fojensen/
cd /uscmst1b_scratch/lpc1/3DayLifetime/fojensen

setenv OUTPUTDIR "root://cmseos.fnal.gov//store/user/fojensen/cmsdas_10122021/"

python haddnano.py DYJetsToLL_M10.root `xrdfsls -u | grep \.root`
xrdcp -f  DYJetsToLL_M10.root  $OUTPUTDIR

python haddnano.py WJetsToLNu.root `xrdfsls -u | grep \.root`
xrdcp -f WJetsToLNu.root $OUTPUTDIR

python haddnano.py QCD_Mu15.root `xrdfsls -u | grep \.root`
xrdcp -f QCD_Mu15.root $OUTPUTDIR

python haddnano.py WW.root `xrdfsls -u | grep \.root`
xrdcp -f WW.root $OUTPUTDIR

python haddnano.py WZ.root `xrdfsls -u | grep \.root`
xrdcp -f WZ.root $OUTPUTDIR

python haddnano.py ZZ.root `xrdfsls -u | grep \.root`
xrdcp -f ZZ.root $OUTPUTDIR

python haddnano.py ST_tW_top.root `xrdfsls -u | grep \.root`
xrdcp -f ST_tW_top.root $OUTPUTDIR

python haddnano.py ST_tW_antitop.root `xrdfsls -u | grep \.root`
xrdcp -f ST_tW_antitop.root $OUTPUTDIR

python haddnano.py TTToSemiLeptonic.root `xrdfsls -u | grep \.root`
xrdcp -f TTToSemiLeptonic.root $OUTPUTDIR

python haddnano.py TTTo2L2Nu.root `xrdfsls -u | grep \0.root`
xrdcp -f TTTo2L2Nu.root $OUTPUTDIR

cd ${CURRENTDIR}
