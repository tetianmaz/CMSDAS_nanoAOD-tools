#!/bin/bash

setenv CURRENTDIR "$PWD"
echo $CURRENTDIR

cp ../scripts/haddnano.py /uscmst1b_scratch/lpc1/3DayLifetime/fojensen/
cd /uscmst1b_scratch/lpc1/3DayLifetime/fojensen

setenv OUTPUTDIR "root://cmseos.fnal.gov//store/user/cmsdas/2022/short_exercises/Tau/"

python haddnano.py DYJetsToLL_M50.0.root `xrdfsls -u /store/user/fojensen/cmsdas_28112021/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_cmsdas_DYJetsToLL_M50/211129_053308/0000/ | grep \.root`
python haddnano.py DYJetsToLL_M50.1.root `xrdfsls -u /store/user/fojensen/cmsdas_28112021/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_cmsdas_DYJetsToLL_M50_ext/211129_053354/0000/ | grep \.root`
python haddnano.py DYJetsToLL_M50.root DYJetsToLL_M50.0.root DYJetsToLL_M50.1.root
xrdcp -f DYJetsToLL_M50.root $OUTPUTDIR

python haddnano.py TTToSemiLeptonic.root `xrdfsls -u /store/user/fojensen/cmsdas_28112021/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/crab_cmsdas_TTToSemiLeptonic/211129_053443/0000/ | grep \.root`
xrdcp -f TTToSemiLeptonic.root $OUTPUTDIR

python haddnano.py TTTo2L2Nu.root `xrdfsls -u /store/user/fojensen/cmsdas_28112021/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_cmsdas_TTTo2L2Nu/211129_053529/0000/ | grep \.root`
xrdcp -f TTTo2L2Nu.root $OUTPUTDIR

python haddnano.py WJetsToLNu.root `xrdfsls -u /store/user/fojensen/cmsdas_28112021/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_cmsdas_WJetsToLNu/211129_054011/0000/ | grep \.root`
xrdcp -f WJetsToLNu.root $OUTPUTDIR

python haddnano.py QCD_Mu15.root `xrdfsls -u /store/user/fojensen/cmsdas_28112021/QCD_Pt-20_MuEnrichedPt15_TuneCP5_13TeV-pythia8/crab_cmsdas_QCD_Pt-20_MuEnrichedPt15/211129_054108/0000/ | grep \.root`
xrdcp -f QCD_Mu15.root $OUTPUTDIR

#python haddnano.py .root `xrdfsls -u | grep \.root`
#xrdcp -f .root $OUTPUTDIR

#rm *_2018.root

cd ${CURRENTDIR}
