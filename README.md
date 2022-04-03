# IndexEgalite

Le ministère du travail met à disposition l'index d'égalité professionnelle femmes hommes des entreprises  :
https://www.data.gouv.fr/en/datasets/index-egalite-professionnelle-f-h-des-entreprises-de-plus-de-250-salaries/

Les entreprises sont identifiées par leur SIREN mais la base ne contient pas d'informations sur le type d'activité ce qui empêche de mener des analyses par secteurs.

Ce code appelle l'[API Siren]( https://entreprise.data.gouv.fr/api_doc/sirene) pour retrouver les informations d'activités et d'effectifs des entreprises. Le code d'activité est ensuite décliné en plusieurs niveaux de classification via la nomenclature de l'INSEE [NAF rév.2](https://www.insee.fr/fr/information/2120875).

La base consolidée est disponible dans `data/index-egalite-fh.csv`.
