#!/bin/bash

setenv CURRENTDIR "$PWD"
echo $CURRENTDIR

cp ../scripts/haddnano.py /uscmst1b_scratch/lpc1/3DayLifetime/fojensen/
cd /uscmst1b_scratch/lpc1/3DayLifetime/fojensen

setenv OUTPUTDIR "root://cmseos.fnal.gov//store/user/fojensen/cmsdas_07122021/"

python haddnano.py EGamma_2018A.0.root `xrdfsls -u | grep \0.root`
python haddnano.py EGamma_2018A.1.root `xrdfsls -u | grep \1.root`
python haddnano.py EGamma_2018A.2.root `xrdfsls -u | grep \2.root`
python haddnano.py EGamma_2018A.3.root `xrdfsls -u | grep \3.root`
python haddnano.py EGamma_2018A.4.root `xrdfsls -u | grep \4.root`
python haddnano.py EGamma_2018A.5.root `xrdfsls -u | grep \5.root`
python haddnano.py EGamma_2018A.6.root `xrdfsls -u | grep \6.root`
python haddnano.py EGamma_2018A.7.root `xrdfsls -u | grep \7.root`
python haddnano.py EGamma_2018A.8.root `xrdfsls -u | grep \8.root`
python haddnano.py EGamma_2018A.9.root `xrdfsls -u | grep \9.root`
python haddnano.py EGamma_2018A_0.root EGamma_2018A.0.root EGamma_2018A.1.root EGamma_2018A.2.root EGamma_2018A.3.root EGamma_2018A.4.root
python haddnano.py EGamma_2018A_1.root EGamma_2018A.5.root EGamma_2018A.6.root EGamma_2018A.7.root EGamma_2018A.8.root EGamma_2018A.9.root
xrdcp -f EGamma_2018A_0.root $OUTPUTDIR
xrdcp -f EGamma_2018A_1.root $OUTPUTDIR

python haddnano.py EGamma_2018B.root `xrdfsls -u | grep \.root`
xrdcp -f EGamma_2018B.root $OUTPUTDIR

python haddnano.py EGamma_2018C.root `xrdfsls -u | grep \.root`
xrdcp -f EGamma_2018C.root $OUTPUTDIR

python haddnano.py EGamma_2018D.0.root `xrdfsls -u | grep \0.root`
python haddnano.py EGamma_2018D.1.root `xrdfsls -u | grep \1.root`
python haddnano.py EGamma_2018D.2.root `xrdfsls -u | grep \2.root`
python haddnano.py EGamma_2018D.3.root `xrdfsls -u | grep \3.root`
python haddnano.py EGamma_2018D.4.root `xrdfsls -u | grep \4.root`
python haddnano.py EGamma_2018D.5.root `xrdfsls -u | grep \5.root`
python haddnano.py EGamma_2018D.6.root `xrdfsls -u | grep \6.root`
python haddnano.py EGamma_2018D.7.root `xrdfsls -u | grep \7.root`
python haddnano.py EGamma_2018D.8.root `xrdfsls -u | grep \8.root`
python haddnano.py EGamma_2018D.9.root `xrdfsls -u | grep \9.root`
python haddnano.py EGamma_2018D_0.root EGamma_2018D.0.root EGamma_2018D.1.root EGamma_2018D.2.root
python haddnano.py EGamma_2018D_1.root EGamma_2018D.3.root EGamma_2018D.4.root EGamma_2018D.5.root
python haddnano.py EGamma_2018D_2.root EGamma_2018D.6.root EGamma_2018D.7.root EGamma_2018D.8.root EGamma_2018D.9.root
xrdcp -f EGamma_2018D_0.root $OUTPUTDIR
xrdcp -f EGamma_2018D_1.root $OUTPUTDIR
xrdcp -f EGamma_2018D_2.root $OUTPUTDIR

cd ${CURRENTDIR}
