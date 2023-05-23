# Installer un petit cluster Hadoop local

## 0. Prérequis

* installer Docker
* si sous Windows : installer WSL 2

## 1. Télécharger l'image Docker `liliasfaxi/spark-hadoop:hv-2.7.2`

> Ubuntu image with Hadoop (2.7.2), Spark (2.2.1), Kafka (2.11-1.0.2) and HBase (1.4.8)

```bash
docker pull liliasfaxi/spark-hadoop:hv-2.7.2
```

## 2. Créer un réseau de type pont et nommé `hadoopnet`

```bash
docker network create --driver=bridge hadoopnet
```
```bash
1351c1d0c553319e7e16e5fe0e344b03ceb92dc099b7b2139b36648a6c3d2a80
```

## 3. Déployer le container `hadoop-master`

* Le noeud *master* a plus de ports (quatre) que n'en a un noeud *slave* (un port) :
  * un pour communiquer avec l'utilisateur,
  * un pour diffuser les ordres concernant les tâches de stockage,
  * un pour diffuser les ordres concernant les tâches de calcul,
  * un pour communiquer avec le gestionnaire de ressources [Hadoop YARN](https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/YARN.html) (à ne pas confondre avec un autre [Yarn](https://yarnpkg.com) — un gestionnaire de paquets de l'écosystème node.js).

* Le noeud *master* reste, malgré son nom, un noeud comme un autre — jusqu'à ce que l'action de démarrer l'environnement Hadoop dessus le désignera automatiquement comme le noeud principal.

```bash
docker run -itd --network=hadoopnet -p 50070:50070 -p 8088:8088 -p 7077:7077 -p 16010:16010 --name hadoop-master --hostname hadoop-master liliasfaxi/spark-hadoop:hv-2.7.2
```

## 4. Déployer les containers `hadoop-slave1` et `hadoop-slave2`

```bash
docker run -itd --network=hadoopnet -p 8040:8042 --name hadoop-slave1 --hostname hadoop-slave1 liliasfaxi/spark-hadoop:hv-2.7.2
```
```bash
docker run -itd --network=hadoopnet -p 8041:8042 --name hadoop-slave2 --hostname hadoop-slave2 liliasfaxi/spark-hadoop:hv-2.7.2
```

## 5. Vérifier les containers qui tournent

Il y a normalement trois containers qui tournent :

```bash
docker ps
```
```bash
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS          PORTS                                                                                                NAMES
6d51e418b50c   liliasfaxi/spark-hadoop:hv-2.7.2   "sh -c 'service ssh …"   22 seconds ago   Up 20 seconds   0.0.0.0:8041->8042/tcp                                                                               hadoop-worker2
a0321845dda3   liliasfaxi/spark-hadoop:hv-2.7.2   "sh -c 'service ssh …"   4 minutes ago    Up 4 minutes    0.0.0.0:8040->8042/tcp                                                                               hadoop-worker1
9d9988769032   liliasfaxi/spark-hadoop:hv-2.7.2   "sh -c 'service ssh …"   25 minutes ago   Up 25 minutes   0.0.0.0:7077->7077/tcp, 0.0.0.0:8088->8088/tcp, 0.0.0.0:16010->16010/tcp, 0.0.0.0:50070->50070/tcp   hadoop-master
```

## 6. Copier le fichier texte `exemple.txt` depuis la machine hôte vers le container

```bash
docker cp ./exemple.txt hadoop-master:/root/
```
```
Successfully copied 10.8kB to hadoop-master:/root/
```

## 7. Se connecter à la machine du container `hadoop-master`:

```bash
docker exec -it hadoop-master /bin/bash
```

## 7.1. Lancer `hadoop`

```bash
./start-hadoop.sh
```
```
Starting namenodes on [hadoop-master]
hadoop-master: Warning: Permanently added 'hadoop-master,172.18.0.2' (ECDSA) to the list of known hosts.
hadoop-master: starting namenode, logging to /usr/local/hadoop/logs/hadoop-root-namenode-hadoop-master.out
hadoop-slave2: Warning: Permanently added 'hadoop-slave2,172.18.0.4' (ECDSA) to the list of known hosts.
hadoop-slave1: Warning: Permanently added 'hadoop-slave1,172.18.0.3' (ECDSA) to the list of known hosts.
hadoop-slave2: datanode running as process 62. Stop it first.
hadoop-slave1: datanode running as process 62. Stop it first.
Starting secondary namenodes [0.0.0.0]
0.0.0.0: Warning: Permanently added '0.0.0.0' (ECDSA) to the list of known hosts.
0.0.0.0: starting secondarynamenode, logging to /usr/local/hadoop/logs/hadoop-root-secondarynamenode-hadoop-master.out


starting yarn daemons
starting resourcemanager, logging to /usr/local/hadoop/logs/yarn--resourcemanager-hadoop-master.out
hadoop-slave1: Warning: Permanently added 'hadoop-slave1,172.18.0.3' (ECDSA) to the list of known hosts.
hadoop-slave2: Warning: Permanently added 'hadoop-slave2,172.18.0.4' (ECDSA) to the list of known hosts.
hadoop-slave1: nodemanager running as process 173. Stop it first.
hadoop-slave2: nodemanager running as process 173. Stop it first.
```

## 7.2. Créer un dossier distribué, nommé `input`

```bash
# -mkdir [-p] <path> ... :
#   Create a directory in specified location.
#   -p  Do not fail if the directory already exists
hadoop fs -mkdir -p input
```

Pour voir le dossier créé :
```bash
hadoop fs -ls
```
```
Found 1 items
drwxr-xr-x   - root supergroup          0 2023-05-22 14:37 input
```
```bash
# cette commande ne verra pas le dossier input :
ls
```

## 7.3. Charger un fichier dans le système distribué HDFS

```bash
# -put [-f] [-p] [-l] <localsrc> ... <dst> :
#   Copy files from the local file system into fs. Copying fails if the file already
#   exists, unless the -f flag is given.
#   Flags:
#   -p  Preserves access and modification times, ownership and the mode.
#   -f  Overwrites the destination if it already exists.
#   -l  Allow DataNode to lazily persist the file to disk. Forces
#          replication factor of 1. This flag will result in reduced
#          durability. Use with care.
hadoop fs -put ./exemple.txt input

# -copyFromLocal [-f] [-p] [-l] <localsrc> ... <dst> :
#   Identical to the -put command.
hadoop fs -copyFromLocal ./exemple.txt input

# -moveFromLocal <localsrc> ... <dst> :
#   Same as -put, except that the source is deleted after it's copied.
hadoop fs -moveFromLocal ./exemple.txt input
```
Pour voir le fichier chargé :
```bash
hadoop fs -ls input
```
```
Found 1 items
-rw-r--r--   2 root supergroup  211312924 2023-05-22 14:37 input/exemple.txt
```
Pour un aperçu du contenu du fichier distribué :
```bash
# pour voir les premières lignes
hadoop fs -cat input/exemple.txt | head

# pour voir les dernières lignes
hadoop fs -tail input/exemple.txt

# autre possibilité de voir les dernières lignes (extrêmement lente)
hadoop fs -cat input/exemple.txt | tail
```

## 8. Copier le JAR depuis la machine hôte vers le container

```bash
docker cp ./WordCount.jar hadoop-master:/root/
```
```
Successfully copied 5.12kB to hadoop-master:/root/
```
```bash
# se connecter au terminal du container si jamais on l'avait quitté
docker exec -it hadoop-master /bin/bash
```

## 9. Exécuter un job de comptage de mots

```bash
hadoop jar ./WordCount.jar WordCount input output
```
Pour voir un aperçu des résultats :
```bash
hadoop fs -cat output/part* | head
```
```
11      1
2004    1
3000    1
Adjani  1
Arvor   1
Au      2
Beaucoup        3
Bedos   1
Bellucci        1
Bernie  1
```
Pour un aperçu trié :
```bash
#   -r, --reverse             reverse the result of comparisons
#   -k, --key=KEYDEF          sort via a key; KEYDEF gives location and type
hadoop fs -cat output/part* | sort -r -k 2 | head
```
```
une     9
en      9
ces     9
au      9
Tu      9
Une     8
L       8
plus    7
pas     6
dans    6
```