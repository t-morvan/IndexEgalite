import requests
import sleep
import tqdm

API_URL = "https://entreprise.data.gouv.fr/api/sirene/v3/etablissements/"
FIELDS = ['activite_principale','tranche_effectifs','categorie_entreprise','date_creation']

def get_file(siren):
    url = API_URL + siren
    resp = requests.get(url).json()
    return resp

def parse(resp):  
    row = {field:resp.get(field,"") for field in FIELDS}
    row.update({'siren' : siren})
    return row

def sirenise(sirens):
    data = []
    for siren in tqdm(sirens):
        resp = get_file(siren)  
        row = parse(resp)
        data.append(row)
        time.sleep(0.2)
    df = pd.DataFrame(data)
    df.to_csv("data/siren.csv")





    