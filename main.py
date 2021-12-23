import pandas as pd
from sirenisation import sirenise


if __name__ == "__main__":

    # fichier non consolidé de l'index égalité homme femme
    egal_hf = pd.read_csv("data/")

    # sirenisation des entreprises
    sirens = egal_hf[["SIREN"]]
    sirenise(sirens)

    # conversion des codes de la nomenclature NAF2 vers 
    sirens = pd.read("data/")
    nomenc = pd.read_csv("data/")
    sirens = sirens.merge(nomenc, how="left", left_on="activite_principale", right_on="id_5")

    # ajout des informations à la base initiale
    egal_hf_cons = egal_hf.merge(sirens, on="siren")
    egal_hf_cons.to_csv("data/")
