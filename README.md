[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
Licence: MIT - Ce badge indique que le projet est sous licence MIT.

[![Django Version](https://img.shields.io/badge/Django-4.2.5-blue)](https://docs.djangoproject.com/en/4.2/)
Django Version: 4.2.5 - Ce badge indique l'utilisation de Django version 4.2.5 dans le projet.

[![Python Version](https://img.shields.io/badge/Python-3.11.5-blue.svg)](https://www.python.org/downloads/release/python-3115/)
Python Version: 3.11.5 - Ce badge indique l'utilisation de Python version 3.11.5 dans le projet.

[![SQLite Version](https://img.shields.io/badge/SQLite-3-blue)](https://www.sqlite.org/index.html)
SQLite Version: 3 - Ce badge indique l'utilisation de SQLite version 3 dans le projet.

[![GitHub release](https://img.shields.io/github/v/release/meryemBouikiouch/Projet_Django_PriceHub_M1.svg)](https://github.com/meryemBouikiouch/Projet_Django_PriceHub_M1/releases/tag/V0.2)
GitHub release: V0.2 - Ce badge indique la release V0.2 du projet sur GitHub.

[![Django CI](https://github.com/meryemBouikiouch/Projet_Django_PriceHub_M1/actions/workflows/django.yml/badge.svg)](https://github.com/meryemBouikiouch/Projet_Django_PriceHub_M1/actions/workflows/django.yml)
Django CI: Ce badge indique l'état de la CI (Intégration Continue) pour le framework Django.

![Codacy coverage](https://img.shields.io/codacy/coverage/:Projet_Django_PriceHub_M1)

[![Code Intelligence Status](https://scrutinizer-ci.com/g/meryemBouikiouch/Projet_Django_PriceHub_M1/badges/code-intelligence.svg?b=master)](https://scrutinizer-ci.com/code-intelligence)

# Projet Django PriceHub M1

Ce repository contient le code source du projet Django PriceHub M1.

## Description

PriceHub est une plateforme web basée sur Django qui permet de comparer les prix des produits numériques dans différents magasins en ligne. Ce projet a été développé dans le cadre du cours de DevOps en M1 MIAGE a Nanterre Université.

## Installation

Assurez-vous d'avoir Python installé. 

Clonez ce repository :

git clone https://github.com/meryemBouikiouch/Projet_Django_PriceHub_M1.git

Installez les dépendances :

cd Projet_Django_PriceHub_M1
pip install -r requirements.txt

Configuration : 

Renommez le fichier .env.example en .env.
Remplissez les informations nécessaires dans le fichier .env.

Utilisation :

Appliquer les migrations : python manage.py migrate
Lancer le serveur de développement: python manage.py runserver

Ce projet est sous licence MIT

# Fonctionnalités principales ::::

### Recherche et sélection de téléphones

L'application permet aux utilisateurs de rechercher des téléphones selon leurs préférences. 
Les utilisateurs ont la possibilité d'effectuer une recherche simple ou avancée. 
La recherche avancée leur permet de filtrer les résultats en fonction de critères tels que le prix, la capacité de la RAM et d'autres spécifications pertinentes. 
Cela permet aux utilisateurs de trouver le téléphone qui correspond le mieux à leurs besoins.

### Recherche d'offres en se déplaçant dans les magasins de téléphones :
L'utilisateur se déplace physiquement dans différents endroits pour trouver le téléphone qu'il souhaite acheter. Pendant ses déplacements, il collecte des informations sur les prix de divers téléphones dans les magasins qu'il visite. En utilisant l'application, il peut facilement entrer ces données dans son tableau de bord dédié. Cette approche proactive permet à l'utilisateur de comparer aisément les différences de prix entre les différents endroits visités. Ainsi, il peut prendre des décisions plus éclairées sur l'achat en se basant sur les informations actualisées en temps réel. En ayant l'endroit déjà enregistré sur son tableau de bord, le processus d'achat est simplifié et optimisé pour l'utilisateur.

### Ajout d'une fonctionnalité de Liste de souhaits :

Intégrer la possibilité pour les utilisateurs de créer une liste de souhaits d'achat afin de se rappeler des articles qu'ils souhaitent acheter lors de leurs sorties.
Élargir les catégories au-delà des téléphones, inclure d'autres types de produits.
Implémenter une fonction de clôture des souhaits, permettant aux utilisateurs de marquer un souhait comme accompli lorsqu'ils ont effectivement effectué l'achat.

### Fonctionnalité d'ajout/modification de téléphones :

Autoriser les utilisateurs à ajouter manuellement un téléphone s'il n'est pas répertorié dans la base de données.
Permettre la modification du prix d'un téléphone, en particulier lorsque l'utilisateur constate des changements de prix lors de ses visites en magasin.
Mettre en place un système pour actualiser la base de données des téléphones en fonction des modifications apportées par les utilisateurs.

### Création de groupes et collaboration :

Offrir la possibilité aux utilisateurs de créer des groupes avec d'autres personnes partageant le même souhait d'achat.
Faciliter la communication au sein du groupe pour discuter des stratégies de recherche de prix et de l'optimisation des offres.
Autoriser chaque membre à noter et à ajouter des lieux visités dans son historique, avec le souhait d'achat et le prix trouvé.
Faciliter l'accès à l'historique des membres du groupe pour permettre une comparaison et une recherche collaborative des meilleures offres.

### Organisation de Shopping Meetings (Groupes de Sorties)

Les utilisateurs ont désormais la possibilité de créer des Shopping Meetings, des groupes réunissant des individus partageant un même désir. Ces groupes permettent de planifier des sorties communes afin de visiter des lieux correspondant à leurs souhaits, tout en effectuant des achats ensemble. L'objectif est de favoriser l'entraide dans les choix d'achat et de dénicher les meilleures offres disponibles en magasin.



