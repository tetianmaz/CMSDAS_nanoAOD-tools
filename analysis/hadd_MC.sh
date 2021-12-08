#!/bin/bash

setenv CURRENTDIR "$PWD"
echo $CURRENTDIR

cp ../scripts/haddnano.py /uscmst1b_scratch/lpc1/3DayLifetime/fojensen/
cd /uscmst1b_scratch/lpc1/3DayLifetime/fojensen

setenv OUTPUTDIR "root://cmseos.fnal.gov//store/user/fojensen/cmsdas_07122021/"

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

python haddnano.py TTToSemiLeptonic.0.root `xrdfsls -u | grep \.root`
python haddnano.py TTToSemiLeptonic.1.root `xrdfsls -u | grep \.root`
python haddnano.py TTToSemiLeptonic.2.root `xrdfsls -u | grep \.root`
python haddnano.py TTToSemiLeptonic.3.root `xrdfsls -u | grep \.root`
python haddnano.py TTToSemiLeptonic.4.root `xrdfsls -u | grep \.root`
python haddnano.py TTToSemiLeptonic.5.root `xrdfsls -u | grep \.root`
python haddnano.py TTToSemiLeptonic.6.root `xrdfsls -u | grep \.root`
python haddnano.py TTToSemiLeptonic.7.root `xrdfsls -u | grep \.root`
python haddnano.py TTToSemiLeptonic.8.root `xrdfsls -u | grep \.root`
python haddnano.py TTToSemiLeptonic.9.root `xrdfsls -u | grep \.root`
python haddnano.py TTToSemiLeptonic_0.root TTToSemiLeptonic.0.root TTToSemiLeptonic.1.root TTToSemiLeptonic.2.root
python haddnano.py TTToSemiLeptonic_1.root TTToSemiLeptonic.3.root TTToSemiLeptonic.4.root TTToSemiLeptonic.5.root
python haddnano.py TTToSemiLeptonic_2.root TTToSemiLeptonic.6.root TTToSemiLeptonic.7.root TTToSemiLeptonic.8.root TTToSemiLeptonic.9.root
xrdcp -f TTToSemiLeptonic_0.root $OUTPUTDIR
xrdcp -f TTToSemiLeptonic_1.root $OUTPUTDIR
xrdcp -f TTToSemiLeptonic_2.root $OUTPUTDIR

python haddnano.py TTTo2L2Nu.0.root `xrdfsls -u | grep \0.root`
python haddnano.py TTTo2L2Nu.1.root `xrdfsls -u | grep \1.root`
python haddnano.py TTTo2L2Nu.2.root `xrdfsls -u | grep \2.root`
python haddnano.py TTTo2L2Nu.3.root `xrdfsls -u | grep \3.root`
python haddnano.py TTTo2L2Nu.4.root `xrdfsls -u | grep \4.root`
python haddnano.py TTTo2L2Nu.5.root `xrdfsls -u | grep \5.root`
python haddnano.py TTTo2L2Nu.6.root `xrdfsls -u | grep \6.root`
python haddnano.py TTTo2L2Nu.7.root `xrdfsls -u | grep \7.root`
python haddnano.py TTTo2L2Nu.8.root `xrdfsls -u | grep \8.root`
python haddnano.py TTTo2L2Nu.9.root `xrdfsls -u | grep \9.root`
python haddnano.py TTTo2L2Nu_0.root TTTo2L2Nu.0.root TTTo2L2Nu.1.root TTTo2L2Nu.2.root TTTo2L2Nu.3.root TTTo2L2Nu.4.root
python haddnano.py TTTo2L2Nu_1.root TTTo2L2Nu.5.root TTTo2L2Nu.6.root TTTo2L2Nu.7.root TTTo2L2Nu.8.root TTTo2L2Nu.9.root
xrdcp -f TTTo2L2Nu_0.root $OUTPUTDIR
xrdcp -f TTTo2L2Nu_1.root $OUTPUTDIR

cd ${CURRENTDIR}
