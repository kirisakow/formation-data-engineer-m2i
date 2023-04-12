# Excercice Panda

## Préparation de l'environnement

### Installation de Python

Sur windows, téléchargez et installez Python depuis le site officiel : https://www.python.org/downloads/

### Installation de pip

pip est un gestionnaire de paquets utilisé pour installer et gérer des paquets de logiciels écrits en Python. Il est installé par défaut avec Python 2 >=2.7.9 ou Python 3 >=3.4.

### Installation de Docker

Docker est un logiciel libre qui permet de créer, déployer et exécuter des applications dans des conteneurs logiciels. Il est disponible pour Windows, macOS et Linux.

Pour installer Docker, téléchargez et installez Docker Desktop depuis le site officiel : https://www.docker.com/products/docker-desktop

### Installation de MariaDB

MariaDB est un système de gestion de base de données relationnelle (SGBDR) libre et open source. Il est disponible pour Windows, macOS et Linux.

Démarrer le conteneur MariaDB en exécutant la commande suivante :

```bash
docker-compose up -d
```

### Création d'un environnement virtuel

Un environnement virtuel est un outil qui aide à garder les dépendances requises pour un  projet de façon séparé des autres. Il s'agit d'un dossier contenant des copies spécifiques des bibliothèques Python nécessaires pour les projets Python.

Pour créer un environnement virtuel, exécutez la commande suivante :

```bash
py -m venv .venv
```

## Étapes

- Installation des dépendances
- Lire le fichier CSV
- Créer une connexion à la base de données
- Créer un curseur
- Insérer les données dans la base de données

## Étape 1 : Installation des dépendances

Assurez-vous d'avoir installé les modules requis : pandas et pymysql. Vous pouvez les installer en utilisant pip:

```bash
pip install pandas pymysql
```

## Étape 2 : Créez un fichier CSV

Créez un fichier CSV nommé "clients.csv" avec le contenu suivant :

```csv
id,firstname,lastname,email,profession,country,city
1,Juliane,Ramona,Juliane.Ramona@yopmail.com,worker,Mexico,Chennai
2,Jsandye,Marlie,Jsandye.Marlie@yopmail.com,doctor,Malta,Lahore
3,Calla,Christal,Calla.Christal@yopmail.com,doctor,Tokelau,Douglas
```

## Étape 3 : Créez un fichier Python

Créez un fichier Python nommé "import_csv.py". Ce fichier contiendra le code pour lire le fichier CSV et l'importer dans la base de données.


### Étape 3.1 : Importer les modules

Importez les modules pandas et pymysql dans le fichier Python.

```python
import pandas as pd
import pymysql
```

### Étape 3.2 : Lire le fichier CSV

1. Lisez le fichier CSV "clients.csv" et affichez le contenu.

    ```python
    df = pd.read_csv('clients.csv')
    print(df)
    ```

2. Affichez de la ligne 2 à la ligne 4 du fichier CSV.

    ```python
    df = lire_csv('clients.csv')
    print(df[1:4])
    ```

3. Placer le code dans une fonction nommée "lire_csv" et appeler cette fonction dans le fichier Python. Cette fonction aura comme signature : `lire_csv(nom_fichier: str) -> pd.DataFrame`

### Étape 3.3 : Importer des données dans la base de données

#### Étape 3.3.1 : Créer une connexion à la base de données

Créez une fonction nommée "creer_connexion" qui aura comme signature : `se_connecter_db() -> pymysql.Connection`. Cette fonction aura pour but de créer une connexion à la base de données.

```python
def se_connecter_db(host, user, password, database):
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    return conn
```

Testez la fonction en appelant la fonction "se_connecter_db" dans le fichier Python.

```python
db_host = "localhost"
db_user = "utilisateur"
db_password = "utilisateur"
db_database = "exemple"

conn = se_connecter_db(db_host, db_user, db_password, db_database)
```

#### Étape 3.3.2 : Insérer les données dans la base de données

Fabriquez une liste d'utilisateurs à partir du fichier CSV.

Insérez des données utilisateurs dans la base de données.

```python
def inserer_donnees(conn, utilisateurs):
    cursor = conn.cursor()
    for index, row in df.iterrows():
        sql = "INSERT INTO clients (id, firstname, lastname, email, profession, country, city) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (row['id'], row['firstname'], row['lastname'], row['email'], row['profession'], row['country'], row['city']))
    conn.commit()
```
