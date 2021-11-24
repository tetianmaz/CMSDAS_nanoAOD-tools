import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import deltaPhi, deltaR
from ROOT import TLorentzVector
#from ROOT import TVector3
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
        self.out.branch("ETau_qq", "I")
        self.out.branch("ETau_EIdx", "I")
        self.out.branch("ETau_TauIdx", "I")
        self.out.branch("ETau_mT", "F")
        self.out.branch("ETau_Mass", "F")
        self.out.branch("ETau_Pt", "F")
        self.out.branch("ETau_ETauDR", "F")
        self.out.branch("ETau_ETauDPhi", "F")
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        #print("beginning ETauProducer, event, run: %d , %d " % (event.event, event.run))

        HavePair = 0
        qq = 0
        EIdx = -1
        TauIdx = -1
        mT = 0
        Mass = 0
        Pt = 0
        ETauDR = 0
        ETauDPhi = 0

        #https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc102X_doc.html
        electrons = Collection(event, "Electron")
        taus = Collection(event, "Tau")

        #https://twiki.cern.ch/CMS/EgammaIDRecipesRun2 
        goodEIdx = []
        for i, e in enumerate(electrons):
            eID = 1>0
            if e.pt>=12. and abs(e.eta)<2.5 and eID:
                goodEIdx.append(i)

        #https://twiki.cern.ch/CMS/TauIDRecommendationForRun2
        goodTauIdx = []
        for i, tau in enumerate(taus):
            tauID = (1&tau.idDeepTau2017v2p1VSjet) and (8&tau.idDeepTau2017v2p1VSmu) and (32&tau.idDeepTau2017v2p1VSe) and not (tau.decayMode==5 or tau.decayMode==6 or tau.decayMode==7)
            if tau.pt>=20. and abs(tau.eta)<2.3 and tauID:
                goodTauIdx.append(i)
        if len(goodTauIdx)==0:
            for i, tau in enumerate(taus):
                tauID = (1&tau.idDeepTau2017v2p1VSjet) and (8&tau.idDeepTau2017v2p1VSmu) and (32&tau.idDeepTau2017v2p1VSe)
                if tau.pt>=20. and abs(tau.eta)<2.3 and tauID:
                    goodTauIdx.append(i)

        maxtauiso = 0
        maxeid = -1
        for i, e in enumerate(electrons):
            if i in goodEIdx:
                for j, tau in enumerate(taus):
                    if j in goodTauIdx:
                         if deltaR(e, tau)>=0.4:
                             HavePair = HavePair + 1
                             if e.mvaFall17V2Iso>=maxeid and tau.idDeepTau2017v2p1VSjet>=maxtauiso:
                                 EIdx = i
                                 TauIdx = j
                                 maxtauiso = tau.idDeepTau2017v2p1VSjet
                                 maxeid = e.mvaFall17V2Iso
                                 ETauDR = deltaR(e, tau)
                                 ETauDPhi = abs(deltaPhi(e, tau))
                                 qq = e.charge*tau.charge
                                 Mass = (e.p4()+tau.p4()).M()
                                 Pt = (e.p4()+tau.p4()).Pt()
                                 mT = 2. * event.MET_pt * e.pt * (1.-math.cos(deltaPhi(event.MET_phi, e.phi)))
                                 mT = math.sqrt(mT)

        self.out.fillBranch("ETau_HavePair", HavePair)
        self.out.fillBranch("ETau_qq", qq)
        self.out.fillBranch("ETau_EIdx", EIdx)
        self.out.fillBranch("ETau_TauIdx", TauIdx)
        self.out.fillBranch("ETau_mT", mT)
        self.out.fillBranch("ETau_Mass", Mass)
        self.out.fillBranch("ETau_Pt", Pt)
        self.out.fillBranch("ETau_ETauDR", ETauDR)
        self.out.fillBranch("ETau_ETauDPhi", ETauDPhi)

        return True, EIdx, TauIdx

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

ETauProducerConstr = lambda : ETauProducer(
)

