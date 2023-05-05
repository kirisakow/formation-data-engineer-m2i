CREATE DATABASE IF NOT EXISTS `auto`;
USE `auto`;

DROP TABLE IF EXISTS auto.client;
CREATE TABLE auto.client (
    clientid INT NOT NULL AUTO_INCREMENT,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    adresse VARCHAR(255) NOT NULL,
    dateNaissance DATE NOT NULL,
    PRIMARY KEY (clientid)
);

DROP TABLE IF EXISTS auto.cd_rom;
CREATE TABLE auto.cd_rom (
    cdromid INT NOT NULL AUTO_INCREMENT,
    editeur VARCHAR(255) NOT NULL,
    PRIMARY KEY (cdromid)
);

DROP TABLE IF EXISTS auto.question;
CREATE TABLE auto.question (
    questionId INT NOT NULL AUTO_INCREMENT,
    intitule VARCHAR(255) NOT NULL,
    reponse VARCHAR(255) NOT NULL,
    niveauDifficulte INT NOT NULL,
    theme VARCHAR(255) NOT NULL,
    PRIMARY KEY (questionId)
);

DROP TABLE IF EXISTS auto.serie;
CREATE TABLE auto.serie (
    serieId INT NOT NULL AUTO_INCREMENT,
    cd_rom_cdromid INT NOT NULL,
    PRIMARY KEY (serieId),
    FOREIGN KEY (cd_rom_cdromid) REFERENCES auto.cd_rom(cdromid)
);

DROP TABLE IF EXISTS auto.serie_has_question;
CREATE TABLE auto.serie_has_question (
    serie_serieId INT NOT NULL,
    question_questionId INT NOT NULL,
    PRIMARY KEY (serie_serieId, question_questionId),
    FOREIGN KEY (serie_serieId) REFERENCES auto.serie(serieId),
    FOREIGN KEY (question_questionId) REFERENCES auto.question(questionId)
);

DROP TABLE IF EXISTS auto.seance_code;
CREATE TABLE auto.seance_code (
    seanceCodeId INT NOT NULL AUTO_INCREMENT,
    date DATE NOT NULL,
    heure TIME NOT NULL,
    nombreFautes INT NOT NULL,
    lieu VARCHAR(255) NOT NULL,
    estExamen BOOLEAN NOT NULL,
    serie_serieId INT NOT NULL,
    client_clientid INT NOT NULL,
    PRIMARY KEY (seanceCodeId),
    FOREIGN KEY (serie_serieId) REFERENCES auto.serie(serieId),
    FOREIGN KEY (client_clientid) REFERENCES auto.client(clientid)
);


insert into auto.client set nom='Dupont', prenom='Jean', adresse='18 rue de la mer', dateNaissance='1980-02-03';
insert into auto.client set nom='Durant', prenom='Henry', adresse='25 rue de la mer', dateNaissance='1975-01-09';
insert into auto.client set nom='Jones', prenom='Indiana', adresse='1 boulevard Oxford', dateNaissance='1965-12-03';
insert into auto.client set nom='Skywalker', prenom='Luke', adresse='1 route l’étoile', dateNaissance='2023-07-07';

insert into auto.cd_rom set editeur='Legrand';
insert into auto.cd_rom set editeur='Lafarge';
insert into auto.cd_rom set editeur='Le vent du large';

insert into auto.question set intitule='Doubler velo dans un virage', reponse='non', niveauDifficulte='1', theme='Doubler';
insert into auto.question set intitule='Se rabatre après doubler', reponse='oui', niveauDifficulte='1', theme='Doubler';
insert into auto.question set intitule='Mettre sa ceinture', reponse='oui', niveauDifficulte='0', theme='Base';
insert into auto.question set intitule='Doubler velo dans un virage 2', reponse='non', niveauDifficulte='1', theme='Doubler';
insert into auto.question set intitule='Se rabatre après doubler 2', reponse='oui', niveauDifficulte='1', theme='Doubler';
insert into auto.question set intitule='Mettre sa ceinture 2', reponse='oui', niveauDifficulte='0', theme='Base';
insert into auto.question set intitule='Doubler velo dans un virage 3', reponse='non', niveauDifficulte='1', theme='Doubler';
insert into auto.question set intitule='Se rabatre après doubler 4', reponse='oui', niveauDifficulte='1', theme='Doubler';
insert into auto.question set intitule='Mettre sa ceinture 5', reponse='oui', niveauDifficulte='0', theme='Base';

insert into auto.serie set cd_rom_cdromid=1;
insert into auto.serie set cd_rom_cdromid=2;
insert into auto.serie set cd_rom_cdromid=1;

insert into auto.serie_has_question set serie_serieId=1, question_questionId=1;
insert into auto.serie_has_question set serie_serieId=1, question_questionId=2;
insert into auto.serie_has_question set serie_serieId=1, question_questionId=3;
insert into auto.serie_has_question set serie_serieId=2, question_questionId=1;
insert into auto.serie_has_question set serie_serieId=2, question_questionId=2;
insert into auto.serie_has_question set serie_serieId=2, question_questionId=3;

insert into auto.seance_code set date='2001-01-01', heure='10:00:00', nombreFautes=3, lieu='Somewhere', estExamen=false, serie_serieId=1, client_clientid=1;
insert into auto.seance_code set date='2001-01-02', heure='10:00:00', nombreFautes=4, lieu='Somewhere', estExamen=false, serie_serieId=1, client_clientid=1;
insert into auto.seance_code set date='2001-01-03', heure='10:00:00', nombreFautes=1, lieu='Somewhere', estExamen=false, serie_serieId=1, client_clientid=1;
insert into auto.seance_code set date='2001-01-04', heure='10:00:00', nombreFautes=3, lieu='Somewhere', estExamen=true, serie_serieId=2, client_clientid=1;
insert into auto.seance_code set date='2001-01-01', heure='10:00:00', nombreFautes=3, lieu='Somewhere', estExamen=false, serie_serieId=1, client_clientid=2;
insert into auto.seance_code set date='2001-01-02', heure='10:00:00', nombreFautes=5, lieu='Somewhere', estExamen=false, serie_serieId=1, client_clientid=2;
insert into auto.seance_code set date='2001-01-03', heure='10:00:00', nombreFautes=2, lieu='Somewhere', estExamen=false, serie_serieId=1, client_clientid=2;

