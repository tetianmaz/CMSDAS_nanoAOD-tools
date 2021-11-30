import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import deltaR

class JetProducer(Module):
    def __init__(self, year_):
        self.year__ = year_
        self.wp = [0, 0, 0]
        #print "chosen year %d" % self.year__
        #https://twiki.cern.ch/CMS/BtagRecommendation2016Legacy
        if self.year__==2015 or self.year__==2016:
            self.wp[0] = 0.2217
            self.wp[1] = 0.6321
            self.wp[2] = 0.8953
        #https://twiki.cern.ch/CMS/BtagRecommendation106XUL17
        elif self.year__==2017:
            self.wp[0] = 0.1355
            self.wp[1] = 0.4506
            self.wp[2] = 0.7738
        #https://twiki.cern.ch/CMS/BtagRecommendation106XUL18
        elif self.year__==2018: 
            self.wp[0] = 0.1208
            self.wp[1] = 0.4168
            self.wp[2] = 0.7665
        else :
            print "*** JetProducer: no year given! ***"
            self.wp[0] = 0.1208
            self.wp[1] = 0.4168
            self.wp[2] = 0.7665

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

        jets = Collection(event, "Jet")

        nJet = 0
        nBJetL = nBJetM = nBJetT = 0

        for jet in jets:
            if jet.pt>=20. and abs(jet.eta)<2.5 and (4&jet.jetId):
                nJet = nJet+1
                if jet.btagDeepB >= self.wp[0]:
                    nBJetL = nBJetL + 1
                    if jet.btagDeepB >= self.wp[1]:
                        nBJetM = nBJetM + 1
                        if jet.btagDeepB >= self.wp[2]:
                            nBJetT = nBJetT + 1

        self.out.fillBranch("JetProducer_nJet", nJet)
        self.out.fillBranch("JetProducer_nBJetL", nBJetL)
        self.out.fillBranch("JetProducer_nBJetM", nBJetM)
        self.out.fillBranch("JetProducer_nBJetT", nBJetT)
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

JetProducerConstr = lambda year : JetProducer(
    year_ = year,
)

