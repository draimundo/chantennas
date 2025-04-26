import requests
import json
import os.path
import os
import pandas

url = "https://data.geo.admin.ch/ch.bakom.standorte-mobilfunkanlagen/standorte-mobilfunkanlagen/standorte-mobilfunkanlagen_2056.json"

def download_file(url, folder):
    fn = url.split('/')[-1]
    r = requests.get(url, stream=True)
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder,fn)
    with open(path, 'wb') as f:
        f.write(r.content)

#TODO check if doesn't exists, load if needed
folder = "./data"
#download_file(url,folder)


data = json.load(open('./data/standorte-mobilfunkanlagen_2056.json'))
df = pandas.DataFrame(data['features'])
print(df.head())
print(df.head())