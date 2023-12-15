[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub release](https://img.shields.io/github/v/release/meryemBouikiouch/Projet_Django_PriceHub_M1.svg)](https://github.com/meryemBouikiouch/Projet_Django_PriceHub_M1/releases/tag/V0.2)

<<<<<<< HEAD
[![Django Version](https://img.shields.io/badge/Django-4.2.5-blue)](https://docs.djangoproject.com/en/4.2/)

[![Python Version](https://img.shields.io/badge/Python-3.11.5-blue.svg)](https://www.python.org/downloads/release/python-3115/)

[![SQLite Version](https://img.shields.io/badge/SQLite-3-blue)](https://www.sqlite.org/index.html)

[![GitHub release](https://img.shields.io/github/v/release/dihiaDR/Projet_Django_PriceHub_M1.svg)](https://github.com/dihiaDR/Projet_Django_PriceHub_M1/releases)
=======
[![Django CI](https://github.com/meryemBouikiouch/Projet_Django_PriceHub_M1/actions/workflows/django.yml/badge.svg)](https://github.com/meryemBouikiouch/Projet_Django_PriceHub_M1/actions/workflows/django.yml)


[![Codacy Badge](https://app.codacy.com/project/badge/Grade/392df07d1f33495fa1261bc10ee4b2df)](https://app.codacy.com/gh/meryemBouikiouch/Projet_Django_PriceHub_M1/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade) 


[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/meryemBouikiouch/Projet_Django_PriceHub_M1/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/meryemBouikiouch/Projet_Django_PriceHub_M1/?branch=master)

[![Build Status](https://scrutinizer-ci.com/g/meryemBouikiouch/Projet_Django_PriceHub_M1/badges/build.png?b=master)](https://scrutinizer-ci.com/g/meryemBouikiouch/Projet_Django_PriceHub_M1/build-status/master)
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

# Fonctionnalités Principales

## Recherche et Sélection de Téléphones

- **Recherche Simple ou Avancée :** Les utilisateurs peuvent rechercher des téléphones avec des filtres avancés tels que le prix et les spécifications.

## Recherche d'Offres en Se Déplaçant dans les Magasins de Téléphones

- **Collecte d'Informations en Déplacement :** Utilisateurs enregistrent les prix de téléphones en se déplaçant.
- **Enregistrement des Données sur l'Application :** Les données sont saisies dans l'application pour comparaison.

## Ajout d'une Fonctionnalité de Liste de Souhaits

- **Création de Liste de Souhaits :** Utilisateurs créent des listes pour se rappeler des articles.
- **Diversification des Catégories :** Inclut différents types de produits pour une liste complète.
- **Fermeture des Souhaits :** Possibilité de marquer un souhait comme accompli après l'achat.

## Fonctionnalité d'Ajout/Modification de Téléphones

- **Ajout Manuel dans la Base de Données :** Utilisateurs ajoutent des téléphones manquants.
- **Modification des Prix :** Ils ajustent les prix lors de changements en magasin.
- **Actualisation de la Base de Données Collaborative :** Les modifications contribuent à une base de données collaborative.

## Création de Groupes et Collaboration

- **Formation de Groupes :** Utilisateurs créent des groupes pour partager des souhaits d'achat.
- **Communication Facilitée :** L'application facilite les discussions sur les prix et les offres.
- **Historique Collaboratif :** Les membres notent les lieux visités et les prix pour des comparaisons collaboratives.

## Organisation de Shopping Meetings (Groupes de Sorties)

- **Création de Shopping Meetings :** Possibilité de planifier des sorties communes.
- **Planification de Sorties Communes :** Les groupes visitent des lieux correspondant à leurs souhaits.
- **Entraide et Découverte des Meilleures Offres :** Favorise l'entraide pour dénicher les meilleures offres.
>>>>>>> 352788c670aef8fa5b2fe4a67e06158b38c68c03
