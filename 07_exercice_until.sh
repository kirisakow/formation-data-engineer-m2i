#!/bin/bash
# Réaliser à l'aide de la boucle until un script qui demande à l'utilisateur
# d'écrire "Je veux sortir" pour quitter le script.
# Tant que l'utilisateur n'aura pas écrit la réponse attendue, le
# script affichera "Mauvaise réponse. Pour sortir, taper 'Je veux sortir'"
# pour chacune de ses réponses.
#     ./hello.sh
#     Pour sorir de ce script, taper 'Je veux sortir' : leave
#     Mauvaise réponse. Pour sortir,  taper 'Je veux sortir' : 24
#     Mauvaise réponse. Pour sortir,  taper 'Je veux sortir' : é
#     Mauvaise réponse. Pour sortir,  taper 'Je veux sortir' : @
#     Mauvaise réponse. Pour sortir,  taper 'Je veux sortir' : Je veux sortir
#     Au revoir

phrase_attendue="Je veux sortir"

prompt="Pour sortir,  taper 'Je veux sortir' : "
read -r -p "$prompt" phrase_saisie

until [[ "$phrase_saisie" == "$phrase_attendue" ]]
do
    read -r -p "Mauvaise réponse. $prompt" phrase_saisie
done

echo "Au revoir"
exit 0