import json

data = []

data.append({
    'name': 'Electron_2018A',
    'inputDataset': '/EGamma/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
    'nFiles': '226',
})

data.append({
    'name': 'Electron_2018B',
    'inputDataset': '/EGamma/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
    'nFiles': '74',
})

data.append({
    'name': 'Electron_2018C',
    'inputDataset': '/EGamma/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
    'nFiles': '83',
})

data.append({
    'name': 'Electron_2018D',
    'inputDataset': '/EGamma/Run2018D-UL2018_MiniAODv2_NanoAODv9-v3/NANOAOD',
    'nFiles': '349',
})

data.append({
    'name': 'Muon_2018A',
    'inputDataset': '/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
    'nFiles': '123',
})

data.append({
    'name': 'Muon_2018B',
    'inputDataset': '/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD',
    'nFiles': '51',
})

data.append({
    'name': 'Muon_2018C',
    'inputDataset': '/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD',
    'nFiles': '56',
})

data.append({
    'name': 'Muon_2018D',
    'inputDataset': '/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
    'nFiles': '194',
})

data.append({
    'name': 'Tau_2018A',
    'inputDataset': '/Tau/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
    'nFiles': '50',
})

data.append({
    'name': 'Tau_2018B',
    'inputDataset': '/Tau/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
    'nFiles': '35',
})

data.append({
    'name': 'Tau_2018C',
    'inputDataset': '/Tau/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
    'nFiles': '30',
})

data.append({
    'name': 'Tau_2018D',
    'inputDataset': '/Tau/Run2018D-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD',
    'nFiles': '153',
})

#data.append({
#    'name': 'MuonEG_2018A',
#    'inputDataset': '/MuonEG/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
#    'nFiles': '33',
#})

#data.append({
#    'name': 'MuonEG_2018B',
#    'inputDataset': '/MuonEG/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
#    'nFiles': '20',
#})

#data.append({
#    'name': 'MuonEG_2018C',
#    'inputDataset': '/MuonEG/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
#    'nFiles': '22',
#})

#data.append({
#    'name': 'MuonEG_2018D',
#    'inputDataset': '/MuonEG/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
#    'nFiles': '63',
#})

for entry in data:
   entry['year'] = '2018'
   entry['lumiMask'] = 'Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt' 

with open('datasamples_2018.json', 'w') as outfile:
   json.dump(data, outfile)
