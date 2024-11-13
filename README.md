# OUKHEMANOU Mohand-Tahar
# Mastère DATA & IA
# TP Dataset
# [PRS] MIA 26.2

TP Dataset - Création d'un Modèle de Classification.
Par OUKHEMANOU Mohand.

## Informations

Ce projet explore une base de données regroupant des informations sur différents pingouins, issus de plusieurs espèces et vivant sur diverses îles. Pour chaque individu, la base contient des données sur la longueur et la profondeur de leur bec, leur masse corporelle, la longueur de leurs nageoires, leur sexe et l'année de collecte de ces informations.

Dans notre étude, nous nous concentrons exclusivement sur leurs caractéristiques physiques, et nous avons donc exclu les informations sur le sexe et l'année d'observation. Ce dataset a été choisi en raison de mon expérience antérieure dans l'analyse de ces données via différents algorithmes de classification (par exemple, k-means, DBSCAN). J'ai trouvé intéressant de réutiliser ce jeu de données pour construire un modèle de classification.

Cette étude vise également à tester deux hypothèses :
1. L'espèce des pingouins a une influence sur leurs caractéristiques physiques.
2. L'habitat des pingouins (l'île sur laquelle ils vivent) a une influence sur leurs caractéristiques physiques.

En effet, si le modèle basé sur ces caractéristiques obtient un bon score de précision, cela indiquera l'existence d'une corrélation entre l'espèce/l'habitat et les caractéristiques physiques des pingouins. Nous inclurons également les résultats d'une classification k-means pour valider et compléter les résultats obtenus avec les modèles.

## Utilisation

Pour lancer les fichiers python, utiliser la commande : 
    -> python3 nom_du_fichier.py

## Explication

L'objectif de ce projet est de créer un modèle de classification permettant, à partir des caractéristiques physiques d’un pingouin, de prédire son espèce (dataset_specie.py) ou son île d'origine (dataset_island.py).

La classification via k-means permet également de vérifier, en comparant la répartition des données selon les étiquettes (espèce ou île) et les clusters générés par k-means, s'il existe une corrélation significative.

## Résultats

### Modèle de classification par espèce

![decision_tree_specie](https://github.com/user-attachments/assets/86f699e3-04cc-4e14-9f52-7ff4c267229c)

Pour le modèle de prédiction de l'espèce, nous obtenons une précision de 94%. L'importance des caractéristiques est la suivante :
1. Longueur des nageoires : 52%
2. Longueur du bec : 38%
3. Profondeur du bec : 10%
4. Masse corporelle : 0%

Ces résultats suggèrent une corrélation claire entre les caractéristiques physiques et l'espèce des pingouins, en particulier une influence sur la longueur des nageoires et du bec.

### Modèle de classification par île

![decision_tree_island](https://github.com/user-attachments/assets/ccf1f780-bb59-420f-8972-987d59b21e77)

Pour le modèle de prédiction de l'habitat, nous obtenons une précision de 66%. L'importance des caractéristiques est la suivante :
1. Longueur des nageoires : 63%
2. Longueur du bec : 23%
3. Profondeur du bec : 14%
4. Masse corporelle : 0%

Les résultats sont ici plus mitigés et moins significatifs que pour le modèle de classification par espèce, indiquant qu'il n'existe probablement pas de corrélation forte entre les caractéristiques physiques et l'habitat des pingouins.

### Classification k-means

![islands_distrib](https://github.com/user-attachments/assets/c4ea2198-c15e-4dcb-927b-6a4e23a9f670)

![species_distrib](https://github.com/user-attachments/assets/e9190833-f164-4e90-81db-99a1cea6faab)

![k_means](https://github.com/user-attachments/assets/19a31e03-733a-43c6-a99b-d62384ac2298)

Les résultats du clustering k-means corroborent nos observations : les clusters obtenus sont largement alignés avec la répartition des espèces, chaque cluster regroupant majoritairement des pingouins de la même espèce (à quelques exceptions près dues aux bruits). Cela soutient l'hypothèse de la corrélation entre les caractéristiques physiques et l'espèce.
