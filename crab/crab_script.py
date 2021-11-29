import datetime
then = datetime.datetime.now()
print ("Start date and time: ", then.strftime("%Y-%m-%d %H:%M:%S"))

#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import runsAndLumis

import sys
print sys.argv
for arg in sys.argv:
    print arg
 
##interactive
#if len(sys.argv)<2:
#    print "missing year parameter!"
#year = int(sys.argv[1])

#crab
#== CMSSW: ['crab_script.py', '1', 'arg1=2016'] data
#if len(sys.argv)<3:
#    print "missing year parameter!"
#year = int(sys.argv[2][5:])
year=2018

#testfile = [
#    "root://cmseos.fnal.gov//store/user/cmsdas/2022/short_exercises/Tau/WJetsToLNu__AE18A33F-9CF5-BC4E-A1E9-46F7BF382AF1.root"
    #"root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18NanoAODv9/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/AE18A33F-9CF5-BC4E-A1E9-46F7BF382AF1.root"
    #"root://cmseos.fnal.gov//store/user/cmsdas/2022/short_exercises/Tau/DYJetsToLL__7B7D90CB-14EF-B749-B4D7-7C413FE3CCC1.root"
    #"root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18NanoAODv9/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/7B7D90CB-14EF-B749-B4D7-7C413FE3CCC1.root"
    #"root://cmseos.fnal.gov//store/user/cmsdas/2022/short_exercises/Tau/TTTo2L2Nu__1656732C-0CD4-F54B-B39D-19CA08E18A77.root"
    #"root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18NanoAODv9/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/1656732C-0CD4-F54B-B39D-19CA08E18A77.root",
#]
#print testfile

cut_TauTau = "Sum$(Tau_pt>=20.0 && TMath::Abs(Tau_eta)<2.3 && Tau_decayMode!=5 && Tau_decayMode!=6 && Tau_decayMode!=7 && (1&Tau_idDeepTau2017v2p1VSjet) && (1&Tau_idDeepTau2017v2p1VSmu) && (1&Tau_idDeepTau2017v2p1VSe))>=2"
cut_Tau    = "Sum$(Tau_pt>=180. && TMath::Abs(Tau_eta)<2.3 && Tau_decayMode!=5 && Tau_decayMode!=6 && Tau_decayMode!=7 && (1&Tau_idDeepTau2017v2p1VSjet) && (1&Tau_idDeepTau2017v2p1VSmu) && (1&Tau_idDeepTau2017v2p1VSe))>=1"
cut_TauMET = "Sum$(Tau_pt>=50.0 && TMath::Abs(Tau_eta)<2.3 && Tau_decayMode!=5 && Tau_decayMode!=6 && Tau_decayMode!=7 && (1&Tau_idDeepTau2017v2p1VSjet) && (1&Tau_idDeepTau2017v2p1VSmu) && (1&Tau_idDeepTau2017v2p1VSe))>=1 && MET_pt>=90."
cut_ETau   = "Sum$(Tau_pt>=20.0 && TMath::Abs(Tau_eta)<2.3 && Tau_decayMode!=5 && Tau_decayMode!=6 && Tau_decayMode!=7 && (1&Tau_idDeepTau2017v2p1VSjet) && (1&Tau_idDeepTau2017v2p1VSmu) && (1&Tau_idDeepTau2017v2p1VSe))>=1 && Sum$(TMath::Abs(Electron_eta)<2.5 && Electron_pt>=12. && (Electron_mvaFall17V2Iso_WPL||Electron_mvaFall17V2noIso_WPL))>0"
cut_MuTau  = "Sum$(Tau_pt>=20.0 && TMath::Abs(Tau_eta)<2.3 && Tau_decayMode!=5 && Tau_decayMode!=6 && Tau_decayMode!=7 && (1&Tau_idDeepTau2017v2p1VSjet) && (1&Tau_idDeepTau2017v2p1VSmu) && (1&Tau_idDeepTau2017v2p1VSe))>=1 && Sum$(TMath::Abs(Muon_eta)<2.4 && Muon_pt>=8. && Muon_looseId)>0"
cut_EMu    = "Sum$(TMath::Abs(Electron_eta)<2.5 && Electron_pt>=12. && (Electron_mvaFall17V2Iso_WPL||Electron_mvaFall17V2noIso_WPL))>0 && Sum$(TMath::Abs(Muon_eta)<2.4 && Muon_pt>=8. && Muon_looseId)>0"
#https://twiki.cern.ch/CMS/MissingETOptionalFiltersRun2
cut_Flag16   = "Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_BadPFMuonDzFilter && Flag_eeBadScFilter"
cut_Flag1718 = "Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_BadPFMuonDzFilter && Flag_eeBadScFilter && Flag_ecalBadCalibFilter"
if year==2016:
    cut_Flag = cut_Flag16
elif year==2017 or year==2018:
    cut_Flag = cut_Flag1718
cut_ = "("+ cut_ETau + " || " + cut_MuTau + " || " + cut_TauTau + " || " + cut_Tau + " || " + cut_TauMET + " || " + cut_EMu + ") && (" + cut_Flag + ")"
print cut_

from PhysicsTools.NanoAODTools.postprocessing.examples.ZProducer import ZProducerConstr
from PhysicsTools.NanoAODTools.postprocessing.examples.ETauProducer import ETauProducerConstr
from PhysicsTools.NanoAODTools.postprocessing.examples.MuTauProducer import MuTauProducerConstr
from PhysicsTools.NanoAODTools.postprocessing.examples.TauTauProducer import TauTauProducerConstr
from PhysicsTools.NanoAODTools.postprocessing.examples.JetProducer import JetProducerConstr

applyZVeto=False
modules_ = [ZProducerConstr(applyZVeto), ETauProducerConstr(), MuTauProducerConstr(), TauTauProducerConstr(), JetProducerConstr(year)]

isMC = False
if isMC:
    if len(sys.argv)==3: w = float(sys.argv[2]) #interactive
    if len(sys.argv)==4: w = eval(str(sys.argv[3])[5:]) #crab
    from PhysicsTools.NanoAODTools.postprocessing.examples.xsWeightProducer import xsWeightProducerConstr
    modules_ += [xsWeightProducerConstr(w, year)]

p=PostProcessor(
    outputDir = "./",
    inputFiles = inputFiles(),
    #inputFiles = [sys.argv[1]],
    #inputFiles = testfile,
    cut = cut_,
    modules = modules_,
    #maxEntries = 10000,
    provenance = True,
    fwkJobReport = True,
    jsonInput = runsAndLumis(),
    #outputbranchsel = "keep_and_drop.txt"
    #outputbranchsel = "keep_all.txt",
    #histFileName = "myhists.root",
    #histDirName = "histdir"    
)
p.run()

now = datetime.datetime.now()
print ("Finish date and time: ", now.strftime("%Y-%m-%d %H:%M:%S"))
duration = now - then
print ("Total seconds elapsed: ", duration.total_seconds())
