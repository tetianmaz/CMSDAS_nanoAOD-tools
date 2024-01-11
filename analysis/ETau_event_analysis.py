#config
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.tools import deltaPhi, deltaR

from importlib import import_module
import os
import sys
import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True


class ETauProducer(Module):
    def __init__(self):
        self.writeHistFile = True

    def beginJob(self, histFile=None, histDirName=None):
        Module.beginJob(self, histFile, histDirName)

        self.h_mass = ROOT.TH1F('mass', 'mass', 100, 50, 150)
        self.h_mT = ROOT.TH1F('mT', 'mT', 100, 0, 100)
        self.h_pT = ROOT.TH1F('pT', 'pT', 100, 0, 80)
        self.h_nbjet = ROOT.TH1F('nbjet', 'nbjet', 8, 0, 8)
        self.addObject(self.h_mass)
        self.addObject(self.h_mT)
        self.addObject(self.h_pT)
        self.addObject(self.h_nbjet)
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree        
        self.out.branch("ETau_HavePair", "I")
        self.out.branch("ETau_qq", "I")    ##same or opposite charge
        self.out.branch("ETau_EIdx", "I")   ##index of the selected electron
        self.out.branch("ETau_TauIdx", "I")   ##index of the selected tau
        self.out.branch("ETau_mT", "F")
        self.out.branch("ETau_Mass", "F")
        self.out.branch("ETau_Pt", "F")
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        #event analyzer
        genpart = Collection(event, "GenPart")
        tau = Collection(event, "Tau")
        jets = Collection(event, "Jet")
        electron = Collection(event, "Electron")
        hlt = Object(event, "HLT")
        met = Object(event, "MET")
        
        ETauSum = ROOT.TLorentzVector()
        Tauh_exists = False
        Tauele_exists = False
        no_bjets = False
        ele_idx = -999
        ele_pt = -999.
        tau_idx = -999
        tau_pt = -999

        # select events with a tau to ele, use highest pT electron
        if len(electron) > 0:
            idx = 0
            for lep in electron:
                if (lep.genPartFlav == 15 and lep.mvaFall17V2Iso_WP90 and abs(lep.eta < 2.5)): #electron selection
                    Tauele_exists=True
                    if lep.pt > ele_pt:
                        ele_idx = idx
                        ele_pt = lep.pt
                idx += 1 
            

        # select events with tau to had, use highest pT tau 
        if len(tau) > 0:
            idxt=0
            for lep in tau:
                if (abs(lep.eta < 2.3) and lep.pt > 20. and lep.genPartFlav == 5 and abs(lep.dz) < 0.2 and lep.idDeepTau2017v2p1VSe >= 4 and lep.decayMode != 5 and lep.decayMode != 6 and lep.decayMode != 7): #add more requirements here 
                    Tauh_exists=True
                #->there is a hadronic tau
                    if lep.pt > tau_pt:
                        tau_idx = idxt
                        tau_pt = lep.pt
                idxt += 1
        nbjets = 0
        for jet in jets:
            if (0 <= jet.btagDeepB <= 0.1208): 
                no_bjets = True
            else:
                nbjets+=1

        # check that hadronic and electronic tau exists, and not b background
        if Tauh_exists and Tauele_exists and no_bjets:
            #compute variables
            ETauSum+=tau[tau_idx].p4()
            ETauSum+=electron[ele_idx].p4()
            EMETmT = math.sqrt((2.*ele_pt*met.pt*(1.-math.cos(deltaPhi(electron[ele_idx].phi, met.phi)))))


            #fill branches
            self.out.fillBranch("ETau_HavePair", 1)
            self.out.fillBranch("ETau_qq", (tau[tau_idx].charge * electron[ele_idx].charge))
            self.out.fillBranch("ETau_EIdx", ele_idx)
            self.out.fillBranch("ETau_TauIdx", tau_idx)
            self.out.fillBranch("ETau_mT", ETauSum.Mt())#fix
            self.out.fillBranch("ETau_Mass", ETauSum.M())
            self.out.fillBranch("ETau_Pt", ETauSum.Pt())

            #fill histograms
            self.h_mass.Fill(ETauSum.M())
            self.h_mT.Fill(EMETmT)
            self.h_pT.Fill(ETauSum.Pt())
            self.h_nbjet.Fill(nbjets)

        else:
            self.out.fillBranch("ETau_HavePair", 0)
        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

ETauProducerConstr = lambda : ETauProducer(
)

preselection = "HLT_Ele32_WPTight_Gsf"
files = ["root://cmseos.fnal.gov//store/user/cmsdas/2023/short_exercises/Tau/DYJetsToLL__7B7D90CB-14EF-B749-B4D7-7C413FE3CCC1.root"]
p = PostProcessor(".", files, cut=preselection, branchsel=None, modules=[
                  ETauProducer()], noOut=False, histFileName="ETauProduced.root", histDirName="plots", maxEntries=100000)
p.run()

