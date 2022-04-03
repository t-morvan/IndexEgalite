import logging
from time import sleep
from typing import Dict, Any, Iterable, Union

import pandas as pd
import requests
from tqdm import tqdm

logging.basicConfig(filename="data/sirenisation.log", level=logging.INFO)

API_URL = "https://entreprise.data.gouv.fr/api/sirene/v3/unites_legales/"
FIELDS = [
    "siren",
    "activite_principale",
    "tranche_effectifs",
    "categorie_entreprise",
    "date_creation",
]


def parse(resp: Dict[str, Any]) -> Dict[str, Union[str, int]]:
    row = {field: resp.get(field, "") for field in FIELDS}
    row["n_etablissements"] = len(resp["etablissements"])
    return row


def sirenise(sirens: Iterable[str]) -> pd.DataFrame:
    """
    Sirenisation of a list of Siren id using SIREN API.
    """
    data = []
    for siren in tqdm(sirens):
        sleep(0.2)
        resp = requests.get(url=API_URL + siren)
        if resp.ok:
            siren_file = resp.json()["unite_legale"]
            row = parse(siren_file)
            data.append(row)
        elif resp.status_code == 404:
            logging.warning("Siren number not found : %s", siren)
            continue
        else:
            resp.raise_for_status()

    df_siren = pd.DataFrame(data)
    df_siren.to_csv("data/sirens.csv", index=False)

    return df_siren
