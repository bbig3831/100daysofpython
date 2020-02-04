import requests

resp = requests.get('https://data.cms.gov/resource/vtv9-ubcx.json')
data = resp.json()

for aco in data:
    print(aco['aco_name'])