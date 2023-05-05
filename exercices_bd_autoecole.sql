# Créez et validez les requêtes suivantes :

### 1.  Sélectionner tous les clients qui sont nés avant 1980

SELECT *
FROM client
WHERE year(dateNaissance) < 1980
;

### 2.  Sélectionner tous les examens passés par le client n°1

SELECT *
FROM seance_code
WHERE estExamen = 1
	AND client_clientid = 1
;

### 3.  Sélectionner le nom du client qui a le plus grand nombre d’erreurs commises

SELECT clientid, nom, prenom, sum(nombreFautes) as nb_fautes_total
FROM client
INNER JOIN seance_code ON client_clientid = clientid
GROUP BY clientid
ORDER BY nb_fautes_total desc
LIMIT 1
;

### 4.  Sélectionner le nom du client qui a le plus petit nombre d’erreurs commises

SELECT clientid, nom, prenom, sum(nombreFautes) as nb_fautes_total
FROM client
INNER JOIN seance_code ON client_clientid = clientid
GROUP BY clientid
ORDER BY nb_fautes_total asc
LIMIT 1
;

### 5.  Sélectionner les intitulés des questions de la série n°1

SELECT intitule
FROM question
INNER JOIN serie_has_question ON question_questionId = questionId
	WHERE serie_serieId = 1
;

### 6.  Sélectionner le nom et le prénom des élèves ayant échoué au moins une fois à l'examen

SELECT nom, prenom
FROM client
INNER JOIN seance_code ON client_clientid = clientid
	WHERE estExamen = 1 AND nombreFautes > 5
;