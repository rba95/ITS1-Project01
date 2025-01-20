# README

Préparation nécessaire avant éxecution

Commencer par mettre à jour votre système 
```
sudo apt update
``` 

## Cloner le répertoire 

Pour commencer vous avez besoin de cloner notre repertoire : 
```
git clone https://github.com/rba95/ITS
```

## Python 

Vérifier la version de votre python :
```
python3 --version

```
Nous utilisons la version **Python 3.12.3**

Installer le package permettant de déployer un environnement virtuel en python pour **isoler nos packages installé** :

```
sudo apt install python3-venv

```

## PostgreSQL 

Installation de PostgreSQL et sa configuration :D

```
sudo apt install postgresql postgresql-contrib

```
Ensuite vérifier si le service démarre bien : 

```
sudo systemctl status postgresql

```
Si il ne démarre pas faite :

```
sudo systemctl start postgresql

```
