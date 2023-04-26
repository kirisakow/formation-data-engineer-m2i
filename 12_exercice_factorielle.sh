#!/usr/bin/env bash
# Créer un script qui permet de calculer et d'afficher la factorielle d'un nombre donné en paramètre
# (ou saisi en cas d'absence de paramètres).
# Rappel : En mathématiques, la factorielle d'un entier naturel n est le produit des nombres entiers
# strictement positifs inférieurs ou égaux à n. Soit n un entier naturel. Sa factorielle est
# formellement définie par : n! = 1 * 2 * 3 * ... * (n-1) * n

function usage() {
    echo "usage : $(basename "$0") <nombre entier positif>"
}

function is_positive_integer() {
    value_to_test=$1
    code_retour=1
    if [[ $value_to_test =~ ^[1-9]|([1-9][0-9]+)$ ]]
    then
        code_retour=0
    fi
    return $code_retour
}

if [[ $# -eq 0 ]]
then
    echo "erreur : $(usage)" >&2
    exit 1
elif ! is_positive_integer "$1"
then
    echo "erreur : $(usage)" >&2
    exit 1
elif [[ $1 -eq 0 ]]
then
    echo "erreur : $(usage)" >&2
    exit 1
fi

nombre=$1
printf "n! = 1"
if (( nombre > 1 )); then
    for n in $(seq 1 $nombre)
    do
        LC_ALL=fr_FR printf " * %'d" $n
    done
fi
