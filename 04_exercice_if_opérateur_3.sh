#!/bin/bash
# exercice 3:
# Réaliser un script qui :
# * compare l'âge de deux fichiers renseigné par l'utilisateur
# * Affiche quel fichier est le plus vieux
# * l'utilisateur devra renseigner le chemin des fichiers à comparer à partir de la racine.

if (( $# != 2 )); then
    echo "Usage : $(basename "$0") </chemin/absolu/au/fichier1> </chemin/absolu/au/fichier2>" >&2
    exit 1
fi

fichier1=$1
fichier2=$2

age_fichier1=$(stat -c '%W' $fichier1 2>/dev/null || echo -1)
if (( $age_fichier1 == -1 )); then
    echo "erreur : la date de création du fichier $fichier1 n'a pas pu être déterminée" >&2
    exit 1
fi
age_fichier2=$(stat -c '%W' $fichier2 2>/dev/null || echo -1)
if (( $age_fichier2 == -1 )); then
    echo "erreur : la date de création du fichier $fichier2 n'a pas pu être déterminée" >&2
    exit 1
fi

echo "Le fichier $fichier1 est plus ancien : créé le $(stat -c '%w' $fichier1)"
echo "Le fichier $fichier2 est plus récent : créé le $(stat -c '%w' $fichier2)"
