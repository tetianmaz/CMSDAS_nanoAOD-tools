#!/bin/bash

setenv CURRENTDIR "$PWD"
echo $CURRENTDIR

cp ../scripts/haddnano.py /uscmst1b_scratch/lpc1/3DayLifetime/fojensen/
cd /uscmst1b_scratch/lpc1/3DayLifetime/fojensen

setenv OUTPUTDIR "root://cmseos.fnal.gov//store/user/cmsdas/2022/short_exercises/Tau/"

python haddnano.py SingleMuon_2018A.root `xrdfsls -u /store/user/fojensen/cmsdas_27112021/SingleMuon/crab_cmsdas_Muon_2018A/211127_223308/0000/ | grep \.root`
xrdcp -f SingleMuon_2018A.root $OUTPUTDIR

python haddnano.py SingleMuon_2018B.root `xrdfsls -u /store/user/fojensen/cmsdas_27112021/SingleMuon/crab_cmsdas_Muon_2018B/211127_174401/0000/ | grep \.root`
xrdcp -f SingleMuon_2018B.root $OUTPUTDIR

python haddnano.py SingleMuon_2018C.root `xrdfsls -u /store/user/fojensen/cmsdas_27112021/SingleMuon/crab_cmsdas_Muon_2018C/211127_174505/0000/ | grep \.root`
xrdcp -f SingleMuon_2018C.root $OUTPUTDIR

python haddnano.py SingleMuon_2018D.root `xrdfsls -u /store/user/fojensen/cmsdas_27112021/SingleMuon/crab_cmsdas_Muon_2018D/211127_174550/0000/ | grep \.root`
xrdcp -f SingleMuon_2018D.root $OUTPUTDIR

#python haddnano.py SingleMuon_2018.root SingleMuon_2018A.root SingleMuon_2018B.root SingleMuon_2018C.root SingleMuon_2018D.root
#xrdcp -f SingleMuon_2018.root $OUTPUTDIR

#rm SingleMuon*_2018.root

cd ${CURRENTDIR}
