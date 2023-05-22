## Installer Hadoop & Spark en local

### 0. Prérequis

* installer Docker
* installer WSL 2

### 1. Télécharger l'image Docker `liliasfaxi/spark-hadoop:hv-2.7.2`

> Ubuntu image with Hadoop (2.7.2), Spark (2.2.1), Kafka (2.11-1.0.2) and HBase (1.4.8)

```bash
docker pull liliasfaxi/spark-hadoop:hv-2.7.2
```
```bash
hv-2.7.2: Pulling from liliasfaxi/spark-hadoop
1be7f2b886e8: Pull complete
6fbc4a21b806: Pull complete
c71a6f8e1378: Pull complete
4be3072e5a37: Pull complete
06c6d2f59700: Pull complete
b8606274051a: Pull complete
8176485c06ce: Pull complete
f3a132dac987: Pull complete
a3c7183d2677: Pull complete
d010f061a722: Pull complete
d81c164d96f9: Pull complete
d8d441090d24: Pull complete
7c12d721deef: Pull complete
091d1ad175e0: Pull complete
793a639c13bb: Pull complete
040b0d6351fa: Pull complete
262437b95da7: Pull complete
Digest: sha256:56f4243e1b22684301e611df6e724605846f4ddbaf8d8884ef841fc5f2e48a70
Status: Downloaded newer image for liliasfaxi/spark-hadoop:hv-2.7.2
docker.io/liliasfaxi/spark-hadoop:hv-2.7.2
```

### 2. Créer un réseau de type pont et nommé `hadoopnet`

```bash
docker network create --driver=bridge hadoopnet
```
```bash
1351c1d0c553319e7e16e5fe0e344b03ceb92dc099b7b2139b36648a6c3d2a80
```

### 3. Déployer le container `hadoop-master`

* Le noeud *master* a plus de ports qu'un noeud *worker*
* Le noeud *master* n'est défini comme tel que parce que ce sera celui sur lequel on démarrera l'environnement Hadoop

```bash
docker run -itd --network=hadoopnet -p 50070:50070 -p 8088:8088 -p 7077:7077 -p 16010:16010 --name hadoop-master --hostname hadoop-master liliasfaxi/spark-hadoop:hv-2.7.2
```
```bash
9d9988769032673a61d51b1c5914f61c84d61b59ccd627c23821a8d40f028b2c
```

### 4. Déployer les containers `hadoop-slave1` et `hadoop-slave2`

```bash
docker run -itd --network=hadoopnet -p 8040:8042 --name hadoop-slave1 --hostname hadoop-slave1 liliasfaxi/spark-hadoop:hv-2.7.2
```
```bash
a0321845dda35d2bb39a9b44fc8dbda8af5b1aa5ad2e7bf74074e45a89350721
```
```bash
docker run -itd --network=hadoopnet -p 8041:8042 --name hadoop-slave2 --hostname hadoop-slave2 liliasfaxi/spark-hadoop:hv-2.7.2
```
```bash
6d51e418b50cb310869433ed7ae0aa43ccb0b41489986e9791d3771584bdd417
```

### 5. Vérifier les containers qui tournent

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

### 6. Se connecter à la machine du container `hadoop-master`:

```bash
docker exec -it hadoop-master /bin/bash
```
```bash
root@hadoop-master:~#
```

### 7. Lancer `hadoop`

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

### 8. Créer un dossier distribué, nommé `input`

```bash
# -mkdir [-p] <path> ... :
#   Create a directory in specified location.
#   -p  Do not fail if the directory already exists
hadoop fs -mkdir -p input
```

Pour voir le dossier créé :
```bash
# cette commande verra le dossier input :
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

### 9. Charger un fichier dans le système distribué HDFS

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
hadoop fs -put ./purchases.txt input

# -copyFromLocal [-f] [-p] [-l] <localsrc> ... <dst> :
#   Identical to the -put command.
hadoop fs -copyFromLocal ./purchases.txt input

# -moveFromLocal <localsrc> ... <dst> :
#   Same as -put, except that the source is deleted after it's copied.
hadoop fs -moveFromLocal ./purchases.txt input
```
Pour voir le fichier chargé :
```bash
hadoop fs -ls input
```
```
Found 1 items
-rw-r--r--   2 root supergroup  211312924 2023-05-22 14:37 input/purchases.txt
```
Pour voir un aperçu du contenu du fichier distribué :
```bash
# pour voir les premières lignes
hadoop fs -cat input/purchases.txt | head

# pour voir les dernières lignes
hadoop fs -tail input/purchases.txt
```

