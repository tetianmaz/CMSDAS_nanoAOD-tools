#!/bin/bash

setenv CURRENTDIR "$PWD"
echo $CURRENTDIR

cp ../scripts/haddnano.py /uscmst1b_scratch/lpc1/3DayLifetime/fojensen/
cp splitDY.c /uscmst1b_scratch/lpc1/3DayLifetime/fojensen/
cd /uscmst1b_scratch/lpc1/3DayLifetime/fojensen

setenv OUTPUTDIR "root://cmseos.fnal.gov///store/user/fojensen/cmsdas_06122021/"

python haddnano.py DYJetsToLL_M50.0.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_cmsdas_DYJetsToLL_M50/211205_212855/0000/ | grep \.root`
root -l -q 'splitDY.c+("DYJetsToLL_M50.0.root", "DYJetsToEEMuMu_M50.0.root", "DYJetsToTauTau_M50.0.root")'

python haddnano.py DYJetsToLL_M50.1.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_cmsdas_DYJetsToLL_M50_ext/211205_212936/0000/ | grep \.root`
root -l -q 'splitDY.c+("DYJetsToLL_M50.1.root", "DYJetsToEEMuMu_M50.1.root", "DYJetsToTauTau_M50.1.root")'

python haddnano.py DYJetsToEEMuMu_M50.root DYJetsToEEMuMu_M50.0.root DYJetsToEEMuMu_M50.1.root
xrdcp -f DYJetsToEEMuMu_M50.root $OUTPUTDIR

python haddnano.py DYJetsToTauTau_M50.root DYJetsToTauTau_M50.0.root DYJetsToTauTau_M50.1.root
xrdcp -f DYJetsToTauTau_M50.root $OUTPUTDIR

#rm DYJetsTo*.root

cd ${CURRENTDIR}