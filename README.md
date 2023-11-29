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

![Scrutinizer code quality (GitHub/Bitbucket)](https://img.shields.io/scrutinizer/quality/g/:meryemBouikiouch/:Projet_Django_PriceHub_M1/:master)


# Projet Django PriceHub M1

Ce repository contient le code source du projet Django PriceHub M1.

## Description

PriceHub est une plateforme web basée sur Django qui permet de comparer les prix des produits numériques dans différents magasins en ligne. Ce projet a été développé dans le cadre du cours de DevOps en M1 MIAGE a Nanterre Université.

## Installation

Assurez-vous d'avoir Python installé. Clonez ce repository :

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

##### Fonctionnalités principales ::::

# Recherche et sélection de téléphones

L'application permet aux utilisateurs de rechercher des téléphones selon leurs préférences. 
Les utilisateurs ont la possibilité d'effectuer une recherche simple ou avancée. 
La recherche avancée leur permet de filtrer les résultats en fonction de critères tels que le prix, la capacité de la RAM et d'autres spécifications pertinentes. 
Cela permet aux utilisateurs de trouver le téléphone qui correspond le mieux à leurs besoins.

# Comparaison des prix lors des déplacements

Les utilisateurs peuvent saisir les prix des téléphones qu'ils trouvent dans différents magasins. 
Grâce au tableau de bord de l'application, ils peuvent comparer les différences de prix entre les différents endroits visités. 
Cette fonctionnalité aide les utilisateurs à prendre des décisions éclairées en se basant sur les prix disponibles et à se diriger vers l'endroit enregistré sur leur tableau de bord pour effectuer leur achat.

# À venir

Nous travaillons actuellement sur deux autres fonctionnalités pour améliorer encore l'expérience des utilisateurs. Restez à l'écoute pour les prochaines mises à jour !







