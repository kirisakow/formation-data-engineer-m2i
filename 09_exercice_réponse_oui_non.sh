#!/usr/bin/env bash
# Exercice Réponse Utilisateur
# Créer un script qui demande à l'utilisateur s'il valide (Oui/oui) ou refuse (Non/non).
# Si l'utilisateur entre autre chose, le script repose la même question.
# S'il rentre une bonne réponse le script s'arrete.
# indice : vous utiliserez des conditions de type if
# Version 2 :les réponses utilisateurs peuvent aller jusqu'a (Oui/oui/O/o) ou (Non/non/N/n)
# Vous utiliserez un case

prompt="Validez en saisissant Oui/oui ou Non/non : "
read -r -p "$prompt" reponse
while true; do
    case "${reponse}" in
        O|o|Oui|oui)
            echo "Merci. Validation enregistrée"
            exit 0
        ;;
        N|n|Non|non)
            echo "Merci. Validation rejetée"
            exit 0
        ;;
        *)
            read -r -p "Réponse incorrecte. $prompt" reponse
        ;;
    esac
done