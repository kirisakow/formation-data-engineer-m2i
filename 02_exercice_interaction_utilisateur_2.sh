#!/bin/bash
# exercice 2:
# Réaliser un script qui :
# * Demande à l'utilisateur son login, 5 caractères maximum peuvent être renseignés
# * Demande à l'utilisateur son Mot de passe, celui-ci ne doit pas s'afficher à l'écran et l'utilisateur à 10 secondes pour le rentrer.
# * Affiche à l'écran le login et le mot de passe donné par l'utilisateur.

read -n 5 -p "Veuillez renseigner un login (5 char max) : " login
echo "Merci. Votre login est : $login"
read -s -t 10 -p "Veuillez renseigner un mot de passe (vous avez 10 secondes) : " mdp
echo "Merci. Votre mot de passe est : $mdp"