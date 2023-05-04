# Exercices avec la base de données MySQL `beer`

### 1. Quels sont les tickets qui comportent l’article d’ID 500, afficher le numéro de ticket uniquement ?
```sql
SELECT DISTINCT
    ticket.NUMERO_TICKET
FROM
    ticket
        JOIN
    ventes ON ventes.NUMERO_TICKET = ticket.NUMERO_TICKET
WHERE
    ventes.ID_ARTICLE = 500
;
-- NUMERO_TICKET
-- 36
-- 264
-- 290
-- 315
-- 349
-- 423
-- 524
-- 708
-- 763
-- 770
-- 846
-- 871
-- 998
-- 1003
-- 1092
-- 1139
-- 1143
-- 1172
-- 1637
-- 1892
-- 1980
-- 2626
-- 3004
-- 3479
```
### 2. Afficher les tickets du 15/01/2014.
```sql
SELECT
    numero_ticket, date_vente
FROM
    ticket
WHERE
    ticket.DATE_VENTE LIKE '2014-01-15%'
;
-- NUMERO_TICKET, DATE_VENTE
-- 37	2014-01-15 00:00:00

```
### 3. Afficher les tickets émis du 15/01/2014 et le 17/01/2014.
```sql
SELECT
    NUMERO_TICKET, DATE_VENTE
FROM
    ticket
WHERE
    ticket.DATE_VENTE in ('2014-01-15%', '2014-01-17%')
;
-- NUMERO_TICKET, DATE_VENTE
-- 37	2014-01-15 00:00:00
-- 38	2014-01-17 00:00:00
-- 39	2014-01-17 00:00:00
-- 40	2014-01-17 00:00:00
```
### 4. Editer la liste des articles apparaissant à 50 et plus exemplaires sur un ticket.
```sql
select distinct article.ID_ARTICLE, NOM_ARTICLE from article
join ventes on ventes.ID_ARTICLE = article.ID_ARTICLE
where ventes.QUANTITE >= 50
order by ID_ARTICLE
;
-- 1090 row(s) returned
```
### 5. Quelles sont les tickets émis au mois de mars 2014.
```sql
SELECT
    NUMERO_TICKET
FROM
    ticket
WHERE
    DATE_VENTE LIKE '2014-03%'
;
-- 78 row(s) returned	0,000 sec / 0,000 sec
```
### 6. Quelles sont les tickets émis entre les mois de mars et avril 2014 ?
```sql
SELECT
    NUMERO_TICKET, DATE_VENTE
FROM
    ticket
WHERE
    ticket.DATE_VENTE BETWEEN '2014-03-01' AND '2014-04-30'
;
-- 166 row(s) returned	0,000 sec / 0,000 sec
```
### 7. Quelles sont les tickets émis au mois de mars et juin 2014 ?
```sql
SELECT
    NUMERO_TICKET, DATE_VENTE
FROM
    ticket
WHERE
    MONTH(ticket.DATE_VENTE) IN (3 , 6)
        AND YEAR(ticket.DATE_VENTE) = 2014
;
-- 174 row(s) returned	0,000 sec / 0,000 sec
```
### 8. Afficher la liste des bières classée par couleur. (Afficher l’id et le nom)
```sql
SELECT
    ID_ARTICLE, NOM_ARTICLE
FROM
    article
ORDER BY id_couleur ASC , ID_ARTICLE ASC
;
-- 3922 row(s) returned	0,000 sec / 0,000 sec
```
### 9. Afficher la liste des bières n’ayant pas de couleur. (Afficher l’id et le nom)
```sql
SELECT
    ID_ARTICLE, NOM_ARTICLE
FROM
    article
WHERE
    id_couleur IS NULL
ORDER BY id_couleur ASC , ID_ARTICLE ASC
;
-- 706 rows
```
### 10. Lister pour chaque ticket la quantité totale d’articles vendus. (Classer par quantité décroissante)
```sql
SELECT
    NUMERO_TICKET, SUM(QUANTITE)
FROM
    ventes
GROUP BY NUMERO_TICKET
ORDER BY NUMERO_TICKET ASC
;
-- 4502 rows
```
### 11. Lister chaque ticket pour lequel la quantité totale d’articles vendus est supérieure à 500. (Classer par quantité décroissante)
```sql
SELECT
    NUMERO_TICKET, SUM(QUANTITE) AS qte_totale
FROM
    ventes
GROUP BY NUMERO_TICKET
HAVING qte_totale > 500
ORDER BY qte_totale DESC
;
-- 1026 rows
```
### 12. Lister chaque ticket pour lequel la quantité totale d’articles vendus est supérieure à 500. On exclura du total, les ventes ayant une quantité supérieure à 50 (classer par quantité décroissante)
```sql
SELECT
    NUMERO_TICKET, SUM(QUANTITE) AS qte_totale
FROM
    ventes
WHERE
    QUANTITE < 50
GROUP BY NUMERO_TICKET
HAVING qte_totale > 500
ORDER BY qte_totale DESC
;
-- 901 rows
```
### 13. Lister les bières de type ‘Trappiste’. (id, nom de la bière, volume et titrage)
```sql
SELECT
    ID_ARTICLE, NOM_ARTICLE, VOLUME, TITRAGE
FROM
    article
        JOIN
    type ON article.ID_TYPE = type.ID_TYPE
WHERE
    NOM_TYPE = 'Trappiste'
;
-- 48 rows
```
### 14. Lister les marques de bières du continent ‘Afrique’
```sql
SELECT
    ID_MARQUE, NOM_MARQUE
FROM
    marque
        JOIN
    pays ON marque.ID_PAYS = pays.ID_PAYS
        JOIN
    continent ON pays.ID_CONTINENT = continent.ID_CONTINENT
WHERE
    NOM_CONTINENT = 'Afrique'
;
-- 3 rows
```
### 15. Lister les bières du continent ‘Afrique’
```sql
SELECT
    ID_ARTICLE, NOM_ARTICLE
FROM
    article
        JOIN
    marque ON article.ID_MARQUE = marque.ID_MARQUE
        JOIN
    pays ON marque.ID_PAYS = pays.ID_PAYS
        JOIN
    continent ON pays.ID_CONTINENT = continent.ID_CONTINENT
WHERE
    NOM_CONTINENT = 'Afrique'
;
-- 6 rows (3 duplicates)
```
### 16. Lister les tickets (année, numéro de ticket, montant total payé). En sachant que le prix de vente est égal au prix d’achat augmenté de 15% et que l’on n’est pas assujetti à la TVA.
```sql
SELECT
    ANNEE,
    NUMERO_TICKET,
    SUM(QUANTITE * PRIX_ACHAT * 1.15) AS montant_total_paye
FROM
    ventes
        JOIN
    article ON ventes.ID_ARTICLE = article.ID_ARTICLE
GROUP BY ANNEE , NUMERO_TICKET
;
-- 8263 rows in 0.016
SELECT
    ANNEE,
    NUMERO_TICKET,
    SUM(QUANTITE * PRIX_ACHAT * 1.15) AS montant_total_paye
FROM
    ventes
JOIN article USING(ID_ARTICLE)
GROUP BY ANNEE , NUMERO_TICKET
;
-- 8263 rows in 0.016
```
### 17. Donner le C.A. par année.
```sql
SELECT
    ANNEE,
    REPLACE(
        FORMAT(
            SUM(QUANTITE * PRIX_ACHAT * 1.15), 2, 'en_US'
        ), ',', ' '
    ) AS ca_annee
FROM
    ventes
        JOIN
    article ON ventes.ID_ARTICLE = article.ID_ARTICLE
GROUP BY ANNEE
;
-- 3 rows
-- ANNEE, ca_annee
-- 2014   585 094.47
-- 2015   1 513 663.13
-- 2016   2 508 162.52
```
### 18. Lister les quantités vendues de chaque article pour l’année 2016.
```sql
SELECT
    ID_ARTICLE,
    sum(QUANTITE) AS "qté vendue de chaque art"
FROM
    ventes
WHERE ANNEE = 2016
GROUP BY ANNEE, ID_ARTICLE
;
-- 3922 rows
```
### 19. Lister les quantités vendues de chaque article pour les années 2014,2015,2016.
```sql
SELECT
    ID_ARTICLE,
    sum(QUANTITE) AS "qté vendue de chaque art"
FROM
    ventes
WHERE ANNEE IN (2014, 2015, 2016)
GROUP BY ANNEE, ID_ARTICLE
;
-- 11197 rows
```
### 20. Lister les articles qui n’ont fait l’objet d’aucune vente en 2014.
```sql
SELECT ID_ARTICLE, NOM_ARTICLE
FROM article
WHERE ID_ARTICLE NOT IN (
	SELECT
        ID_ARTICLE
	FROM ventes
	WHERE ANNEE = 2014
	GROUP BY ANNEE , ID_ARTICLE
)
;
-- 540 rows in 0.016
SELECT article.ID_ARTICLE, NOM_ARTICLE
FROM article
LEFT JOIN (
	SELECT
        ANNEE,
		ID_ARTICLE,
		SUM(QUANTITE) AS 'qté vendue de chaque art'
    FROM ventes
    WHERE ANNEE = 2014
    GROUP BY ANNEE , ID_ARTICLE
) t1 USING(ID_ARTICLE)
WHERE t1.ID_ARTICLE IS NULL
;
-- 540 rows in 0.015
```
### 21. Coder de 3 manières différentes la requête suivante : Lister les pays qui fabriquent des bières de type ‘Trappiste’.
```sql
SELECT DISTINCT NOM_PAYS
FROM pays
JOIN marque USING(ID_PAYS)
JOIN article USING(ID_MARQUE)
JOIN type USING(ID_TYPE)
WHERE NOM_TYPE = 'Trappiste'
;
-- 3 row(s)
SELECT NOM_PAYS
FROM pays
WHERE ID_PAYS in (
	SELECT ID_PAYS
	FROM marque
	WHERE ID_MARQUE IN (
		SELECT DISTINCT ID_MARQUE
		FROM article
		WHERE ID_TYPE = (
			SELECT id_type
			FROM type
			WHERE NOM_TYPE IN 'Trappiste'
		)
	)
)
;
-- 3 rows
```
### 22. Lister les tickets sur lesquels apparaissent un des articles apparaissant aussi sur le ticket 2014-856 (le ticket 856 de l’année 2014).
```sql
SELECT DISTINCT NUMERO_TICKET
FROM ventes
WHERE ID_ARTICLE IN (
	SELECT ID_ARTICLE
	FROM ventes
	WHERE ANNEE = 2014
		AND NUMERO_TICKET = 856
)
;
-- 37 rows
```
### 23. Lister les articles ayant un degré d’alcool plus élevé que la plus forte des trappistes.
```sql
SELECT ID_ARTICLE
FROM article
WHERE titrage > (
	SELECT max(TITRAGE) as "la plus forte des trappistes"
	FROM article
	JOIN type USING(ID_TYPE)
	WHERE NOM_TYPE = 'Trappiste'
)
;
-- 74 rows
```
### 24. Éditer les quantités vendues pour chaque couleur en 2014.
```sql

```
### 25. Donner pour chaque fabricant, le nombre de tickets sur lesquels apparait un de ses produits en 2014.
```sql

```
### 26. Donner l’ID, le nom, le volume et la quantité vendue des 20 articles les plus vendus en 2016.
```sql

```
### 27. Donner l’ID, le nom, le volume et la quantité vendue des 5 ‘Trappistes’ les plus vendus en 2016.
```sql

```
### 28. Donner l’ID, le nom, le volume et les quantités vendues en 2015 et 2016, des bières dont les ventes ont été stables. (Moins de 1% de variation)
```sql

```
### 29. Lister les types de bières suivant l’évolution de leurs ventes entre 2015 et 2016. Classer le résultat par ordre décroissant des performances.
```sql

```
### 30. Existe-t-il des tickets sans vente ?
```sql

```
### 31. Lister les produits vendus en 2016 dans des quantités jusqu’à -15% des quantités de l’article le plus vendu.
```sql

```
### 32. Appliquer une augmentation de tarif de 10% pour toutes les bières ‘Trappistes’ de couleur ‘Blonde’
```sql

```
### 33. Mettre à jour le degré d’alcool des toutes les bières n’ayant pas cette information. On y mettra le degré d’alcool de la moins forte des bières du même type et de même couleur.
```sql

```
### 34. Suppression des bières qui ne sont pas des bières ! (Type ‘Bière Aromatisée’)
```sql

```
### 35. Supprimer les tickets qui n’ont pas de ventes.
```sql

```