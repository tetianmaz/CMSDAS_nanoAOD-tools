import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import deltaPhi, deltaR
import math

class MuTauProducer(Module):
    def __init__(self):
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("MuTau_HavePair", "I")
        self.out.branch("MuTau_qq", "I")
        self.out.branch("MuTau_MuIdx", "I")
        self.out.branch("MuTau_TauIdx", "I")
        self.out.branch("MuTau_mT", "F")
        self.out.branch("MuTau_Mass", "F")
        self.out.branch("MuTau_Pt", "F")
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        #print("beginning MuTauProducer, event, run: %d , %d " % (event.event, event.run))

        HavePair = 0
        qq = 0
        MuIdx = -1
        TauIdx = -1
        mT = 0
        Mass = 0
        Pt = 0

        #https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc102X_doc.html
        muons = Collection(event, "Muon")
        taus = Collection(event, "Tau")

        #https://twiki.cern.ch/CMS/SWGuideMuonIdRun2 
        goodMuonIdx = []
        for i, mu in enumerate(muons):
            muonID = mu.tightId
            if mu.pt>=8. and abs(mu.eta)<2.4 and muonID:
                goodMuonIdx.append(i)
        if len(goodMuonIdx)==0:
            for i, mu in enumerate(muons):
                muonID = mu.mediumId
                if mu.pt>=8. and abs(mu.eta)<2.4 and muonID:
                    goodMuonIdx.append(i)

        #https://twiki.cern.ch/CMS/TauIDRecommendationForRun2
        goodTauIdx = []
        for i, tau in enumerate(taus):
            tauID = (1&tau.idDeepTau2017v2p1VSjet) and (8&tau.idDeepTau2017v2p1VSmu) and (4&tau.idDeepTau2017v2p1VSe) and not (tau.decayMode==5 or tau.decayMode==6 or tau.decayMode==7)
            if tau.pt>=20. and abs(tau.eta)<2.3 and tauID:
                goodTauIdx.append(i)
        if len(goodTauIdx)==0:
            for i, tau in enumerate(taus):
                tauID = (1&tau.idDeepTau2017v2p1VSjet) and (8&tau.idDeepTau2017v2p1VSmu) and (4&tau.idDeepTau2017v2p1VSe)
                if tau.pt>=20. and abs(tau.eta)<2.3 and tauID:
                    goodTauIdx.append(i)

        maxtauiso = 0
        maxmuiso = 0
        maxphotonpt = 0
        for i, mu in enumerate(muons):
            if i in goodMuonIdx:
                for j, tau in enumerate(taus):
                    if j in goodTauIdx:
                        if deltaR(mu, tau)>=0.4:
                             HavePair = HavePair + 1
                             if (mu.pfIsoId>=maxmuiso) and (tau.idDeepTau2017v2p1VSjet>=maxtauiso):
                                 MuIdx = i
                                 TauIdx = j
                                 maxtauiso = tau.idDeepTau2017v2p1VSjet
                                 maxmuiso = mu.pfIsoId
                                 qq = mu.charge*tau.charge
                                 Mass = (mu.p4()+tau.p4()).M()
                                 Pt =  (mu.p4()+tau.p4()).Pt()
                                 mT = 2. * event.MET_pt * mu.pt * (1.-math.cos(deltaPhi(event.MET_phi, mu.phi)))
                                 mT = math.sqrt(mT)

        #if HavePair==0: return False
        self.out.fillBranch("MuTau_HavePair", HavePair)
        self.out.fillBranch("MuTau_qq", qq)
        self.out.fillBranch("MuTau_MuIdx", MuIdx)
        self.out.fillBranch("MuTau_TauIdx", TauIdx)
        self.out.fillBranch("MuTau_Mass", Mass)
        self.out.fillBranch("MuTau_Pt", Pt)
        self.out.fillBranch("MuTau_mT", mT)

        return True, MuIdx, TauIdx

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

MuTauProducerConstr = lambda : MuTauProducer(
)

