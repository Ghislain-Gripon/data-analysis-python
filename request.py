import requests
import json

url = 'http://0.0.0.0:5000/api/'

data = [[294.613340, 176.0, 144.0, 55242.0, 12.0, 61.0, 3474.0, 0.0, 3535.0, 84002.0, 1950409.0, 2034411.0, 820000.0, 24.0, 176.0, 144.0, 88736.0]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)
