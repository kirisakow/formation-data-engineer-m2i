-- créations des bases de données
CREATE DATABASE IF NOT EXISTS exercice;

use exercice;

-- création des tables
CREATE TABLE clients (
    id INT PRIMARY KEY,
    prenom VARCHAR(255),
    nom VARCHAR(255),
    email VARCHAR(255),
    profession VARCHAR(255),
    pays VARCHAR(255),
    ville VARCHAR(255)
);