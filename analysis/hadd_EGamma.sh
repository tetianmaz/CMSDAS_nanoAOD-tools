#!/bin/bash

setenv CURRENTDIR "$PWD"
echo $CURRENTDIR

cp ../scripts/haddnano.py /uscmst1b_scratch/lpc1/3DayLifetime/fojensen/
cd /uscmst1b_scratch/lpc1/3DayLifetime/fojensen

setenv OUTPUTDIR "root://cmseos.fnal.gov//store/user/fojensen/cmsdas_06122021/"

python haddnano.py EGamma_2018A.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/EGamma/crab_cmsdas_EGamma_2018A/211205_211905/0000/ | grep \.root`
xrdcp -f EGamma_2018A.root $OUTPUTDIR

python haddnano.py EGamma_2018B.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/EGamma/crab_cmsdas_EGamma_2018B/211205_211946/0000/ | grep \.root`
xrdcp -f EGamma_2018B.root $OUTPUTDIR

python haddnano.py EGamma_2018C.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/EGamma/crab_cmsdas_EGamma_2018C/211205_212027/0000/ | grep \.root`
xrdcp -f EGamma_2018C.root $OUTPUTDIR

python haddnano.py EGamma_2018D.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/EGamma/crab_cmsdas_EGamma_2018D/211205_212110/0000/ | grep \.root`
xrdcp -f EGamma_2018D.root $OUTPUTDIR

cd ${CURRENTDIR}
