import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import deltaR
import math
import numpy

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
        self.out.branch("TauTau_qq", "I")
        self.out.branch("TauTau_Tau0Idx", "I")
        self.out.branch("TauTau_Tau1Idx", "I")
        self.out.branch("TauTau_mT", "F")
        self.out.branch("TauTau_Mass", "F")
        self.out.branch("TauTau_Pt", "F")
        self.out.branch("TauTau_TauTauDR", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
   
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        #print("beginning TauTauProducer, event, run: %d , %d " % (event.event, event.run))

        HavePair = 0
        qq = 0
        Tau0Idx = -1
        Tau1Idx = -1
        mT0 = mT1 = 0
        Mass = 0
        Pt = 0
        TauTauDR = 0
        HaveTriplet = 0
 
        #https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc102X_doc.html
        taus = Collection(event, "Tau")
 
        #https://twiki.cern.ch/CMS/TauIDRecommendationForRun2
        goodTauIdx = []
        for i, tau in enumerate(taus):
            tauID = (1&tau.idDeepTau2017v2p1VSjet) and (8&tau.idDeepTau2017v2p1VSmu) and (4&tau.idDeepTau2017v2p1VSe) and not (tau.decayMode==5 or tau.decayMode==6 or tau.decayMode==7)
            if tau.pt>=40. and abs(tau.eta)<2.1 and tauID:
                pair = [i, tau.idDeepTau2017v2p1VSjet]
                goodTauIdx.append(pair)
                #print("   tau found: (%d, %f)" % (tau.idDeepTau2017v2p1VSjet, tau.pt))
        if len(goodTauIdx)<2:
            for i, tau in enumerate(taus):
                tauID = (1&tau.idDeepTau2017v2p1VSjet) and (8&tau.idDeepTau2017v2p1VSmu) and (4&tau.idDeepTau2017v2p1VSe) and not (tau.decayMode==5 or tau.decayMode==6 or tau.decayMode==7)
                if tau.pt>=20. and abs(tau.eta)<2.3 and tauID:
                    pair = [i, tau.idDeepTau2017v2p1VSjet]
                    goodTauIdx.append(pair)
                    #print("   tau found: (%d, %f)" % (tau.idDeepTau2017v2p1VSjet, tau.pt))

        # sort in order of decreasing isolation
        goodTauIdx = sorted(goodTauIdx, key=lambda i: (-i[1], i[0]))

        miniso = 0
        maxphotonpt = 0
        for i, ii in enumerate(goodTauIdx):
            for j, jj in enumerate(goodTauIdx):
                if i>j:
                    tau0 = taus[ii[0]]
                    tau1 = taus[jj[0]]
                    #print("tau0 pt, eta, phi: %f, %f, %f" % (tau0.pt, tau0.eta, tau0.phi))
                    #print("tau1 pt, eta, phi: %f, %f, %f" % (tau1.pt, tau1.eta, tau1.phi))
                    if deltaR(tau0, tau1)>=0.4:
                        HavePair = HavePair + 1
                        tempminiso = min(tau0.idDeepTau2017v2p1VSjet, tau1.idDeepTau2017v2p1VSjet)
                        if tempminiso > miniso: #we want to choose the pair with the maximum minimum
                            miniso = tempminiso
                            TauTauDR = deltaR(tau0, tau1)
                            qq = tau0.charge*tau1.charge
                            Tau0Idx = ii[0]
                            Tau1Idx = jj[0]
                            Mass = (tau0.p4()+tau1.p4()).M()
                            Pt =   (tau0.p4()+tau1.p4()).Pt()

        #if HavePair:
        #    tau0 = taus[Tau0Idx]
        #    tau1 = taus[Tau1Idx]
        #    print ("         selected pair: (%d, %f), (%d, %f)" % (tau0.idDeepTau2017v2p1VSjet, tau0.pt, tau1.idDeepTau2017v2p1VSjet, tau1.pt))
        #    if HavePair>1: print("            !!!multiple pairs!!!")

        self.out.fillBranch("TauTau_HavePair", HavePair)
        self.out.fillBranch("TauTau_qq", qq)
        self.out.fillBranch("TauTau_Tau0Idx", Tau0Idx)
        self.out.fillBranch("TauTau_Tau1Idx", Tau1Idx)
        self.out.fillBranch("TauTau_Mass", Mass)
        self.out.fillBranch("TauTau_Pt", Pt)
        return True, Tau0Idx, Tau1Idx

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

TauTauProducerConstr = lambda : TauTauProducer(
)

