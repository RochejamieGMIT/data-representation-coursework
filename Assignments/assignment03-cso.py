import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
response = requests.get(url)
data = response.json()
with open ("cso.json", "w") as fp:
    json.dump(data, fp)

print(fp)