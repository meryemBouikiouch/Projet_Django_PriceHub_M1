[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![GitHub release](https://img.shields.io/github/v/release/meryemBouikiouch/Projet_Django_PriceHub_M1.svg)](https://github.com/meryemBouikiouch/Projet_Django_PriceHub_M1/releases/tag/V0.2)

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

##  Création de Budget
Définition de Budget pour des Achats ou Sorties : Permet à l'utilisateur de fixer un budget pour des souhaits spécifiques ou des sorties de shopping planifiées.
Gestion Efficace des Finances : Aide les utilisateurs à contrôler leurs dépenses, en évitant de dépasser leur budget prédéfini.
Fonctionnalités d'Ajout et de Suppression de Budgets : Offre une flexibilité pour ajuster les budgets en fonction des besoins, assurant une gestion optimale des finances.

## Communauté Interactive
Plateforme Collaborative pour Partager des Expériences : Engage les utilisateurs à rejoindre des communautés basées sur des catégories de produits spécifiques.
Création et Participation à des Discussions : Encourage la création de nouveaux sujets et la participation à des débats sur des produits et expériences liés.
Gestion des Contributions : Permet aux utilisateurs de supprimer leurs sujets, offrant un contrôle sur le contenu qu'ils partagent.

## Gestion Dynamique des Groupes
Ajout et Suppression Faciles de Groupes : Permet une gestion flexible des groupes en fonction des intérêts et des souhaits actuels.
Mise à Jour Automatique des Membres : Si un utilisateur marque un souhait comme "clôturé", il est automatiquement retiré du groupe concerné.
Association Pertinente avec les Objectifs : Assure que les membres du groupe sont activement engagés dans des souhaits en cours.

Fonctionnalité des Favoris
Liste Personnalisée de Produits Préférés : Permet aux utilisateurs de marquer et de sauvegarder leurs articles préférés pour un accès rapide ultérieur.
Facilitation de la Consultation et de la Comparaison : Aide à retrouver et comparer facilement les produits favoris sans recherches répétées.

Fonctionnalité d'Invitation
Inviter des Amis à Rejoindre et Participer : Permet d'envoyer des invitations pour s'inscrire sur le site ou pour rejoindre des activités spécifiques.
Renforcement de la Communauté : Favorise l'inscription de nouveaux membres et la collaboration au sein de groupes de shopping ou d'événements spéciaux.

