//https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc102X_doc.html
#include <TCut.h>
#include <TFile.h>
#include <TTree.h>
#include <TCanvas.h>
#include <TGraphErrors.h>
#include <TAxis.h>
#include <iostream>

void roc()
{
   const TString tag = "WJetsToLNu";
   const TString infile = "root://cmseos.fnal.gov//store/user/cmsdas/2022/short_exercises/Tau/WJetsToLNu__AE18A33F-9CF5-BC4E-A1E9-46F7BF382AF1.root";
   //const TString infile = "root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18NanoAODv9/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/AE18A33F-9CF5-BC4E-A1E9-46F7BF382AF1.root";

   //const TString tag = "DYJetsToLL";
   //const TString infile = "root://cmseos.fnal.gov//store/user/cmsdas/2022/short_exercises/Tau/DYJetsToLL__7B7D90CB-14EF-B749-B4D7-7C413FE3CCC1.root";
   //const TString infile = "root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18NanoAODv9/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/7B7D90CB-14EF-B749-B4D7-7C413FE3CCC1.root";

   //const TString tag = "TTTo2L2Nu";
   //const TString infile = "root://cmseos.fnal.gov//store/user/cmsdas/2022/short_exercises/Tau/TTTo2L2Nu__1656732C-0CD4-F54B-B39D-19CA08E18A77.root";
   //const TString infile = "root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18NanoAODv9/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/1656732C-0CD4-F54B-B39D-19CA08E18A77.root";

   const TString fname_sig = infile;
   TFile * f_sig = TFile::Open(fname_sig);
   TTree * t_sig = (TTree*)f_sig->Get("Events");

   const TString fname_bkg = infile;
   TFile * f_bkg = TFile::Open(fname_bkg);
   TTree * t_bkg = (TTree*)f_bkg->Get("Events");

   TCut taucut = "Tau_pt>=20. && TMath::Abs(Tau_eta)<2.3 && !(Tau_decayMode==5||Tau_decayMode==6||Tau_decayMode==7)";
   taucut = taucut && TCut("(8&Tau_idDeepTau2017v2p1VSjet) && (2&Tau_idDeepTau2017v2p1VSmu)");
   const TCut sigcut = "Tau_genPartFlav==5";
   const TCut bkgcut = "Tau_genPartFlav==1";

   TCut wpcut[8];
   for (int i = 0; i < 8; ++i) {
      char buffer[100];
      const int mask = 1<<i;
      sprintf(buffer, "%i&Tau_idDeepTau2017v2p1VSe", mask);
      std::cout << buffer << std::endl;
      wpcut[i] = TCut(buffer);
   }

   const double n_sig_tot = t_sig->GetEntries(taucut && sigcut);
   const double n_bkg_tot = t_bkg->GetEntries(taucut && bkgcut);
   double n_sig[8], n_bkg[8];
   for (int i = 0; i < 8; ++i) {
      n_sig[i] = t_sig->GetEntries(taucut && sigcut && wpcut[i]);
      n_bkg[i] = t_bkg->GetEntries(taucut && bkgcut && wpcut[i]);
   }

   TGraphErrors * g = new TGraphErrors(8);
   g->SetTitle(";Tau ID efficiency;Electron mis-id probability");
   g->SetMarkerStyle(20);
   for (int i = 0; i < 8; ++i) {
      const double eff_sig = n_sig[i]/n_sig_tot;
      const double eff_sig_err = eff_sig * sqrt((1./n_sig[i])+(1./n_sig_tot));
      const double eff_bkg = n_bkg[i]/n_bkg_tot;
      const double eff_bkg_err = eff_bkg * sqrt((1./n_bkg[i])+(1./n_bkg_tot));
      g->SetPoint(i, eff_sig, eff_bkg);
      g->SetPointError(i, eff_sig_err, eff_bkg_err); 
   }

   std::cout << "inclusive efficiencies (sig, bkg)" << std::endl;
   for (int i = 0; i < 8; ++i) {
      double x, y;
      g->GetPoint(i, x, y);
      std::cout << x << ", " << y << std::endl;
   }

   TCanvas * c = new TCanvas("c", "c", 400, 400);
   g->Draw("APE");
   g->SetMinimum(0.00001);
   g->SetMaximum(1.);
   c->SetLogy();
   TAxis * a = g->GetXaxis();
   a->SetLimits(0.5, 1.);
   c->SaveAs("./plots/roc.pdf");
}

