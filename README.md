# TP Docker

Petit exemple d'application Web containerisée / dockerisée C.R.U.D. de gestion d'utilisateurs

## Étapes à effectuer

- [ ] Créer un API HTTP simple en Flask
    - [ ] dans un environnement virtuel Python (`venv`), exclus du dépôt GitHub ;
    - [ ] assorti d'un fichier `requirements.txt` permettant de récupérer toutes les dépendances ;
    - [ ] publié en tant que dépôt GitHub ;
    - [ ] assorti d'un fichier `.gitignore` correctement renseigné ;
    - [ ] comportant les fonctionnalités C.R.U.D. suivantes :
      - CREATE: créer un utilisateur (avec une requête comme `POST http://.../user`) ;
      - RETRIEVE: afficher tous utilisateurs (avec une requête comme `GET http://.../users`), afficher un utilisateur identifié par son ID (avec une requête comme `GET http://.../user/42`) ;
      - UPDATE: mettre à jour un utilisateur (avec une requête comme `PUT http://.../user/42`) ;
      - DELETE: supprimer un utilisateur (avec une requête comme `DELETE http://.../user/42`).
- [ ] Porter la couche persistance en MongoDB.
- [ ] Dockeriser l'application en créant un fichier `Dockerfile`.
- [ ] Créer une composition de containers avec un fichier `docker-compose.yml`. Consignes :
    - trois services : l'application Flask, la base de données MongoDB, l'IHM MongoExpress ;
    - la base de données doit être montée en tant que volume, si bien qu'elle doit continuer d'exister après la destruction des containers qui l'utilisent ;
    - les données confidentielles telles que les mots de passes ne doivent pas figurer dans le fichier `docker-compose.yml` mais doivent être stockées dans un fichier `.env` exclus du dépôt GitHub.