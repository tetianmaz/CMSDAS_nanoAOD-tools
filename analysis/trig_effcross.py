#!/usr/bin/env python
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from importlib import import_module
import os
import sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True


class ExampleAnalysis(Module):
    def __init__(self):
        self.writeHistFile = True

    def beginJob(self, histFile=None, histDirName=None):
        Module.beginJob(self, histFile, histDirName)

        self.h_denom = ROOT.TH1F('denom', 'denom', 100, 0, 200)
        self.h_num = ROOT.TH1F('num', 'num', 100, 0, 200)
        self.addObject(self.h_denom)
	self.addObject(self.h_num)

    def analyze(self, event):
        genpart = Collection(event, "GenPart")
        tau = Collection(event, "Tau")
        electron = Collection(event, "Electron")
        hlt = Object(event, "HLT")

        Tauh_exists = False
        Tauele_exists = False
        ele_idx = -999
        ele_pt = -999.

        # select events with a tau to ele
        if len(electron) > 0:
            idx = 0
            for lep in electron:
                if (lep.genPartFlav == 15 and lep.mvaFall17V2Iso_WP90 and abs(lep.eta < 2.5)): #electron selection
                    Tauele_exists=True
                    if lep.pt > ele_pt:
                        ele_idx = idx
                        ele_pt = lep.pt
                idx += 1 

        if len(tau) > 0:
            for lep in tau:
                if (abs(lep.eta < 2.3) and lep.pt > 20. and lep.genPartFlav == 5 and abs(lep.dz) < 0.2 and lep.idDeepTau2017v2p1VSe >= 4 and lep.decayMode != 5 and lep.decayMode != 6 and lep.decayMode != 7): #add more requirements here 
                    Tauh_exists=True
                #->there is a hadronic tau

        if Tauh_exists and Tauele_exists:
            self.h_denom.Fill(electron[ele_idx].pt)
            singlee = hlt.Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1 #only measuring efficiency when both tauele and tauh exist.
            if singlee:
                self.h_num.Fill(electron[ele_idx].pt)
        return True


preselection = ""
#should we have this in?
files = ["root://cmseos.fnal.gov//store/user/cmsdas/2023/short_exercises/Tau/DYJetsToLL__7B7D90CB-14EF-B749-B4D7-7C413FE3CCC1.root"]
p = PostProcessor(".", files, cut=preselection, branchsel=None, modules=[
                  ExampleAnalysis()], noOut=False, histFileName="histeffcross.root", histDirName="plots", maxEntries=10000)
p.run()
