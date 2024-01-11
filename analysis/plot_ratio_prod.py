import ROOT
import math 
import time
#from plot_dict import *

#Plotting script for trigger efficiencies
file = ROOT.TFile("histeffcross.root")
workdir =file.GetDirectory("plots")


Numerator = workdir.Get("num")
Denominator = workdir.Get("denom")


Efficiency = ROOT.TGraphAsymmErrors(Numerator,Denominator,'pT')
#Efficiency.SetLineColor(linecolor[1])
#Efficiency.SetMarkerStyle(markerstylesolid[1])
#Efficiency.SetMarkerColor(markercolor[1])
Efficiency.SetMarkerSize(1.5)
Efficiency.SetTitle("Trigger Efficiency")
Efficiency.GetXaxis().SetTitle("p_{T} [GeV]")
Efficiency.GetYaxis().SetTitle("Efficiency of cross trigger")
Efficiency.GetYaxis().SetRange(0,2) 

#legend = ROOT.TLegend(0.4412607,0.1932773,0.8223496,0.4453782)
#legend.SetFillStyle(1001)
#legend.SetBorderSize(0)
#legend.AddEntry(Efficiency,"Cross Trigger","ep")

canvas=ROOT.TCanvas("Trigger Efficiency", "Trigger Efficiency")
canvas.SetGrid()
Efficiency.Draw("ap")
#legend.Draw("same")

canvas.SaveAs("eff_HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1_leg_ALL.png")
canvas.SaveAs("eff_HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1_leg_ALL.pdf")
