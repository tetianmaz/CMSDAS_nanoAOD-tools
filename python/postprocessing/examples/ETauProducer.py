import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import deltaPhi, deltaR
import math

class ETauProducer(Module):
    def __init__(self):
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
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
        """process event, return True (go to next module) or False (fail, go to next event)"""

        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

ETauProducerConstr = lambda : ETauProducer(
)

