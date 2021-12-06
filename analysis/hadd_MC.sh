#!/bin/bash

setenv CURRENTDIR "$PWD"
echo $CURRENTDIR

cp ../scripts/haddnano.py /uscmst1b_scratch/lpc1/3DayLifetime/fojensen/
cd /uscmst1b_scratch/lpc1/3DayLifetime/fojensen

setenv OUTPUTDIR "root://cmseos.fnal.gov///store/user/fojensen/cmsdas_06122021/"

python haddnano.py DYJetsToLL_M10.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_cmsdas_DYJetsToLL_M10to50/211205_212813/0000/ | grep \.root`
xrdcp -f  DYJetsToLL_M10.root  $OUTPUTDIR

python haddnano.py WJetsToLNu.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_cmsdas_WJetsToLNu/211205_213509/0000/ | grep \.root`
xrdcp -f WJetsToLNu.root $OUTPUTDIR

python haddnano.py QCD_Mu15.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/QCD_Pt-20_MuEnrichedPt15_TuneCP5_13TeV-pythia8/crab_cmsdas_QCD_Pt-20_MuEnrichedPt15/211205_213550/0000/ | grep \.root`
xrdcp -f QCD_Mu15.root $OUTPUTDIR

python haddnano.py WW.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/WW_TuneCP5_13TeV-pythia8/crab_cmsdas_WW/211205_213303/0000/ | grep \.root`
xrdcp -f WW.root $OUTPUTDIR

python haddnano.py WZ.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/WZ_TuneCP5_13TeV-pythia8/crab_cmsdas_WZ/211205_213344/0000/ | grep \.root`
xrdcp -f WZ.root $OUTPUTDIR

python haddnano.py ZZ.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/ZZ_TuneCP5_13TeV-pythia8/crab_cmsdas_ZZ/211205_213425/0000/ | grep \.root`
xrdcp -f ZZ.root $OUTPUTDIR

python haddnano.py ST_tW_top.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_cmsdas_ST_tW_top/211205_213222/0000/ | grep \.root`
xrdcp -f ST_tW_top.root $OUTPUTDIR

python haddnano.py ST_tW_antitop.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_cmsdas_ST_tW_antitop/211205_213140/0000/ | grep \.root`
xrdcp -f ST_tW_antitop.root $OUTPUTDIR

python haddnano.py TTToSemiLeptonic.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/crab_cmsdas_TTToSemiLeptonic/211205_213017/0000/ | grep \.root`
xrdcp -f TTToSemiLeptonic.root $OUTPUTDIR

python haddnano.py TTTo2L2Nu.root `xrdfsls -u /store/user/fojensen/cmsdas_06122021/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_cmsdas_TTTo2L2Nu/211205_213059/0000/ | grep \.root`
xrdcp -f TTTo2L2Nu.root $OUTPUTDIR

cd ${CURRENTDIR}
