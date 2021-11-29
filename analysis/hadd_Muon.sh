#!/bin/bash

cp ../scripts/haddnano.py /uscmst1b_scratch/lpc1/3DayLifetime/fojensen/
cd /uscmst1b_scratch/lpc1/3DayLifetime/fojensen

setenv CURRENTDIR pwd
setenv OUTPUTDIR "root://cmseos.fnal.gov//store/user/fojensen/cmsdas_27112021/SingleMuon/"

python haddnano.py MuonA_2018.root `xrdfsls -u | grep \.root`
python haddnano.py MuonB_2018.root `xrdfsls -u | grep \.root`
python haddnano.py MuonC_2018.root `xrdfsls -u | grep \.root`
python haddnano.py MuonD_2018.root `xrdfsls -u | grep \.root`

python haddnano.py Muon_2018.root MuonA_2018.root MuonB_2018.root MuonC_2018.root MuonD_2018.root
xrdcp -f Muon_2018.root ${OUTPUTDIR}
rm Muon*_2018.root

cd ${CURRENTDIR}
cd /uscms_data/d3/fojensen/excitedTau_06042021/CMSSW_10_6_20/src/PhysicsTools/NanoAODTools/analysis
