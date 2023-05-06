# Exercices avec la base de données MySQL `beer`

### 1. Quels sont les tickets qui comportent l’article d’ID 500, afficher le numéro de ticket uniquement ?

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

### 2. Afficher les tickets du 15/01/2014.

SELECT
    numero_ticket, date_vente
FROM
    ticket
WHERE
    ticket.DATE_VENTE LIKE '2014-01-15%'
;
-- NUMERO_TICKET, DATE_VENTE
-- 37	2014-01-15 00:00:00

### 3. Afficher les tickets émis du 15/01/2014 et le 17/01/2014.

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

### 4. Editer la liste des articles apparaissant à 50 et plus exemplaires sur un ticket.

select distinct article.ID_ARTICLE, NOM_ARTICLE from article
join ventes on ventes.ID_ARTICLE = article.ID_ARTICLE
where ventes.QUANTITE >= 50
order by ID_ARTICLE
;
-- 1090 row(s) returned

### 5. Quelles sont les tickets émis au mois de mars 2014.

SELECT
    NUMERO_TICKET
FROM
    ticket
WHERE
    DATE_VENTE LIKE '2014-03%'
;
-- 78 row(s) returned	0,000 sec / 0,000 sec

### 6. Quelles sont les tickets émis entre les mois de mars et avril 2014 ?

SELECT
    NUMERO_TICKET, DATE_VENTE
FROM
    ticket
WHERE
    ticket.DATE_VENTE BETWEEN '2014-03-01' AND '2014-04-30'
;
-- 166 row(s) returned	0,000 sec / 0,000 sec

### 7. Quelles sont les tickets émis au mois de mars et juin 2014 ?

SELECT
    NUMERO_TICKET, DATE_VENTE
FROM
    ticket
WHERE
    MONTH(ticket.DATE_VENTE) IN (3 , 6)
        AND YEAR(ticket.DATE_VENTE) = 2014
;
-- 174 row(s) returned	0,000 sec / 0,000 sec

### 8. Afficher la liste des bières classée par couleur. (Afficher l’id et le nom)

SELECT
    ID_ARTICLE, NOM_ARTICLE
FROM
    article
ORDER BY id_couleur ASC , ID_ARTICLE ASC
;
-- 3922 row(s) returned	0,000 sec / 0,000 sec

### 9. Afficher la liste des bières n’ayant pas de couleur. (Afficher l’id et le nom)

SELECT
    ID_ARTICLE, NOM_ARTICLE
FROM
    article
WHERE
    id_couleur IS NULL
ORDER BY id_couleur ASC , ID_ARTICLE ASC
;
-- 706 rows

### 10. Lister pour chaque ticket la quantité totale d’articles vendus. (Classer par quantité décroissante)

SELECT
    NUMERO_TICKET, SUM(QUANTITE)
FROM
    ventes
GROUP BY NUMERO_TICKET
ORDER BY NUMERO_TICKET ASC
;
-- 4502 rows

### 11. Lister chaque ticket pour lequel la quantité totale d’articles vendus est supérieure à 500. (Classer par quantité décroissante)

SELECT
    NUMERO_TICKET, SUM(QUANTITE) AS qte_totale
FROM
    ventes
GROUP BY NUMERO_TICKET
HAVING qte_totale > 500
ORDER BY qte_totale DESC
;
-- 1026 rows

### 12. Lister chaque ticket pour lequel la quantité totale d’articles vendus est supérieure à 500. On exclura du total, les ventes ayant une quantité supérieure à 50 (classer par quantité décroissante)

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

### 13. Lister les bières de type ‘Trappiste’. (id, nom de la bière, volume et titrage)

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

### 14. Lister les marques de bières du continent ‘Afrique’

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

### 15. Lister les bières du continent ‘Afrique’

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

### 16. Lister les tickets (année, numéro de ticket, montant total payé). En sachant que le prix de vente est égal au prix d’achat augmenté de 15% et que l’on n’est pas assujetti à la TVA.

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

### 17. Donner le C.A. par année.

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

### 18. Lister les quantités vendues de chaque article pour l’année 2016.

SELECT
    ID_ARTICLE,
    sum(QUANTITE) AS "qté vendue de chaque art"
FROM
    ventes
WHERE ANNEE = 2016
GROUP BY ANNEE, ID_ARTICLE
;
-- 3922 rows

### 19. Lister les quantités vendues de chaque article pour les années 2014,2015,2016.

SELECT
    ID_ARTICLE,
    sum(QUANTITE) AS "qté vendue de chaque art"
FROM
    ventes
WHERE ANNEE IN (2014, 2015, 2016)
GROUP BY ANNEE, ID_ARTICLE
;
-- 11197 rows

### 20. Lister les articles qui n’ont fait l’objet d’aucune vente en 2014.

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

### 21. Coder de 3 manières différentes la requête suivante : Lister les pays qui fabriquent des bières de type ‘Trappiste’.

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

### 22. Lister les tickets sur lesquels apparaissent un des articles apparaissant aussi sur le ticket 2014-856 (le ticket 856 de l’année 2014).

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

### 23. Lister les articles ayant un degré d’alcool plus élevé que la plus forte des trappistes.

SELECT ID_ARTICLE
FROM article
WHERE titrage > (
	SELECT MAX(TITRAGE) as "la plus forte des trappistes"
	FROM article
	JOIN type USING(ID_TYPE)
	WHERE NOM_TYPE = 'Trappiste'
)
;
-- 74 rows

### 24. Éditer les quantités vendues pour chaque couleur en 2014.

SELECT
    ID_Couleur,
    NOM_COULEUR,
    sum(QUANTITE) as "quantités vendues pour chaque couleur en 2014"
FROM article
JOIN couleur USING(ID_Couleur)
JOIN ventes USING(ID_ARTICLE)
	WHERE ANNEE = 2014
GROUP BY ID_Couleur, NOM_COULEUR
;
-- 4 row(s) in 0,031 sec
-- ID_Couleur, NOM_COULEUR, quantités vendues pour chaque couleur en 2014
-- 1           Ambrée       31427
-- 2           Blanche      14416
-- 3           Blonde       72569
-- 4           Brune        49842

### 25. Donner pour chaque fabricant, le nombre de tickets sur lesquels apparait un de ses produits en 2014.

SELECT
	ID_FABRICANT,
    COUNT(DISTINCT NUMERO_TICKET) as nb_tickets_2014_avec_articles_du_fabricant
FROM fabricant
JOIN (
	SELECT DISTINCT ID_FABRICANT, article.ID_ARTICLE
	FROM fabricant
	JOIN marque USING(ID_FABRICANT)
	JOIN article USING(ID_marque)
) articles_par_fabricant USING(ID_FABRICANT)
JOIN ventes USING(ID_ARTICLE)
	WHERE ANNEE = 2014
GROUP BY ID_FABRICANT
;
--
SELECT DISTINCT
    ID_FABRICANT,
    COUNT(DISTINCT NUMERO_TICKET) as nb_tickets_2014_avec_articles_du_fabricant
FROM fabricant
JOIN marque USING(ID_FABRICANT)
JOIN article USING(ID_marque)
JOIN ventes USING(ID_ARTICLE)
	WHERE ANNEE = 2014
GROUP BY ID_FABRICANT
;
-- ID_FABRICANT, nb_tickets_2014_avec_articles_du_fabricant
-- 1             208
-- 2             33
-- 3             2
-- 4             61
-- 5             162
-- 6             26
-- 7             26
-- 8             35
-- 9             27
-- 10            13

### 26. Donner l’ID, le nom, le volume et la quantité vendue des 20 articles les plus vendus en 2016.

SELECT ID_ARTICLE, NOM_ARTICLE, VOLUME, SUM(QUANTITE) as quantite_totale
FROM article
JOIN ventes USING(ID_ARTICLE)
	WHERE ANNEE = 2016
GROUP BY ID_ARTICLE
ORDER BY quantite_totale desc
LIMIT 20
;
-- ID_ARTICLE,  NOM_ARTICLE,                     VOLUME,  quantite_totale
-- 3192         Cuvée Spéciale Cuvée des Trolls  75       597
-- 3631         Home                             75       596
-- 2304         Damruz                           75       581
-- 3850         Robust Porter                    75       576
-- 1469         Lagaille Rouquinette             33       551
-- 1844         Twin Peaks                       33       540
-- 86           Desperados                       33       539
-- 2158         Japan Pale Ale                   75       537
-- 1477         Lutine Blonde (la)               33       518
-- 2248         Waterloo Rossa                   75       517
-- 162          Volpina                          33       516
-- 2749         Salève Weizen                    75       512
-- 3588         Trappe Puur (la)                 75       502
-- 1258         Smoked Rye IPA                   33       500
-- 1294         Fort Indian Pale Ale             33       499
-- 3526         Stout 8                          75       499
-- 768          Mastoc                           33       496
-- 2305         Hini Du                          75       491
-- 1110         Mamouche                         33       489
-- 3789         Methusalem                       75       488

### 27. Donner l’ID, le nom, le volume et la quantité vendue des 5 ‘Trappistes’ les plus vendus en 2016.

SELECT ID_ARTICLE, NOM_ARTICLE, VOLUME, SUM(QUANTITE) as quantite_totale
FROM article
JOIN ventes USING(ID_ARTICLE)
JOIN type USING(id_type)
WHERE ANNEE = 2016
	AND NOM_TYPE = 'Trappiste'
GROUP BY ID_ARTICLE
ORDER BY quantite_totale desc
LIMIT 5
;
-- ID_ARTICLE,  NOM_ARTICLE,      VOLUME,  quantite_totale
-- 3588         Trappe Puur (la)  75       502
-- 2100         Achel Blonde      75       436
-- 120          Chimay Première   33       393
-- 2101         Achel Brune       75       371
-- 2104         Rochefort 6       75       357

### 28. Donner l’ID, le nom, le volume et les quantités vendues en 2015 et 2016, des bières dont les ventes ont été stables. (Moins de 1% de variation)

SELECT
	ID_ARTICLE, NOM_ARTICLE, VOLUME,
    t2015.quantite_vendue AS quantite_vendue_2015,
    t2016.quantite_vendue AS quantite_vendue_2016,
	CONCAT(ROUND((t2016.quantite_vendue - t2015.quantite_vendue) / t2015.quantite_vendue * 100, 2), ' %') as variation_2015_2016
FROM article
INNER JOIN (
	SELECT ID_ARTICLE, SUM(QUANTITE) as quantite_vendue
	FROM article
	JOIN ventes USING(ID_ARTICLE)
		WHERE ANNEE = 2015
	GROUP BY ID_ARTICLE
	ORDER BY quantite_vendue desc
) t2015 USING(ID_ARTICLE)
INNER JOIN (
	SELECT ID_ARTICLE, SUM(QUANTITE) as quantite_vendue
	FROM article
	JOIN ventes USING(ID_ARTICLE)
		WHERE ANNEE = 2016
	GROUP BY ID_ARTICLE
	ORDER BY quantite_vendue desc
) t2016 USING(ID_ARTICLE)
WHERE ABS((t2016.quantite_vendue - t2015.quantite_vendue) / t2015.quantite_vendue * 100) < 1
ORDER BY variation_2015_2016 asc
;
-- 29 row(s) returned	0.156 sec

### 29. Lister les types de bières suivant l’évolution de leurs ventes entre 2015 et 2016. Classer le résultat par ordre décroissant des performances.

SELECT
    type.id_type,
    nom_type,
    t2015.ca_par_type AS ca_2015,
    t2016.ca_par_type AS ca_2016,
    CONCAT(ROUND((t2016.ca_par_type - t2015.ca_par_type) / t2015.ca_par_type * 100, 2), ' %') AS evolution_2015_2016
FROM type
JOIN (
    SELECT type.id_type, ROUND(SUM(prix_achat * quantite), 2) as ca_par_type
    FROM type
    JOIN article USING(id_type)
    JOIN ventes USING(id_article)
        WHERE annee = 2015
    GROUP BY type.id_type
) t2015 USING(id_type)
JOIN (
    SELECT type.id_type, ROUND(SUM(prix_achat * quantite), 2) as ca_par_type
    FROM type
    JOIN article USING(id_type)
    JOIN ventes USING(id_article)
        WHERE annee = 2016
    GROUP BY type.id_type
) t2016 USING(id_type)
ORDER BY evolution_2015_2016 DESC
;
-- id_type  nom_type          ca_2015    ca_2016     evoLlution_2015_2016
-- 7        Bio               4504.28    8335.02     85.05 %
-- 13       Trappiste         16092.24   28853.96    79.30 %
-- 12       Stout             131278.29  224374.89   70.92 %
-- 11       Pils et Lager     47881.33   81620.75    70.46 %
-- 9        Indian Pale Ale   38119.3    64772.92    69.92 %
-- 3        Ale               180373.43  301881.56   67.36 %
-- 2        Abbaye            53609.00   88798.11    65.64 %
-- 8        Bock              8041.89    13274.37    65.07 %
-- 5        Biere de Garde    8507.11    13953.04    64.02 %
-- 6        Biere de Saison   49028.38   78344.34    59.79 %
-- 4        Barley Wine       10554.02   16385.47    55.25 %
-- 1        Biere Aromatisée  92583.91   143479.24   54.97 %
-- 10       Lambic            20351.49   28555.82    40.31 %

### 30. Existe-t-il des tickets sans vente ?

SELECT DISTINCTROW
    numero_ticket,
    annee
FROM ticket
LEFT JOIN ventes USING(numero_ticket, annee)
    WHERE id_article IS NULL
;
-- numero_ticket  annee
-- 2065           2015
-- 1138           2016
-- 1452           2016

### 31. Lister les produits vendus en 2016 dans des quantités jusqu’à -15% des quantités de l’article le plus vendu.

SELECT
    id_article,
    qte_vendue_en_2016,
    CONCAT(ROUND(varia_rap_au_top_art_2016, 2), ' %') AS varia_rap_au_top_art_2016
FROM (
    SELECT
        id_article,
        qte_vendue_en_2016,
        ((qte_vendue_en_2016 - top_qte_2016) / top_qte_2016 * 100) AS varia_rap_au_top_art_2016
    FROM (
        SELECT
            t_top_art_2016.id AS top_id_art_2016,
            t_top_art_2016.qte AS top_qte_2016,
            ventes.id_article,
            SUM(ventes.quantite) AS qte_vendue_en_2016
        FROM ventes, (
            SELECT
                id_article AS id,
                SUM(quantite) AS qte
            FROM ventes
            WHERE annee = 2016
            GROUP BY id
            ORDER BY qte DESC
            LIMIT 1
        ) t_top_art_2016
        WHERE annee = 2016
        GROUP BY top_id_art_2016, top_qte_2016, ventes.id_article
        ORDER BY qte_vendue_en_2016 DESC
    ) t_qte
) t_varia
WHERE ABS(varia_rap_au_top_art_2016) < 15
;
-- id_article  qte_vendue_en_2016  varia_rap_au_top_art_2016
-- 3192        597                  0.00 %
-- 3631        596                 -0.17 %
-- 2304        581                 -2.68 %
-- 3850        576                 -3.52 %
-- 1469        551                 -7.71 %
-- 1844        540                 -9.55 %
-- 86          539                 -9.72 %
-- 2158        537                 -10.05 %
-- 1477        518                 -13.23 %
-- 2248        517                 -13.40 %
-- 162         516                 -13.57 %
-- 2749        512                 -14.24 %

### 32. Appliquer une augmentation de tarif de 10% pour toutes les bières ‘Trappistes’ de couleur ‘Blonde’



### 33. Mettre à jour le degré d’alcool des toutes les bières n’ayant pas cette information. On y mettra le degré d’alcool de la moins forte des bières du même type et de même couleur.



### 34. Suppression des bières qui ne sont pas des bières ! (Type ‘Bière Aromatisée’)



### 35. Supprimer les tickets qui n’ont pas de ventes.


