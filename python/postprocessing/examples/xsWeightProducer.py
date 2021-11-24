import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
class xsWeightProducer(Module):
    def __init__(self, xsWeight_, year_):
        #pass
        self.lumiWeight = 1.
        #if year_==2015: self.lumiWeight=19500.
        #if year_==2016: self.lumiWeight=16800.
        if year_==2016: self.lumiWeight=36330.
        if year_==2017: self.lumiWeight=41480.
        if year_==2018: self.lumiWeight=59830.
        self.xsWeight = xsWeight_
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("xsWeight", "F")
        self.out.branch("lumiWeight", "F")
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        #xsWeight = 1. 
        self.out.fillBranch("xsWeight", self.xsWeight)
        self.out.fillBranch("lumiWeight", self.lumiWeight)
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed


xsWeightProducerConstr = lambda xsWeight, year: xsWeightProducer(
   xsWeight_ = xsWeight,
   year_ =  year
)

