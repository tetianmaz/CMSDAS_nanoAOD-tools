import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from PhysicsTools.NanoAODTools.postprocessing.tools import deltaR

from TauPOG.TauIDSFs.TauIDSFTool import TauIDSFTool
tauSFTool_jet = TauIDSFTool('2018ReReco','DeepTau2017v2p1VSjet','VVTight')
tauSFTool_ele = TauIDSFTool('2018ReReco','DeepTau2017v2p1VSe','VVTight')
tauSFTool_muo = TauIDSFTool('2018ReReco','DeepTau2017v2p1VSmu','Tight')
from TauPOG.TauIDSFs.TauIDSFTool import TauESTool
testool_jet = TauESTool('2018ReReco','DeepTau2017v2p1VSjet')
from TauPOG.TauIDSFs.TauIDSFTool import TauFESTool
testool_ele = TauFESTool('2018ReReco','DeepTau2017v2p1VSe')

class ZProducer(Module):
    def __init__(self, isMC_, electronSelection, muonSelection, muonSelectionLoose, tauSelection, jetSelection, photonSelection):
        #self.xsWeight__ = xsWeight_
        self.isMC__ = isMC_
        self.electronSel = electronSelection
        self.muonSel = muonSelection
        self.muonSelLoose = muonSelectionLoose
        self.tauSel = tauSelection
        self.jetSel = jetSelection
        self.photonSel = photonSelection
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("ZProducer_nElectron",  "I")
        self.out.branch("ZProducer_nMuon",  "I")
        self.out.branch("ZProducer_nMuonLoose", "I")
        self.out.branch("ZProducer_nTau",  "I")
        self.out.branch("ZProducer_nJet", "I")
        self.out.branch("ZProducer_nPhoton", "I")
        self.out.branch("ZProducer_MuTauMass",  "F")
        self.out.branch("ZProducer_ABCDregion", "I")
        self.out.branch("ZProducer_mt", "F")
        self.out.branch("ZProducer_BTags", "I")
        self.out.branch("ZProducer_hasDiMuon", "O")
        self.out.branch("ZProducer_muonPt", "F")
        self.out.branch("ZProducer_muonEta", "F")
        self.out.branch("ZProducer_tauPt", "F")
        self.out.branch("ZProducer_tauEta", "F")
        self.out.branch("ZProducer_deltaRMuTau", "F")
        if self.isMC__:
           self.out.branch("ZProducer_Muon_genPartFlav", "I")
           self.out.branch("ZProducer_Tau_genPartFlav", "I")
           self.out.branch("ZProducer_tauSFjet", "F")
           self.out.branch("ZProducer_tauSFjetup", "F")
           self.out.branch("ZProducer_tauSFjetdown", "F")
           self.out.branch("ZProducer_tauSFele", "F")
           self.out.branch("ZProducer_tauSFeleup", "F")
           self.out.branch("ZProducer_tauSFeledown", "F")
           self.out.branch("ZProducer_tauSFmuo", "F")
           self.out.branch("ZProducer_tauSFmuoup", "F")
           self.out.branch("ZProducer_tauSFmuodown", "F")
           self.out.branch("ZProducer_tauESjet", "F")
           self.out.branch("ZProducer_tauESjetup", "F")
           self.out.branch("ZProducer_tauESjetdown", "F")
           self.out.branch("ZProducer_tauESele", "F")
           self.out.branch("ZProducer_tauESeleup", "F")
           self.out.branch("ZProducer_tauESeledown", "F")
           #self.out.branch("ZProducer_xsWeight", "F")
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
 
        electrons = Collection(event, "Electron")
        electrons_clean = filter(self.electronSel, electrons)
        nElectron_ = len(electrons_clean)

        muons = Collection(event, "Muon")
        muons_clean = filter(self.muonSel, muons)
        nMuon_ = len(muons_clean)

        photons = Collection(event, "Photon")
        photons_clean = filter(self.photonSel, photons)
        nPhoton_ = len(photons_clean)

        muons_clean_loose = filter(self.muonSelLoose, muons)
        nMuonLoose_ = len(muons_clean_loose)
        hasDiMuon = False
        for i in muons_clean_loose:
           for j in muons_clean_loose:
              if i.charge*j.charge < 0:
                 hasDiMuon = True

        taus = Collection(event, "Tau")
        taus_clean = filter(self.tauSel, taus)
        nTau_ = len(taus_clean)

        muon_idx = -1
        tau_idx = -1
        for i in muons:
           if i.pt>=30. and abs(i.eta)<2.1 and i.tightMuon:
              for j in taus:
                 if j.pt>=20. and abs(j.eta)<2.3:
                    if deltaR(i.eta, i.phi, j.eta, j.phi)>=0.4:

 

        jets = Collection(event, "Jet")
        jets_clean = filter(self.jetSel, jets)
        nJet_ = len(jets_clean)

        BTags = 0
        for i in jets_clean:
           if i.btagDeepB>0.7527:
              BTags = BTags+1
         
        ABCDregion = 0
        MuTauMass = -1.
        mt = -1
        muonPt = muonEta = -1.
        tauPt = tauEta = -1.
        Muon_genPartFlav_ = Tau_genPartFlav_ = -1
        tauSFjetdown = tauSFjet = tauSFjetup = 0.
        tauSFeledown = tauSFele = tauSFeleup = 0.
        tauSFmuodown = tauSFmuo = tauSFmuoup = 0.
        tauESjetdown = tauESjet = tauESjetup = 0.
        tauESeledown = tauESele = tauESeleup = 0
        ZProducer_deltaRMuTau = 9
        if nMuon_>0:
          mt = 2 * event.MET_pt * muons_clean[0].pt * (1-math.cos(event.MET_phi-muons_clean[0].phi))
          mt = math.sqrt(mt)
          iso = muons_clean[0].pfIsoId>=4
          muonPt = muons_clean[0].pt
          muonEta = muons_clean[0].eta
          if self.isMC__:
             Muon_genPartFlav_ = muons_clean[0].genPartFlav
          if iso: ABCDregion = -1
          if not iso: ABCDregion = -2
          if nTau_>0:
             recoZ = muons_clean[0].p4()+taus_clean[0].p4()
             MuTauMass = recoZ.M()
             q1q2 = muons_clean[0].charge*taus_clean[0].charge
             tauPt = taus_clean[0].pt
             tauEta = taus_clean[0].eta
             ZProducer_deltaRMuTau = deltaR(tauEta, taus_clean[0].phi, muonEta, muons_clean[0].phi)
             if q1q2==0: print "warning: q1q2==0"
             if q1q2<0 and iso: ABCDregion = 1
             if q1q2>0 and iso: ABCDregion = 2
             if q1q2<0 and not iso: ABCDregion = 3
             if q1q2>0 and not iso: ABCDregion = 4
             if self.isMC__:
                Tau_genPartFlav_ = taus_clean[0].genPartFlav
                tauSFjetdown, tauSFjet, tauSFjetup = tauSFTool_jet.getSFvsPT(tauPt, Tau_genPartFlav_, unc='All')
                tauSFeledown, tauSFele, tauSFeleup = tauSFTool_ele.getSFvsEta(tauEta, Tau_genPartFlav_, unc='All')
                tauSFmuodown, tauSFmuo, tauSFmuoup = tauSFTool_muo.getSFvsEta(tauEta, Tau_genPartFlav_, unc='All')
                tauESjetdown, tauESjet, tauESjetup =  testool_jet.getTES(tauPt, Tau_genPartFlav_, unc='All')
                tauESeledown, tauESele, tauESeleup =  testool_ele.getFES(tauPt, Tau_genPartFlav_, unc='All')

        self.out.fillBranch("ZProducer_nElectron", nElectron_)
        self.out.fillBranch("ZProducer_nMuon", nMuon_)
        self.out.fillBranch("ZProducer_nMuonLoose", nMuonLoose_)
        self.out.fillBranch("ZProducer_nPhoton", nPhoton_)
        self.out.fillBranch("ZProducer_nTau", nTau_)
        self.out.fillBranch("ZProducer_MuTauMass", MuTauMass)
        self.out.fillBranch("ZProducer_ABCDregion", ABCDregion)
        self.out.fillBranch("ZProducer_mt", mt)
        self.out.fillBranch("ZProducer_BTags", BTags)
        self.out.fillBranch("ZProducer_nJet", nJet_)
        self.out.fillBranch("ZProducer_hasDiMuon", hasDiMuon)
        self.out.fillBranch("ZProducer_muonPt", muonPt)
        self.out.fillBranch("ZProducer_muonEta", muonEta)         
        self.out.fillBranch("ZProducer_tauPt", tauPt)
        self.out.fillBranch("ZProducer_tauEta", tauEta)
        self.out.fillBranch("ZProducer_deltaRMuTau", ZProducer_deltaRMuTau)
        if self.isMC__:
           self.out.fillBranch("ZProducer_Muon_genPartFlav", Muon_genPartFlav_)
           self.out.fillBranch("ZProducer_Tau_genPartFlav", Tau_genPartFlav_)
           self.out.fillBranch("ZProducer_tauSFjet", tauSFjet)
           self.out.fillBranch("ZProducer_tauSFjetup", tauSFjetup)
           self.out.fillBranch("ZProducer_tauSFjetdown", tauSFjetdown)
           self.out.fillBranch("ZProducer_tauSFele", tauSFele)
           self.out.fillBranch("ZProducer_tauSFeleup", tauSFeleup)
           self.out.fillBranch("ZProducer_tauSFeledown", tauSFeledown)
           self.out.fillBranch("ZProducer_tauSFmuo", tauSFmuo)
           self.out.fillBranch("ZProducer_tauSFmuoup", tauSFmuoup)
           self.out.fillBranch("ZProducer_tauSFmuodown", tauSFmuodown)
           self.out.fillBranch("ZProducer_tauESjet", tauESjet)
           self.out.fillBranch("ZProducer_tauESjetup", tauESjetup)
           self.out.fillBranch("ZProducer_tauESjetdown", tauESjetdown)
           self.out.fillBranch("ZProducer_tauESele", tauESele)
           self.out.fillBranch("ZProducer_tauESeleup", tauESeleup)
           self.out.fillBranch("ZProducer_tauESeledown", tauESeledown)
           #self.out.fillBranch("ZProducer_xsWeight", self.xsWeight__)
        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

ZProducerConstr = lambda isMC : ZProducer(
   #xsWeight_ = xsWeight,
   isMC_ = isMC,
   electronSelection = lambda j: j.pt>40 and abs(j.eta)<2.5 and j.mvaFall17V2Iso_WP80,
   muonSelection = lambda j: j.pt>30 and abs(j.eta)<2.1 and j.tightId,
   muonSelectionLoose = lambda j: j.pt>25 and abs(j.eta)<2.4 and j.mediumId and j.pfIsoId>=3,
   tauSelection = lambda j: j.pt>20 and abs(j.eta)<2.3 and (128&j.idDeepTau2017v2p1VSjet) and (128&j.idDeepTau2017v2p1VSe) and (8&j.idDeepTau2017v2p1VSmu),
   jetSelection = lambda j: j.pt>20 and abs(j.eta)<2.5 and (4&j.jetId),
   photonSelection = lambda j: j.pt>45 and abs(j.eta)<2.5 and j.mvaID_WP90 and (j.electronVeto or not j.pixelSeed)
)

