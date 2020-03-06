import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from MuonPOG.MuonSFs.MuonSFTool import MuonSFTool
muonSFTool = MuonSFTool()

class ZMuMuProducer(Module):
    def __init__(self, isMC_):
        self.isMC__ = isMC_
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("ZMuMuProducer_Mass", "F")
        self.out.branch("ZMuMuProducer_Pt", "F")
        self.out.branch("ZMuMuProducer_Eta", "F")
        self.out.branch("ZMuMuProducer_Phi", "F")
        self.out.branch("ZMuMuProducer_havePair", "O")
        self.out.branch("ZMuMuProducer_MuIdx1", "I")
        self.out.branch("ZMuMuProducer_MuIdx2", "I")
        if self.isMC__:
           self.out.branch("ZMuMuProducer_SFMuonID", "F")
           self.out.branch("ZMuMuProducer_SFMuonISO", "F")
           self.out.branch("ZMuMuProducer_SFMuonTrigger", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        #print "ZMuMuProducer"

        havePair = False 
        Mass = Pt = Eta = Phi = 0
        MuIdx1 = MuIdx2 = -1
        if self.isMC__:
           SFMuonID = SFMuonISO = 0
           SFMuonTrigger = 0

        muons = Collection(event, "Muon")
        for i, muon1 in enumerate(muons):
           if muon1.pt>=30. and abs(muon1.eta)<2.1 and muon1.mediumId and muon1.pfIsoId>=4:
              for j, muon2 in enumerate(muons):
                  if muon2.pt>=20. and abs(muon2.eta)<2.4 and muon2.mediumId and muon2.pfIsoId>=4:
                     if muon1.charge*muon2.charge<0:
                        if not havePair:
                           havePair = True
                           recoZ = muon1.p4()+muon2.p4();
                           Mass = recoZ.M();
                           Pt = recoZ.Pt();
                           Eta = recoZ.Eta();
                           Phi = recoZ.Phi();
                           if muon1.pt>=muon2.pt:
                              MuIdx1 = i
                              MuIdx2 = j
                           else :
                              MuIdx1 = j
                              MuIdx2 = i
                           if self.isMC__:
                              SFMuonID = muonSFTool.getSF_MediumID(muon1.pt, muon1.eta) * muonSFTool.getSF_MediumID(muon2.pt, muon2.eta)
                              SFMuonISO = muonSFTool.getSF_ISO_MediumID(muon1.pt, muon1.eta, 4) * muonSFTool.getSF_ISO_MediumID(muon2.pt, muon2.eta, 4)
                              SFMuonTrigger = muonSFTool.getSF_Trigger(muon1.pt, muon1.eta)
                           if abs(muon2.eta)<2.1 and muon2.pt>muon1.pt:
                                 SFMuonTrigger = muonSFTool.getSF_Trigger(muon2.pt, muon2.eta)

        self.out.fillBranch("ZMuMuProducer_havePair", havePair)              
        self.out.fillBranch("ZMuMuProducer_Mass", Mass)
        self.out.fillBranch("ZMuMuProducer_Pt", Pt)
        self.out.fillBranch("ZMuMuProducer_Eta", Eta)
        self.out.fillBranch("ZMuMuProducer_Phi", Phi)
        self.out.fillBranch("ZMuMuProducer_MuIdx1", MuIdx1)
        self.out.fillBranch("ZMuMuProducer_MuIdx2", MuIdx2)
        if self.isMC__:
           self.out.fillBranch("ZMuMuProducer_SFMuonID", SFMuonID)
           self.out.fillBranch("ZMuMuProducer_SFMuonISO", SFMuonISO)
           self.out.fillBranch("ZMuMuProducer_SFMuonTrigger", SFMuonTrigger)
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

ZMuMuProducerConstr = lambda isMC : ZMuMuProducer(
   isMC_ = isMC
)

