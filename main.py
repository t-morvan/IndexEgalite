import pandas as pd
from sirenisation import sirenise


if __name__ == "__main__":

    # fichier non consolidé de l'index égalité homme femme
    egal_hf = pd.read_csv("data/index-egalite-fh.csv", sep=";")

    # sirenisation des entreprises
    sirens = set(egal_hf["SIREN"])
    sirenise(sirens)

    # conversion des codes de la nomenclature NAF2 vers 
    sirens = pd.read_csv("data/sirens.csv")
    nomenc = pd.read_csv("data/naf.csv")
    sirens = sirens.merge(nomenc, how="left", left_on="activite_principale", right_on="id_5")

    # ajout des informations à la base initiale
    egal_hf_cons = egal_hf.merge(sirens, left_on="SIREN", right_on="siren")
    egal_hf_cons.to_csv("data/index_eg_hf_cons.csv")
