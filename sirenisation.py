import requests
from time import sleep
import pandas as pd
from tqdm import tqdm

API_URL = "https://entreprise.data.gouv.fr/api/sirene/v3/unites_legales/"
FIELDS = ['siren', 'activite_principale', 'tranche_effectifs', 'categorie_entreprise', 'date_creation']

def get_file(siren):
    url = API_URL + str(siren)
    resp = requests.get(url).json()
    resp = resp['unite_legale']
    return resp

def parse(resp):
    row = {field:resp.get(field,"") for field in FIELDS}
    row["n_etablissements"] = len(resp['etablissements'])
    return row

def sirenise(sirens):
    data = []
    for siren in tqdm(sirens):
        try :
            resp = get_file(siren)
        except KeyError:
            continue
        else:
            row = parse(resp)  
            data.append(row)
        sleep(0.2)
    df = pd.DataFrame(data)
    df.to_csv("data/sirens.csv", index = False)





    