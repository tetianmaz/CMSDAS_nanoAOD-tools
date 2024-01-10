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

        self.h_denom = ROOT.TH1F('denom', 'denom', 100, 0, 1000)
        self.h_num = ROOT.TH1F('num', 'num', 100, 0, 1000)
        self.addObject(self.h_denom)
	self.addObject(self.h_num)

    def analyze(self, event):
        genpart = Collection(event, "GenPart")
        htau = Collection(event, "GenVisTau")
        electron = Collection(event, "Electron")
        hlt = Object(event, "HLT")

        Tauh_exists = False
        Tauele_exists = False
        Tauele_idx = -999

        # select events with a tau to had
        if len(electron) > 0:
            for lep in electron:
                if lep.genPartFlav == 15 & lep.mvaFall17V2Iso_WP90: #electron selection
                    Tauele_exists=True

        if len(htau) > 0:
            for lep in htau:
                if 1 == 1: #add more requirements here
                    Tauh_exists=True
                #->there is a hadronic tau

        if Tauh_exists & Tauele_exists:
            self.h_denom.Fill(electron[0].pt)
            singlee = hlt.Ele32_WPTight_Gsf #only measuring efficiency when both tauele and tauh exist.
            if singlee:
                self.h_num.Fill(electron[0].pt) #which thing
        return True


preselection = "Electron_eta < 2.5 && Electron_eta > -2.5"
#should we have this in?
files = ["root://cmseos.fnal.gov//store/user/cmsdas/2023/short_exercises/Tau/DYJetsToLL__7B7D90CB-14EF-B749-B4D7-7C413FE3CCC1.root"]
p = PostProcessor(".", files, cut=preselection, branchsel=None, modules=[
                  ExampleAnalysis()], noOut=False, histFileName="histeff.root", histDirName="plots", maxEntries=1000)
p.run()
