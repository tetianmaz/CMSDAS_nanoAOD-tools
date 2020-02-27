import json

data = {}
data['people'] = []
data['people'].append({
   'name': 'SingleMuon_Run2018A',
   'das': '/SingleMuon/Run2018A-Nano25Oct2019-v1/NANOAOD',
   'json': 'Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt',
   'nEvents': '241608232',
   'nFiles': '210',
})
data['people'].append({
   'name': 'SingleMuon_Run2018B',
   'das': '/SingleMuon/Run2018B-Nano25Oct2019-v1/NANOAOD',
   'json': 'Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt',
   'nEvents': '119918017',
   'nFiles': '81',
})
data['people'].append({
   'name': 'SingleMuon_Run2018C',
   'das': '/SingleMuon/Run2018C-Nano25Oct2019-v1/NANOAOD',
   'json': 'Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt',
   'nEvents': '110032072',
   'nFiles': '80',
})
data['people'].append({
   'name': 'SingleMuon_Run2018D',
   'das': '/SingleMuon/Run2018D-Nano25Oct2019-v1/NANOAOD',
   'json': 'Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt',
   'nEvents': '513867253',
   'nFiles': '252',
})

with open('data_2018.json', 'w') as outfile:
   json.dump(data, outfile)
