#!/usr/bin/env bash
# Réaliser à l'aide de la boucle for un script qui affiche la table de multiplication de 54.

for diviseur in {1..54}; do
    reste=$((54 % diviseur))
    if (( $reste == 0 )); then
        quotient=$((54 / diviseur))
        echo "$diviseur x $quotient = 54"
    fi
done