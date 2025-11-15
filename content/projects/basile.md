---
title: Basile, startup RH de cooptation
date: 2025-03-01
description: Développement fullstack chez une startup RH en plein croissance (rachetée par HelloWork)
keywords:
  - Symfony
  - API Platform
  - Vue.js
  - APIs REST
background: hands.png
logo: logo_basile.jpeg
duration: 3 ans
---

# Basile, développement fullstack chez une startup RH en plein croissance

Développement fullstack sur la solution web de cooptation et mobilité interne de Basile (racheté par HelloWork) pendant 3 ans.
Mon travail pour cette startup s’articulait autour de trois axes: scaling de l'activité, nouvelles fonctionnalités et améliorations de la fiabilité

## Scaling de l'activité (en 3 ans)
- passage de quelques dizaines à plusieurs milliers de candidatures traitées par mois
- emailing: de 2000 à 200 000 newsletters envoyées par mois
- traffic web: de 10 000 à 500 000 visites mensuelles
- en pratique: améliorations des performances sur l'envoi de newsletters (symfony messenger et queues Redis), migration vers API Platform pour augmenter les performances et la solidité du backend, mise en place d'une CI avec une couverture importante de la codebase).

## Nouvelles fonctionnalités
- Conception et développement du hub de connection aux Application Tracking System (ATS), voire plus bas
- Développement de la fonctionnalité pivot de gestion des mobilités internes
- Développement d'un système de planification d'envoi des newsletters

## Fiabilité de la solution
- Mise en place d'une CI et d'une architecture de tests avec couverture importante (fixtures db, mockups API)
- Introduction de design patterns éprouvés dans le backend.
- Introduction de concept de Domain Driven Design (backend).

## Focus sur la fonctionnalité Hub ATS
- Développement d'un système complet de gestion des connections API aux  ATS
- Connections selon divers protocoles (REST, SOAP)
- Gestion automatique des erreurs et retry
- Architecture orientée objet future proof
- Développement séparé d'un outil d'authentification gérant différents flow (notamment Oauth 1 et 2, api tokens)
- Implémentation d'une bonne partie des ATS suivants: https://basile.io/basile-nos-partenaires

## Technologies utilisées

- Symfony, API Platform, Vue.js, APIs REST 

## Liens

- <a href="https://basile.io/" target="_blank" rel="noopener noreferrer">basile.io</a>
