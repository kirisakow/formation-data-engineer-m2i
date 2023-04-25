#!/bin/bash
# Exercice Case
# Réaliser un script qui demande à l'utilisateur de choisir une de ces options :
# * r pour démarrer. Lorsque cette option est choisie, informer l'utilisateur que le programme démarre.
# * s pour arrêter. Lorsque cette option est choisie, informer l'utilisateur que le programme s'arrête.
# * d pour supprimer. Lorsque cette option est choisie, informer l'utilisateur que le programme se supprime.
# * h pour afficher l'aide disponible. Lorsque cette option est choisie, informer l'utilisateur que le
# programme affiche l'aide disponible.

function choisir() {
    read -n 1 -p "Veuillez choisir une des options (r, s, d ou h) : " choix

    echo

    case "$choix" in
        r)
            echo "choix $choix : le programme va démarrer"
        ;;
        s)
            echo "choix $choix : le programme va s'arrêter"
        ;;
        d)
            echo "choix $choix : le programme va être supprimé"
        ;;
        h)
            echo "choix $choix : le programme affiche la notice d'aide"
        ;;
        *)
            echo "erreur : choix inconnu" >&2
            choisir
        ;;
    esac

}

choisir