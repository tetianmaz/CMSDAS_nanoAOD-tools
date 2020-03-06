import json

data = {}
data['people'] = []
isMC_ = True

data['people'].append({
   'name': 'WJetsToLNu',
   'das': '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '70454125',
   'nFiles': '50',
   'isMC': isMC_,
   'xs': '52940.0', #LO
})
data['people'].append({
   'name': 'W1JetsToLNu',
   'das': '/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '51082776',
   'nFiles': '39',
   'isMC': isMC_,
   'xs': '',
})
data['people'].append({
   'name': 'W2JetsToLNu',
   'das': '/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '23290710',
   'nFiles': '22',
   'isMC': isMC_,
   'xs': '2793.0', #LO
})
data['people'].append({
   'name': 'W3JetsToLNu',
   'das': '/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '14508481',
   'nFiles': '17',
   'isMC': isMC_,
   'xs': '992.5', #LO
})
data['people'].append({
   'name': 'W4JetsToLNu',
   'das': '/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '10082747',
   'nFiles': '11',
   'isMC': isMC_,
   'xs': '544.3', #LO
})
data['people'].append({
   'name': 'DYJetsToLL_M-50',
   'das': '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '100194597',
   'nFiles': '58',
   'isMC': isMC_,
   'xs': '6077.22', ##NNLO
})
data['people'].append({
   'name': 'DY1JetsToLL_M-50',
   'das': '/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '68898175',
   'nFiles': '64',
   'isMC': isMC_,
   'xs': '877.8', #LO
})
data['people'].append({
   'name': 'DY2JetsToLL_M-50',
   'das': '/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '20456037',
   'nFiles': '15',
   'isMC': isMC_,
   'xs': '304.4', #LO
})
data['people'].append({
   'name': 'DY3JetsToLL_M-50',
   'das': '/DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '5652357',
   'nFiles': '7',
   'isMC': isMC_,
   'xs': '111.5', #LO
})
data['people'].append({
   'name': 'DY4JetsToLL_M-50',
   'das': '/DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '2817812',
   'nFiles': '8',
   'isMC': isMC_,
   'xs': '44.03', #LO
})
data['people'].append({
   'name': 'TTJets',
   'das': '/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '10244307',
   'nFiles': '13',
   'isMC': isMC_,
   'xs': '496.1', #LO
})
data['people'].append({
   'name': 'TTTo2L2Nu',
   'das': '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '64120000',
   'nFiles': '59',
   'isMC': isMC_,
   'xs': '88.29', #NNLO
})
data['people'].append({
   'name': 'TTToSemiLeptonic',
   'das': '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '101550000',
   'nFiles': '84',
   'isMC': isMC_,
   'xs': '365.34', #NNLO
})
data['people'].append({
   'name': 'TTToHadronic',
   'das': '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v3/NANOAODSIM',
   'nEvents': '131024000',
   'nFiles': '18',
   'isMC': isMC_,
   'xs': '377.96', #NNLO
})
'''data['people'].append({
   'name': 'TTToHadronic_ext',
   'das': '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext2-v1/NANOAODSIM',
   'nEvents': '199524000',
   'nFiles': '145',
   'isMC': isMC_,
   'xs': '377.96', ##NNLO
})'''
data['people'].append({
   'name': 'QCD_Pt-20toInf_MuEnrichedPt15',
   'das' :'/QCD_Pt-20toInf_MuEnrichedPt15_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '22165320',
   'nFiles': '20',
   'isMC': isMC_,
   'xs': '239400.0',
})
'''
data['people'].append({
   'name': 'WW',
   'das': '/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '7850000',
   'nFiles': '25',
   'isMC': isMC_,
   'xs': '75.8', #unknown
})
data['people'].append({
   'name': 'WZ',
   'das': '/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '3885000',
   'nFiles': '5',
   'isMC': isMC_,
   'xs': '27.6', #unknown
})
data['people'].append({
   'name': 'ZZ',
   'das': '/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '1979000',
   'nFiles': '6',
   'isMC': isMC_,
   'xs': '12.14', #unknown
})
data['people'].append({
   'name': 'DYJetsToLL_M-10to50',
   'das': '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '39392062',
   'nFiles': '29',
   'isMC': isMC_,
   'xs': '15810', #LO
})
data['people'].append({
   'name': 'DYJetsToLL_M-10to50_ext',
   'das': '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM',
   'nEvents': '46976952',
   'nFiles': '27',
   'isMC': isMC_,
   'xs': '15810', #LO
})
data['people'].append({
   'name': 'ST_tW_antitop',
   'das': '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM',
   'nEvents': '7623000',
   'nFiles': '11',
   'isMC': isMC_,
   'xs': '34.97', #NLO
})
data['people'].append({
   'name': 'ST_tW_top',
   'das': '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM',
   'nEvents': '9598000',
   'nFiles': '12',
   'isMC': isMC_,
   'xs': '34.91', #NLO
})
data['people'].append({
   'name': 'ST_t-channel_antitop',
   'das' : '/ST_t-channel_antitop_5f_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '3955024',
   'nFiles': '4',
   'isMC': isMC_,
   'xs': '',
})
data['people'].append({
   'name': 'ST_t-channel_top',
   'das': '/ST_t-channel_top_5f_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM',
   'nEvents': '5903676',
   'nFiles': '8',
   'isMC': isMC_,
   'xs': '119.7', #NLO
})'''

with open('mc_2018.json', 'w') as outfile:
   json.dump(data, outfile)
