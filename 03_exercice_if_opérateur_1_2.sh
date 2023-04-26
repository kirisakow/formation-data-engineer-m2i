#!/bin/bash
# Exercice If et Opérateur
# Exercice 1 :
# Réaliser un script qui demande à l'utilisateur de rentrer un nombre ;
# Si le nombre est égal à 0, Afficher "Vous avez entré zéro."
# Si le nombre est inférieur à 0, Afficher "Vous avez entré un nombre négatif."
# Si le nombre est supérieur à 0, Afficher "Vous avez entré un nombre positif."
# Exercice 2:
# Modifier le script afin que si l'utilisateur renseigne autre chose qu'un nombre, le script lui retourne :
# "Ceci n'est pas un nombre"

if (( $# != 1 )); then
    echo "Aucun nombre passé en paramètre. Usage : $(basename "$0") <nombre entier>"
    exit 1
fi

nombre=$1

if [[ ! $nombre =~ ^[+-]?[0-9]+([.][0-9]+)?$ ]]; then
    echo "erreur : $nombre n'est pas un nombre"
    exit 1
elif ((nombre < 0)); then
    echo "Vous avez entré un nombre négatif"
    exit 0
elif ((nombre == 0)); then
    echo "Vous avez entré zéro"
    exit 0
elif ((nombre > 0)); then
    echo "Vous avez entré un nombre positif"
    exit 0
fi