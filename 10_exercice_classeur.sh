#!/usr/bin/env bash
# Le classeur
# Réaliser un script bash qui va classer dans des sous répertoire tous les fichiers d'un répertoire selon leursextensions. Le script prend en argument le nom du répertoire cible.

if (( $# != 1 ))
then
    echo "Erreur : Usage : $(basename "$0") <chemin absolu du répertoire contenant des fichiers>" >&2
    exit 1
fi

function determiner_extension () {
    if (( $# != 1 ))
    then
        exit 1
    fi
    nom_fichier=$1
    extension_fichier="other"
    nom_fichier_sans_premier_char=${nom_fichier:1}
    nom_fichier_decoupe_au_point_en_n_segments=$(echo "$nom_fichier_sans_premier_char" | awk '{print split($0, a, ".")}')
    if (( nom_fichier_decoupe_au_point_en_n_segments > 1 ))
    then
        extension_fichier=${nom_fichier##*.}
    fi
    echo "$extension_fichier"
}

repertoire_cible=$1
repertoire_cible_absolu=$(cd "$(dirname "$repertoire_cible")" || exit 1; pwd)
echo "Le répertoire cible est : $repertoire_cible_absolu"
mkdir -p "$repertoire_cible_absolu" || exit 1
cd "$repertoire_cible_absolu" || exit 1
repertoires_et_fichiers_tries_par_extension=$(ls -1aApX --group-directories-first)
fichiers_sans_repertoires=$(echo "$repertoires_et_fichiers_tries_par_extension" | grep -v -E '/$')
for nom_fichier in $fichiers_sans_repertoires
do
    extension_fichier=$(determiner_extension "$nom_fichier")
    repertoire_destination_absolu="$repertoire_cible_absolu/classeur/$extension_fichier"
    if [ ! -d "$repertoire_destination_absolu" ]
    then
        mkdir -p "$repertoire_destination_absolu"
    fi
    cp "$nom_fichier" "$repertoire_destination_absolu"
done
echo
echo "Résultat : contenu du répertoire $repertoire_cible_absolu/classeur :"
echo
tree -a "$repertoire_cible_absolu/classeur"