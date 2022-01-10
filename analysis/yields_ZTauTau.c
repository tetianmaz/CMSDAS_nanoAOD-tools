#include <iostream>
#include <THStack.h>
#include <TCut.h>
#include <TH1D.h>
#include <TFile.h>
#include <TTree.h>
#include <TChain.h>
#include <TCanvas.h>
#include <TLegend.h>

/*double addOverflow(TH1D * h)
{
   const int n = h->GetNbinsX();
   const double o = h->GetBinContent(n+1);
   if (!o) return 0;

   std::cout << "Adding overflow to " << h->GetName() << std::endl;
   const int nbefore = h->GetEntries();
   std::cout << "   there are " << nbefore << " entries in the histogram." << std::endl;

   const double oerr = h->GetBinError(n+1);
   std::cout << "   content of the overflow bin: " << o << " +- " << oerr << std::endl;
   std::cout << "   content of the last bin: " << h->GetBinContent(n) << " +- " << h->GetBinError(n) << std::endl;
   h->AddBinContent(n, o);
   h->SetBinContent(n+1, 0.);
   h->SetBinError(n+1, 0.);
   std::cout << "   new content of the overflow bin: " << h->GetBinContent(n+1) << " +- " << h->GetBinError(n+1) << std::endl;
   std::cout << "   new content of the last bin: " << h->GetBinContent(n) << " +- " << h->GetBinError(n) << std::endl;

   const int nafter = h->GetEntries();
   std::cout << "   there are " << nafter << " entries in the modified histogram." << std::endl;
   return o;
}*/

TFile * makeHists(const TString tag, const double weight=0.)
{
   std::cout << "makeHists(): " << tag << ", " << weight << std::endl;

   TChain * t_events = new TChain("Events");
   TChain * t = new TChain("Friends");
   const TString frienddir = "root://cmseos.fnal.gov//store/user/fojensen/TauTauLongExercise_8151201/";
   if (tag=="SingleMuon") {
      t->Add(frienddir+"SingleMuon_2018A_Friend.root");
      t->Add(frienddir+"SingleMuon_2018B_Friend.root");
      t->Add(frienddir+"SingleMuon_2018C_Friend.root");
      t->Add(frienddir+"SingleMuon_2018D_0_Friend.root");
      t->Add(frienddir+"SingleMuon_2018D_1_Friend.root");
      t_events->Add("root://cmseos.fnal.gov//store/user/fojensen/cmsdas_05012022/SingleMuon_2018A.root");
      t_events->Add("root://cmseos.fnal.gov//store/user/fojensen/cmsdas_05012022/SingleMuon_2018B.root");
      t_events->Add("root://cmseos.fnal.gov//store/user/fojensen/cmsdas_05012022/SingleMuon_2018C.root");
      t_events->Add("root://cmseos.fnal.gov//store/user/fojensen/cmsdas_05012022/SingleMuon_2018D_0.root");
      t_events->Add("root://cmseos.fnal.gov//store/user/fojensen/cmsdas_05012022/SingleMuon_2018D_1.root");
   }
   if (tag=="WJetsToLNu") {
      t->Add(frienddir+"WJetsToLNu_Friend.root");
      t_events->Add("root://cmseos.fnal.gov//store/user/fojensen/cmsdas_05012022/WJetsToLNu.root");
   }
   if (tag=="TTTo2L2Nu") {
      t->Add(frienddir+"TTTo2L2Nu_Friend.root");
      t_events->Add("root://cmseos.fnal.gov//store/user/fojensen/cmsdas_05012022/TTTo2L2Nu.root");
   }
   if (tag=="TTToSemiLeptonic") {
      t->Add(frienddir+"TTToSemiLeptonic_0_Friend.root");
      t->Add(frienddir+"TTToSemiLeptonic_1_Friend.root");
      t->Add(frienddir+"TTToSemiLeptonic_2_Friend.root");
      t_events->Add("root://cmseos.fnal.gov//store/user/fojensen/cmsdas_05012022/TTToSemiLeptonic_0.root");
      t_events->Add("root://cmseos.fnal.gov//store/user/fojensen/cmsdas_05012022/TTToSemiLeptonic_1.root");
      t_events->Add("root://cmseos.fnal.gov//store/user/fojensen/cmsdas_05012022/TTToSemiLeptonic_2.root");
   }
   if (tag=="DYJetsToEEMuMu_M50") {
      t->Add(frienddir+"DYJetsToEEMuMu_M50_Friend.root");
      t_events->Add("root://cmseos.fnal.gov//store/user/fojensen/cmsdas_05012022/DYJetsToEEMuMu_M50.root");
   }
   if (tag=="DYJetsToTauTau_M50") {
      t->Add(frienddir+"DYJetsToTauTau_M50_Friend.root");
      t_events->Add("root://cmseos.fnal.gov//store/user/fojensen/cmsdas_05012022/DYJetsToTauTau_M50.root");
   }
   std::cout << "# of entries in t: " << t->GetEntries() << std::endl;
   std::cout << "# of entries in t_events: " << t_events->GetEntries() << std::endl;

   t->AddFriend(t_events);

   TCut baseline = "MuTau_HavePair>0";
   baseline = baseline && TCut("(HLT_IsoMu24||HLT_IsoMu27) && Muon_pt[MuTau_MuIdx]>=26. && Muon_tightId[MuTau_MuIdx] && Muon_pfIsoId[MuTau_MuIdx]>=4");
   baseline = baseline && TCut("EE_HavePair==0 && MuMu_HavePair==0");
   baseline = baseline && TCut("Tau_decayMode[MuTau_TauIdx]!=5 && Tau_decayMode[MuTau_TauIdx]!=6 && Tau_decayMode[MuTau_TauIdx]!=7");
   baseline = baseline && TCut("Sum$(Electron_pt>=12. && TMath::Abs(Electron_eta)<2.5 && Electron_mvaFall17V2Iso_WP90)==0");
   baseline = baseline && TCut("Sum$(Muon_pt>=8. && TMath::Abs(Muon_eta)<2.4 && Muon_tightId && Muon_pfIsoId>=4)==1");
   baseline = baseline && TCut("MuTau_mT<40.");
   baseline = baseline && TCut("JetProducer_nBJetL==0");

   const TCut regionA = "MuTau_qq==-1 && (32&Tau_idDeepTau2017v2p1VSjet[MuTau_TauIdx])";
   const TCut regionB = "MuTau_qq==-1 && (8&Tau_idDeepTau2017v2p1VSjet[MuTau_TauIdx]) && !(32&Tau_idDeepTau2017v2p1VSjet[MuTau_TauIdx])";
   const TCut regionC = "MuTau_qq==+1 && (32&Tau_idDeepTau2017v2p1VSjet[MuTau_TauIdx])";
   const TCut regionD = "MuTau_qq==+1 && (8&Tau_idDeepTau2017v2p1VSjet[MuTau_TauIdx]) && !(32&Tau_idDeepTau2017v2p1VSjet[MuTau_TauIdx])";

   char bufferA[1000], bufferB[1000], bufferC[1000], bufferD[1000];
   if (weight) {
      sprintf(bufferA, "%f * (%s)", weight, TString(baseline && regionA).Data());
      sprintf(bufferB, "%f * (%s)", weight, TString(baseline && regionB).Data());
      sprintf(bufferC, "%f * (%s)", weight, TString(baseline && regionC).Data());
      sprintf(bufferD, "%f * (%s)", weight, TString(baseline && regionD).Data());
   } else {
      sprintf(bufferA, "%s", TString(baseline && regionA).Data());
      sprintf(bufferB, "%s", TString(baseline && regionB).Data());
      sprintf(bufferC, "%s", TString(baseline && regionC).Data());
      sprintf(bufferD, "%s", TString(baseline && regionD).Data());
   }

   const TString var = "MuTau_Mass";
   //TH1D * h_A = new TH1D("h_A_"+tag, ";#mu+#tau_{h} visible mass [GeV];events / 10 GeV", 15, 60., 210.);
   TH1D * h_A = new TH1D("h_A_"+tag, ";#mu+#tau_{h} visible mass [GeV];events / 10 GeV", 25, 0., 250.);
   TH1D * h_B = (TH1D*)h_A->Clone("h_B_"+tag);
   TH1D * h_C = (TH1D*)h_A->Clone("h_C_"+tag);
   TH1D * h_D = (TH1D*)h_A->Clone("h_D_"+tag);

   std::cout << "   region | yield | mc events" << std::endl;
   const int n_A = t->Project(h_A->GetName(), var, bufferA);
   const double i_A = h_A->Integral();
   std::cout << "   A " << i_A << " " << n_A << std::endl;

   const int n_B = t->Project(h_B->GetName(), var, bufferB);
   const double i_B = h_B->Integral();
   std::cout << "   B " << i_B << " " << n_B << std::endl;
   
   const int n_C = t->Project(h_C->GetName(), var, bufferC);
   const double i_C = h_C->Integral();
   std::cout << "   C " << i_C << " " << n_C << std::endl;
  
   const int n_D = t->Project(h_D->GetName(), var, bufferD);
   const double i_D = h_D->Integral();
   std::cout << "   D " << i_D << " " << n_D << std::endl;

   TFile * f_out = new TFile("./outputHists/"+tag+".root", "RECREATE");
   h_A->Write("h_A");
   h_B->Write("h_B");
   h_C->Write("h_C");
   h_D->Write("h_D");
   f_out->Close();
   return f_out;
}

TFile * makeQCDHists()
{
   std::cout << "QCD" << std::endl;
   TFile * f_data = TFile::Open("./outputHists/SingleMuon.root");
   //TH1D * data_A = (TH1D*)f_data->Get("h_A"); nonono
   TH1D * data_B = (TH1D*)f_data->Get("h_B");
   TH1D * data_C = (TH1D*)f_data->Get("h_C");
   TH1D * data_D = (TH1D*)f_data->Get("h_D");

   const int nmc = 5;
   TString mctags[nmc];
   mctags[0] = "WJetsToLNu";
   mctags[1] = "TTTo2L2Nu";
   mctags[2] = "TTToSemiLeptonic";
   mctags[3] = "DYJetsToEEMuMu_M50";
   mctags[4] = "DYJetsToTauTau_M50";

   TH1D *h_A[nmc], *h_B[nmc], *h_C[nmc], *h_D[nmc];
   for (int i = 0; i < nmc; ++i) {
      char fname[100];
      sprintf(fname, "./outputHists/%s.root", mctags[i].Data());
      TFile * f = TFile::Open(fname);
      h_A[i] = (TH1D*)f->Get("h_A");
      h_B[i] = (TH1D*)f->Get("h_B");
      h_C[i] = (TH1D*)f->Get("h_C");
      h_D[i] = (TH1D*)f->Get("h_D");
   }

   for (int i = 0; i < nmc; ++i) {
      data_B->Add(h_B[i], -1.);
      data_C->Add(h_C[i], -1.);
      data_D->Add(h_D[i], -1.);
   }

   double B, Berr;
   B = data_B->IntegralAndError(1, data_B->GetNbinsX()+1, Berr);
   double C, Cerr;
   C = data_C->IntegralAndError(1, data_C->GetNbinsX()+1, Cerr);
   double D, Derr;
   D = data_D->IntegralAndError(1, data_D->GetNbinsX()+1, Derr);
   const double CoD = C/D;
   const double CoDerr = CoD * sqrt((Berr/B)*(Berr/B)+(Cerr/C)*(Cerr/C));
   const double BCoD = B * CoD;
   const double errBCoD = BCoD * sqrt((Berr/B)*(Berr/B)+(CoDerr/CoD)*(CoDerr/CoD));
   std::cout << "inclusive transfer factor: " << CoD << " +- " << CoDerr << std::endl;

   TH1D * h_CoD = (TH1D*)data_C->Clone("h_CoD");
   h_CoD->Divide(data_D);

   TH1D * h_QCD = (TH1D*)data_B->Clone("h_QCD");
   //h_QCD->Scale(CoD);
   h_QCD->Multiply(h_CoD);
 
   TCanvas * c = new TCanvas("c_makeQCDHists", "c_makeQCDHists", 400, 400);
   h_CoD->Draw("PE");
   h_CoD->GetYaxis()->SetTitle("C / D");
   h_CoD->SetStats(0);
   h_CoD->SetMinimum(0.);
   //h_CoD->SetMaximum(0.65);
   h_CoD->SetMarkerStyle(20);
   c->SaveAs("./plots/CoD.pdf");
 
   TFile * f_qcd = new TFile("./outputHists/QCD.root", "RECREATE");
   h_QCD->Write("h_A");
   data_B->Write("h_B");
   data_C->Write("h_C");
   data_D->Write("h_D");
   h_CoD->Write("h_CoD");
   f_qcd->Close();
   return f_qcd;
}

void plotControlRegions()
{
   std::cout << "plotControlRegions()" << std::endl;
   const double ymin = 1.e2;
   const double ymax = 1.e6;

   TFile *f_SingleMuon = TFile::Open("./outputHists/SingleMuon.root");
   TH1D * h_SingleMuon_B = (TH1D*)f_SingleMuon->Get("h_B");
   TH1D * h_SingleMuon_C = (TH1D*)f_SingleMuon->Get("h_C");
   TH1D * h_SingleMuon_D = (TH1D*)f_SingleMuon->Get("h_D");
   h_SingleMuon_B->SetMarkerStyle(20);
   h_SingleMuon_C->SetMarkerStyle(20);
   h_SingleMuon_D->SetMarkerStyle(20);

   int nmc = 5;
   double xsweight[nmc];
   const double lumi = 59725.419;
   xsweight[0] = lumi * 61526.7 / 81051269.;
   xsweight[1] = lumi * 87.31 / 145020000.;
   xsweight[2] = lumi * 365.34 / 476408000.;
   xsweight[3] = lumi * 6077.22 / 197649078.;
   xsweight[4] = lumi * 6077.22 / 197649078.;
 
   TString labels[nmc];
   labels[0] = "W#rightarrowl#nu";
   labels[1] = "t#bar{t}#rightarrow2l2#nu";
   labels[2] = "t#bar{t}#rightarrow1l1#nu2q";
   labels[3] = "Z#rightarrowee,#mu#mu";
   labels[4] = "Z#rightarrow#tau#tau";
 
   TString mctags[nmc];
   mctags[0] = "WJetsToLNu";
   mctags[1] = "TTTo2L2Nu";
   mctags[2] = "TTToSemiLeptonic";
   mctags[3] = "DYJetsToEEMuMu_M50";
   mctags[4] = "DYJetsToTauTau_M50";

   int colz[nmc];
   colz[0] = 5;
   colz[1] = 6;
   colz[2] = 7;
   colz[3] = 8;
   colz[4] = 9;

   TH1D *h_mc_B[nmc], *h_mc_C[nmc], *h_mc_D[nmc];
   for (int i = 0; i < nmc; ++i) {
      TFile * f = TFile::Open("./outputHists/"+mctags[i]+".root");
      h_mc_B[i] = (TH1D*)f->Get("h_B");
      h_mc_C[i] = (TH1D*)f->Get("h_C");
      h_mc_D[i] = (TH1D*)f->Get("h_D");
      h_mc_B[i]->SetFillColor(colz[i]);
      h_mc_C[i]->SetFillColor(colz[i]);
      h_mc_D[i]->SetFillColor(colz[i]);
   }

   THStack * s_B = new THStack("s_B", "");
   s_B->SetTitle("B;#mu+#tau_{h} visible mass [GeV];events / 10 GeV");
   for (int i = 0; i < nmc; ++i) s_B->Add(h_mc_B[i]);

   THStack * s_C = new THStack("s_C", "");
   s_C->SetTitle("C;#mu+#tau_{h} visible mass [GeV];events / 10 GeV");
   for (int i = 0; i < nmc; ++i) s_C->Add(h_mc_C[i]);

   THStack * s_D = new THStack("s_D", "");
   s_D->SetTitle("D;#mu+#tau_{h} visible mass [GeV];events / 10 GeV");
   for (int i = 0; i < nmc; ++i) s_D->Add(h_mc_D[i]);

   TLegend * l = new TLegend(0.225, 0.75, 0.875, 0.875);
   l->SetBorderSize(0);
   l->SetNColumns(3);
   for (int i = 0; i < nmc; ++i) l->AddEntry(h_mc_B[i], labels[i], "F");
   l->AddEntry(h_SingleMuon_B, "data", "P");

   TCanvas * c = new TCanvas("c", "c", 800, 800);
   c->Divide(2,2);

   TPad * p2 = (TPad*)c->cd(2);
   s_B->Draw("HIST");
   h_SingleMuon_B->Draw("PE, SAME"); 
   p2->SetLogy();
   s_B->SetMinimum(ymin);
   s_B->SetMaximum(ymax);
   l->Draw();

   TPad * p3 = (TPad*)c->cd(3);
   s_C->Draw("HIST");
   h_SingleMuon_C->Draw("PE, SAME");
   p3->SetLogy();
   s_C->SetMinimum(ymin);
   s_C->SetMaximum(ymax);
   l->Draw();

   TPad * p4 = (TPad*)c->cd(4);
   s_D->Draw("HIST");
   h_SingleMuon_C->Draw("PE, SAME");
   p4->SetLogy();
   s_D->SetMinimum(ymin);
   s_D->SetMaximum(ymax);
   l->Draw();

   c->SaveAs("./plots/cr.pdf");
}

void yields_ZTauTau()
{
   const double ymin = 1.e2;
   const double ymax = 1.e6;

   int nmc = 5;
   double xsweight[nmc];
   const double lumi = 59725.419;
   xsweight[0] = lumi * 61334.9 / 81051269.;
   xsweight[1] = lumi * 87.31 / 145020000.;
   xsweight[2] = lumi * 365.34 / 476408000.;
   xsweight[3] = lumi * 6025.2 / 197649078.;
   xsweight[4] = lumi * 6025.2 / 197649078.;

   TString mctags[nmc];
   mctags[0] = "WJetsToLNu";
   mctags[1] = "TTTo2L2Nu";
   mctags[2] = "TTToSemiLeptonic";
   mctags[3] = "DYJetsToEEMuMu_M50";
   mctags[4] = "DYJetsToTauTau_M50";

   TString labels[nmc];
   labels[0] = "W#rightarrowl#nu";
   labels[1] = "t#bar{t}#rightarrow2l2#nu";
   labels[2] = "t#bar{t}#rightarrow1l1nu2q";
   labels[3] = "Z#rightarrowee,#mu#mu";
   labels[4] = "Z#rightarrow#tau#tau";
   
   int colz[nmc];
   colz[0] = 5;
   colz[1] = 6;
   colz[2] = 7;
   colz[3] = 8;
   colz[4] = 9;

   makeHists("SingleMuon");
   TFile *f_SingleMuon = TFile::Open("./outputHists/SingleMuon.root");
   TH1D * h_SingleMuon = (TH1D*)f_SingleMuon->Get("h_A");
   h_SingleMuon->SetMarkerStyle(20);
   
   for (int i = 0; i < nmc; ++i) makeHists(mctags[i], xsweight[i]);
   double samplesum = 0.;

   TH1D * h[nmc];
   for (int i = 0; i < nmc; ++i) {
      char fname[100];
      sprintf(fname, "./outputHists/%s.root", mctags[i].Data());
      TFile * f = TFile::Open(fname);
      h[i] = (TH1D*)f->Get("h_A");
      h[i]->SetFillColor(colz[i]);
      samplesum += h[i]->Integral();
   }

   makeQCDHists();
   TFile * f_QCD = TFile::Open("./outputHists/QCD.root");
   TH1D * h_QCD = (TH1D*)f_QCD->Get("h_A");
   samplesum += h_QCD->Integral();
   h_QCD->SetFillColor(4);

   for (int i = 0; i < nmc; ++i) {
      std::cout << mctags[i] << std::endl;
      std::cout << "   Integral(): " << h[i]->Integral() << "; fraction of total:" << h[i]->Integral()/samplesum << std::endl;
      std::cout << "   GetEntries(): " << h[i]->GetEntries() << std::endl;
   }
   std::cout << "QCD" << std::endl;
   std::cout << "   Integral(): " << h_QCD->Integral() << "; fraction of total: " << h_QCD->Integral()/samplesum << std::endl;
   std::cout << "   GetEntries(): " << h_QCD->GetEntries() << std::endl;
 
   THStack * s = new THStack("s", "");
   s->SetTitle(h_SingleMuon->GetTitle());
   for (int i = 0; i < nmc; ++i) {
      s->Add(h[i]);
   }
   s->Add(h_QCD);

   TCanvas * c = new TCanvas("c_yieldsZTauTau", "c_yieldsZTauTau", 400, 400);
   h_SingleMuon->SetMinimum(ymin);
   h_SingleMuon->SetMaximum(ymax);
   h_SingleMuon->Draw("P, E");
   h_SingleMuon->SetStats(0);
   h_SingleMuon->SetMinimum(ymin);
   h_SingleMuon->SetMaximum(ymax);
   c->SetLogy();
   s->Draw("HIST, SAME");
   s->SetMinimum(ymin);
   s->SetMaximum(ymax);
   h_SingleMuon->Draw("P, E, SAME");

   TLegend * l = new TLegend(0.225, 0.75, 0.875, 0.875);
   l->SetBorderSize(0);
   l->SetNColumns(3);
   for (int i = 0; i < nmc; ++i) l->AddEntry(h[i], labels[i], "F");
   l->AddEntry(h_QCD, "multijet", "F");
   l->AddEntry(h_SingleMuon, "data", "P");
   l->Draw();

   c->SaveAs("./plots/ZMuTauVisibleMass.pdf");

   plotControlRegions();
}

