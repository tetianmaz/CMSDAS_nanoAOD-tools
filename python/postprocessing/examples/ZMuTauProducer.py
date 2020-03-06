import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from TauPOG.TauIDSFs.TauIDSFTool import TauIDSFTool
tauSFTool_jet = TauIDSFTool('2018ReReco','DeepTau2017v2p1VSjet','VVTight')
tauSFTool_ele = TauIDSFTool('2018ReReco','DeepTau2017v2p1VSe','VVTight')
tauSFTool_muo = TauIDSFTool('2018ReReco','DeepTau2017v2p1VSmu','Tight')
from TauPOG.TauIDSFs.TauIDSFTool import TauESTool
testool_jet = TauESTool('2018ReReco','DeepTau2017v2p1VSjet')
from TauPOG.TauIDSFs.TauIDSFTool import TauFESTool
testool_ele = TauFESTool('2018ReReco','DeepTau2017v2p1VSe')

from MuonPOG.MuonSFs.MuonSFTool import MuonSFTool
muonSFTool = MuonSFTool()

from PhysicsTools.NanoAODTools.postprocessing.tools import deltaR

class ZMuTauProducer(Module):
    def __init__(self, isMC_):
        self.isMC__ = isMC_
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("ZMuTauProducer_mt", "F")
        self.out.branch("ZMuTauProducer_MuonIdx", "I")
        self.out.branch("ZMuTauProducer_TauIdx", "I")
        self.out.branch("ZMuTauProducer_havePair", "O")
        self.out.branch("ZMuTauProducer_Mass", "F")
        self.out.branch("ZMuTauProducer_Pt", "F")
        self.out.branch("ZMuTauProducer_Eta", "F")
        self.out.branch("ZMuTauProducer_Phi", "F")
        self.out.branch("ZMuTauProducer_DeltaR", "F")
        self.out.branch("ZMuTauProducer_ABCD", "I")
        if self.isMC__:
           self.out.branch("ZMuTauProducer_TauSFjet", "F")
           self.out.branch("ZMuTauProducer_TauSFele", "F")
           self.out.branch("ZMuTauProducer_TauSFmuo", "F")
           self.out.branch("ZMuTauProducer_TauESjet", "F")
           self.out.branch("ZMuTauProducer_TauESele", "F")
           self.out.branch("ZMuTauProducer_MuonSFId", "F")
           self.out.branch("ZMuTauProducer_MuonSFIso", "F")
           self.out.branch("ZMuTauProducer_MuonSFTrigger", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        #print "ZMuTauProducer"
 
        taus = Collection(event, "Tau")
        muons = Collection(event, "Muon")

        havePair = False
        Mass = Pt = Eta = Phi = 0
        MuonIdx = TauIdx = -1
        DeltaR = 0
        ABCD = 0
        mt = 0
        if self.isMC__:
           TauSFjet = TauSFele = TauSFmuo = 0
           TauESjet = TauESele = 0
           MuonSFId = MuonSFIso = 0
           MuonSFTrigger = 0

        for i, muon in enumerate(muons):
           if muon.pt>=30. and abs(muon.eta)<2.1 and muon.tightId:
              for j, tau in enumerate(taus):
                 tauID = (128&tau.idDeepTau2017v2p1VSjet) and (128&tau.idDeepTau2017v2p1VSe) and (8&tau.idDeepTau2017v2p1VSmu)
                 if tau.pt>=20. and abs(tau.eta)<2.3 and tauID:
                    if deltaR(muon.eta, muon.phi, tau.eta, tau.phi)>=0.4:
                       havePair = True
                       DeltaR = deltaR(muon.eta, muon.phi, tau.eta, tau.phi)
                       MuonIdx = i
                       TauIdx = j
                       mt = 2. * event.MET_pt * muon.pt * (1-math.cos(event.MET_phi-muon.phi))
                       mt = math.sqrt(mt)
                       recoZ = muon.p4()+tau.p4()
                       Mass = recoZ.M()
                       Pt = recoZ.Pt()
                       Eta = recoZ.Eta()
                       Phi = recoZ.Phi()
                       q1q2 = muon.charge * tau.charge
                       iso = muon.pfIsoId>=4
                       if q1q2<0 and iso:     ABCD = 1
                       if q1q2>0 and iso:     ABCD = 2
                       if q1q2<0 and not iso: ABCD = 3
                       if q1q2>0 and not iso: ABCD = 4
                       if self.isMC__:
                          TauSFjet = tauSFTool_jet.getSFvsPT(tau.pt, tau.genPartFlav)
                          TauSFele = tauSFTool_ele.getSFvsEta(tau.eta, tau.genPartFlav)
                          TauSFmuo = tauSFTool_muo.getSFvsEta(tau.eta, tau.genPartFlav)
                          TauESjet = testool_jet.getTES(tau.pt, tau.genPartFlav)
                          TauESele = testool_ele.getFES(tau.pt, tau.genPartFlav)
                          MuonSFId = muonSFTool.getSF_TightID(muon.pt, muon.eta)
                          MuonSFIso = muonSFTool.getSF_ISO_TightID(muon.pt, muon.eta, muon.pfIsoId)
                          MuonSFTrigger = muonSFTool.getSF_Trigger(muon.pt, muon.eta)


        self.out.fillBranch("ZMuTauProducer_havePair", havePair)
        self.out.fillBranch("ZMuTauProducer_Mass", Mass)
        self.out.fillBranch("ZMuTauProducer_Pt", Pt)
        self.out.fillBranch("ZMuTauProducer_Eta", Eta)
        self.out.fillBranch("ZMuTauProducer_Phi", Phi)
        self.out.fillBranch("ZMuTauProducer_DeltaR", DeltaR)
        self.out.fillBranch("ZMuTauProducer_MuonIdx", MuonIdx)
        self.out.fillBranch("ZMuTauProducer_TauIdx", TauIdx)
        self.out.fillBranch("ZMuTauProducer_ABCD", ABCD)
        self.out.fillBranch("ZMuTauProducer_mt", mt)
        if self.isMC__:
           self.out.fillBranch("ZMuTauProducer_TauSFjet", TauSFjet)
           self.out.fillBranch("ZMuTauProducer_TauSFele", TauSFele)
           self.out.fillBranch("ZMuTauProducer_TauSFmuo", TauSFmuo)
           self.out.fillBranch("ZMuTauProducer_TauESjet", TauESjet)
           self.out.fillBranch("ZMuTauProducer_TauESele", TauESele)
           self.out.fillBranch("ZMuTauProducer_MuonSFId", MuonSFId)
           self.out.fillBranch("ZMuTauProducer_MuonSFIso", MuonSFIso)
           self.out.fillBranch("ZMuTauProducer_MuonSFTrigger", MuonSFTrigger)
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

ZMuTauProducerConstr = lambda isMC : ZMuTauProducer(
    isMC_ = isMC
)

