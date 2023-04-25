#!/bin/bash
# exercice 1:
# Réaliser avec select un script qui propose à l'utilisateur de choisir entre trois formats de dates différentes.
# Ces formats seront : - J/M/A - M/A/J - A/J/M

select date_format in J/M/A M/A/J A/J/M
do
    echo "Vous avez choisi $date_format"
done