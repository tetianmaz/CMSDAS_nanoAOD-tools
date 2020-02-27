print "top of crab_script.py"

#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

from PhysicsTools.NanoAODTools.postprocessing.examples.ZProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import puWeight_2018
from PhysicsTools.NanoAODTools.postprocessing.modules.common.countHistogramsModule import countHistogramsModule

from TauPOG.TauIDSFs.TauIDSFTool import TauIDSFTool
from TauPOG.TauIDSFs.TauIDSFTool import TauFESTool
from TauPOG.TauIDSFs.TauIDSFTool import TauESTool

#testfile = [
#   "root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18NanoAODv6/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/20000/9E6A9BA6-C187-0F4E-8A45-01B2F2F33E11.root"
   #"root://cmsxrootd.fnal.gov///store/mc/RunIIAutumn18NanoAODv6/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/250000/475C3783-6848-2448-99BE-32B8D5E208AB.root"
#   "root://cmsxrootd.fnal.gov///store/mc/RunIIAutumn18NanoAODv6/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/260000/C00024AD-3D0D-DE45-949F-E56A81BDDCA7.root"
   #"root://xmsxrootd.fnal.gov//store/mc/RunIIAutumn18NanoAODv6/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/Nano25Oct2019_4cores5k_102X_upgrade2018_realistic_v20-v1/250000/0C724FD3-4823-614E-A075-E48A39EBD2D3.root"
#]

#cut_ = "HLT_IsoMu27"
#cut_ = cut_ + " && Sum$(Muon_pt>=30. && TMath::Abs(Muon_eta)<2.1 && Muon_tightId)>0"
#cut_ = cut_ + " && Sum$(Tau_pt>=20. && TMath::Abs(Tau_eta)<2.3 && (128&Tau_idDeepTau2017v2p1VSjet) && (128&Tau_idDeepTau2017v2p1VSe) && (8&Tau_idDeepTau2017v2p1VSmu))>0"
#cut_ = cut_ + " && Sum$(Photon_pt>=45. && TMath::Abs(Photon_eta)<2.6 && Photon_mvaID_WP90 && (Photon_electronVeto||!Photon_pixelSeed))==0"
#cut_ = cut_ + " && Sum$(Jet_pt>=20. && TMath::Abs(Jet_eta)<2.5 && (4&Jet_jetId) && Jet_btagDeepB>=0.7527)==0"
#cut_ = cut_ + " && Sum$(Electron_pt>=30. && TMath::Abs(Electron_eta)<2.5 && Electron_mvaFall17V2Iso_WP80)==0"
cut_ = ""

#from PSet import franksoptions
#modules_=[]
#if franksoptions.isMC==True:
modules_ = [ZProducerConstr(True), puWeight_2018()]
#else:
#modules_ = [ZProducerConstr(False)]

p=PostProcessor(
   outputDir = ".",
   inputFiles = inputFiles(),
 #  inputFiles = testfile,
   cut = cut_,
   modules = modules_,
   provenance = True,
   fwkJobReport = True,
   jsonInput = runsAndLumis(),
   outputbranchsel = "keep_and_drop.txt"
)
p.run()

print "DONE"

