import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import deltaPhi, deltaR
import math

class TauTauProducer(Module):
    def __init__(self):
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("TauTau_HavePair", "I")
        self.out.branch("TauTau_qq", "I")    ##same or opposite charge
        self.out.branch("TauTau_Tau1Idx", "I")   ##index of the selected tau1
        self.out.branch("TauTau_Tau2Idx", "I")   ##index of the selected tau2
        #self.out.branch("TauTau_mT", "F")
        self.out.branch("TauTau_Mass", "F")
        self.out.branch("TauTau_Pt", "F")
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

TauTauProducerConstr = lambda : TauTauProducer(
)

