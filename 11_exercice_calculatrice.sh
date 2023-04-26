#!/usr/bin/env bash
# Réaliser une calculatrice avec les opérations basiques + - / *  sur 2 variables données par l'utilisateur.
# Afficher l’opération et le résultat.

function usage() {
    echo "erreur : usage : $(basename "$0")   <opérand numérique>   <un des opérateurs: + - / \* x>   <opérand numérique>"
}

if (( $# != 3 ))
then
    usage
    exit 1
fi

function is_number() {
    value_to_test=$1
    code_retour=1
    if [[ $value_to_test =~ ^[+-]?[0-9]+([.][0-9]+)?$ ]]
    then
        code_retour=0
    fi
    return $code_retour
}

operand1=$1
operateur=$2
operand2=$3

if ! is_number "$operand1"
then
    echo "erreur : $operand1 n'est pas un nombre" >&2
    exit 1
fi
if ! is_number "$operand2"
then
    echo "erreur : $operand2 n'est pas un nombre" >&2
    exit 1
fi

shopt -s extglob
case "${operateur}" in
    !(+|-|/|\*|x) ) usage >&2 ; exit 1 ;;
    @(+)         ) echo $((operand1 + operand2)) ;;
    @(-)         ) echo $((operand1 - operand2)) ;;
    @(/)         ) echo $((operand1 / operand2)) ;;
    @(\*|x)       ) echo $((operand1 * operand2)) ;;
    *            ) usage >&2 ; exit 1 ;;
esac
