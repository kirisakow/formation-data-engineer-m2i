# Analyse de données

## Préambule

Le jeu de données pour l'exercice est le suivant : https://www.kaggle.com/etiennelq/french-employment-by-town

Ce jeu de données comprend :

- 5 fichiers CSV
- 2 fichiers GeoJSON

Le descriptif de chaque fichier est inclus dans le lien Kaggle ci-dessus.

## Les 3 fichiers à utiliser dans l'exercice sont :

- base_etablissement_par_tranche_effectif.csv
- population.csv
- name_geographic_information_modified.csv
- net_salary_per_town_categories.csv

## Questions

1. Trouver le top 3 des communes ayant le salaire moyen le plus élevé.
2. Trouver la liste des communes où les femmes gagnent en moyenne plus que les hommes.
3. Trouver le top 3 des communes ayant le plus de personnes de 15-30 ans (inclus).
4. Trouver le top 3 des communes ayant le plus grand rapport de 15-30 ans / population totale de la commune, pour les communes de plus de 100 000 habitants.
5. Trouver le top 3 des communes ayant le salaire moyen le plus élevé, parmi les communes de plus de 100 000 habitants.
6. Trouver le top 3 des communes ayant le salaire moyen le plus bas, parmi les communes de plus de 100 000 habitants.
7. Trouver le top 3 des regions ayant le plus de communes.

### Content

Four files are in the dataset :

- base\_etablissement\_par\_tranche\_effectif : give information on the number of firms in every french town, categorized by size, come from [INSEE](https://www.insee.fr/fr/statistiques/1893274)

    - `CODGEO` : geographique code for the town (can be joined with _code_insee_ column from "name\_geographic\_information.csv')
    - `LIBGEO` : name of the town (in french)
    - `REG` : region number
    - `DEP` : depatment number
    - `E14TST` : total number of firms in the town
    - `E14TS0ND` : number of unknown or null size firms in the town
    - `E14TS1` : number of firms with 1 to 5 employees in the town
    - `E14TS6` : number of firms with 6 to 9 employees in the town
    - `E14TS10` : number of firms with 10 to 19 employees in the town
    - `E14TS20` : number of firms with 20 to 49 employees in the town
    - `E14TS50` : number of firms with 50 to 99 employees in the town
    - `E14TS100` : number of firms with 100 to 199 employees in the town
    - `E14TS200` : number of firms with 200 to 499 employees in the town
    - `E14TS500` : number of firms with more than 500 employees in the town
<br/>
<br/>
- name\_geographic\_information : give geographic data on french town (mainly latitude and longitude, but also region / department codes and names )

    - `EU_circo` : name of the European Union Circonscription
    - `code_région` : code of the region attached to the town
    - `nom_région` : name of the region attached to the town
    - `chef`.lieu_région : name the administrative center around the town
    - `numéro_département` : code of the department attached to the town
    - `nom_département` : name of the department attached to the town
    - `préfecture` : name of the local administrative division around the town
    - `numéro_circonscription` : number of the circumpscription
    - `nom_commune` : name of the town
    - `codes_postaux` : post-codes relative to the town
    - `code_insee` : unique code for the town
    - `latitude` : GPS latitude
    - `longitude` : GPS longitude
    - `éloignement` : i couldn't manage to figure out what was the meaning of this number
<br/>
<br/>
- net\_salary\_per\_town\_per_category : salaries around french town per job categories, age and sex

    - `CODGEO` : unique code of the town
    - `LIBGEO` : name of the town
    - `SNHM14` : mean net salary
    - `SNHMC14` : mean net salary per hour for executive
    - `SNHMP14` : mean net salary per hour for middle manager
    - `SNHME14` : mean net salary per hour for employee
    - `SNHMO14` : mean net salary per hour for worker
    - `SNHMF14` : mean net salary for women
    - `SNHMFC14` : mean net salary per hour for feminin executive
    - `SNHMFP14` : mean net salary per hour for feminin middle manager
    - `SNHMFE14` : mean net salary per hour for feminin employee
    - `SNHMFO14` : mean net salary per hour for feminin worker
    - `SNHMH14` : mean net salary for man
    - `SNHMHC14` : mean net salary per hour for masculin executive
    - `SNHMHP14` : mean net salary per hour for masculin middle manager
    - `SNHMHE14` : mean net salary per hour for masculin employee
    - `SNHMHO14` : mean net salary per hour for masculin worker
    - `SNHM1814` : mean net salary per hour for 18-25 years old
    - `SNHM2614` : mean net salary per hour for 26-50 years old
    - `SNHM5014` : mean net salary per hour for &gt;50 years old
    - `SNHMF1814` : mean net salary per hour for women between 18-25 years old
    - `SNHMF2614` : mean net salary per hour for women between 26-50 years old
    - `SNHMF5014` : mean net salary per hour for women &gt;50 years old
    - `SNHMH1814` : mean net salary per hour for men between 18-25 years old
    - `SNHMH2614` : mean net salary per hour for men between 26-50 years old
    - `SNHMH5014` : mean net salary per hour for men &gt;50 years old
<br/>
<br/>
- population : [demographic](https://www.insee.fr/fr/statistiques/2863607) information in France per town, age, sex and living mode

    - `NIVGEO` : geographic level (arrondissement, communes…)
    - `CODGEO` : unique code for the town
    - `LIBGEO` : name of the town (might contain some utf-8 errors, this information has better quality name\_geographic\_information)
    - `MOCO` : cohabitation mode : \[list and meaning available in Data description\]
    - `AGE80_17` : age category (slice of 5 years) | ex : 0 -&gt; people between 0 and 4 years old
    - `SEXE` : sex, 1 for men | 2 for women
    - `NB` : Number of people in the category
<br/>
<br/>
- departments.geojson : contains the borders of french departments.