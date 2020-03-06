import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from PhysicsTools.NanoAODTools.postprocessing.tools import deltaR

class JetProducer(Module):
    def __init__(self):
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("JetProducer_nJet", "I")
        self.out.branch("JetProducer_nBJetL", "I")
        self.out.branch("JetProducer_nBJetM", "I")
        self.out.branch("JetProducer_nBJetT", "I")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
 
        taus = Collection(event, "Tau")
        jets = Collection(event, "Jet")

        JetProducer_nJet = 0
        JetProducer_nBJetL = JetProducer_nBJetM = JetProducer_nBJetT = 0

        for jet in jets:
            if jet.pt>20 and abs(jet.eta)<2.5 and (4&jet.jetId):
                mindr = 9.
                for tau in taus:
                    if (128&tau.idDeepTau2017v2p1VSjet):
                        mindr_ = deltaR(jet.eta, jet.phi, tau.eta, tau.phi)
                        if mindr_<mindr:
                           mindr = mindr_
                if mindr>=0.4:
                    JetProducer_nJet = JetProducer_nJet + 1
                    if jet.btagDeepB>=0.1241:
                        JetProducer_nBJetL = JetProducer_nBJetL + 1
                        if jet.btagDeepB>=0.4184:
                            JetProducer_nBJetM = JetProducer_nBJetM + 1
                            if jet.btagDeepB>=0.7527:
                                JetProducer_nBJetT = JetProducer_nBJetT + 1
       
        self.out.fillBranch("JetProducer_nBJetL", JetProducer_nBJetL)
        self.out.fillBranch("JetProducer_nBJetM", JetProducer_nBJetM)
        self.out.fillBranch("JetProducer_nBJetT", JetProducer_nBJetT)
        self.out.fillBranch("JetProducer_nJet", JetProducer_nJet)
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

JetProducerConstr = lambda : JetProducer(
)

