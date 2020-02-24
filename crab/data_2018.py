import json

data = {}
data['people'] = []

data['people'].append({
   'name': 'SingleMuon_Run2018C',
   'das': '/SingleMuon/Run2018C-Nano25Oct2019-v1/NANOAOD',
   'json': 'Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt',
   'nEvents': '110032072',
   'nFiles': '80',
})

with open('data_2018.json', 'w') as outfile:
   json.dump(data, outfile)
