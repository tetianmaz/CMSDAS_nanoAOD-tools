import datetime
then = datetime.datetime.now()
print ("Start date and time: ", then.strftime("%Y-%m-%d %H:%M:%S"))

#!/usr/bin/env python
from exampleModule import *
#from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
#from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from importlib import import_module
import os
import sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
# soon to be deprecated
# new way of using jme uncertainty


# Function parameters
# (isMC=True, dataYear=2016, runPeriod="B", jesUncert="Total", redojec=False, jetType = "AK4PFchs", noGroom=False)
# All other parameters will be set in the helper module

#jmeCorrections = createJMECorrector(
#    True, "2016", "B", "Total", True, "AK4PFchs", False)

#fnames = ["/eos/cms/store/mc/RunIISummer16NanoAODv5/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext2-v1/120000/FF69DF6E-2494-F543-95BF-F919B911CD23.root"]
#fnames = ["root://cmseos.fnal.gov//store/user/cmsdas/2022/short_exercises/Tau/DYJetsToLL__7B7D90CB-14EF-B749-B4D7-7C413FE3CCC1.root"]
fnames = ["root://cmseos.fnal.gov//store/user/cmsdas/2023/short_exercises/Tau/DYJetsToLL__7B7D90CB-14EF-B749-B4D7-7C413FE3CCC1.root"]
#fnames = ["root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18NanoAODv9/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/593919B4-087D-7A45-8DC4-3FA23EF86339.root"]
#from PhysicsTools.NanoAODTools.postprocessing.examples.ZProducer import ZProducerConstr
#from PhysicsTools.NanoAODTools.postprocessing.examples.ETauProducer import ETauProducerConstr
#from PhysicsTools.NanoAODTools.postprocessing.examples.MuTauProducer import MuTauProducerConstr
#from PhysicsTools.NanoAODTools.postprocessing.examples.TauTauProducer import TauTauProducerConstr
from PhysicsTools.NanoAODTools.postprocessing.examples.JetProducer import JetProducerConstr
# p=PostProcessor(".",fnames,"Jet_pt>150","",[jetmetUncertainties2016(),exampleModuleConstr()],provenance=True)
p = PostProcessor(
    outputDir = ".",
    inputFiles = fnames,
    #inputFiles = [sys.argv[1]],
    cut = "Sum$(Muon_pt>=12. && TMath::Abs(Muon_eta)<2.4 && Muon_tightId && Muon_pfIsoId>=4)==1",
    #modules = [exampleModuleConstr()],
    #modules = [JetProducerConstr(2018)], 
    modules = [ZProducerConstr(False), MuTauProducerConstr(), JetProducerConstr(2018)],
    friend = True,
    provenance=True,
    haddFileName = "tree.root"
)
p.run()

now = datetime.datetime.now()
print ("Finish date and time: ", now.strftime("%Y-%m-%d %H:%M:%S"))
duration = now - then
print ("Total seconds elapsed: ", duration.total_seconds())
