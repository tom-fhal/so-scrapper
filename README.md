# Projet de Scraping de StackOverflow (so-scrapper)

# Introduction

Bienvenue dans le projet **so-scrapper** ! Ce projet a pour objectif de récupérer automatiquement des données de StackOverflow, une plateforme très prisée des développeurs pour ses questions-réponses. Le web scraping est une méthode puissante pour collecter des informations de manière rapide et efficace, tout en respectant les normes éthiques et légales en vigueur.

## Fonctionnalités Principales

### Extraction de Données

Le projet se concentre sur l'extraction des éléments suivants :

- **Titres des questions**
- **Liens vers les questions**
- **Descriptions des questions**
- **Tags associés aux questions**
- **Informations sur les auteurs**
- **Dates de publication**
- **Statistiques des questions**

### Stockage des Données

Les données extraites seront stockées dans une base de données MongoDB, assurant une gestion flexible et structurée des informations collectées.

### Analyse des Données

Après la collecte, les données seront analysées pour détecter des tendances dans les technologies, langages de programmation, et autres tags pertinents. Des techniques de traitement du langage naturel (NLP) pourront être employées pour enrichir cette analyse.

### Tests Unitaires

Des tests unitaires robustes sont mis en place pour vérifier :

- La gestion des requêtes HTTP
- L'analyse HTML
- L'extraction des données
- L'insertion des données dans MongoDB

### Parallélisation

Pour améliorer l'efficacité du scraping, des techniques de parallélisation seront utilisées, permettant de traiter plusieurs pages simultanément et de réduire le temps nécessaire à la collecte des données.

### Utilisation de l'API Stack Overflow

Pour une extraction de données plus fiable et respectueuse des règles du site, l'API Stack Overflow sera utilisée en complément ou en remplacement du scraping direct.

### Visualisation des Données

Utilisez le notebook `scrap-notebook.ipynb` pour visualiser les données collectées.

## Vérifications Unitaires

### Importance des Tests

Les tests unitaires sont essentiels pour garantir le bon fonctionnement de chaque composant du projet. Ils assurent que le code fonctionne comme prévu et simplifient la maintenance en détectant rapidement les erreurs.

### Détail des Vérifications

#### `test_beautifulsoup.py`

- **Objectif** : Vérifier la gestion des requêtes HTTP.
- **Description** : Utilise `unittest.mock` pour simuler des requêtes HTTP et vérifier le traitement correct des réponses.

#### `test_get_questions_beautifulsoup.py`

- **Objectif** : Valider l'analyse HTML.
- **Description** : Vérifie que le parseur HTML extrait correctement les éléments nécessaires d'une page HTML statique.

#### `test_extract_question_data.py`

- **Objectif** : Assurer l'extraction des données.
- **Description** : Simule une page HTML de Stack Overflow et vérifie que les données sont correctement extraites et formatées.

## Conclusion

Le projet **so-scrapper** vise à fournir un outil efficace pour extraire et analyser des données de Stack Overflow. Nous nous engageons à respecter les directives et lois en matière de protection des données tout en fournissant un service de qualité. Vos suggestions pour améliorer ce projet sont les bienvenues.
