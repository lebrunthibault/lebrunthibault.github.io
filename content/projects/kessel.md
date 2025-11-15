---
title: "Kessel, plateforme d'édition numérique"
date: 2025-03-01
description: "Développement backend d'une plateforme d'édition numérique avec un fort traffic"
keywords:
  - FastAPI
  - Stripe
  - React.js
  - Algolia
  - AWS
background: journal.jpeg
logo: logo_kessel.jpeg
---

# kessel.media, dev backend lead

- Scaling de l'emailing de 100 000 à 3 millions d'emails envoyés par mois en déployant une task queue Celery et en optimisant la génération d'emails.
- Optimisation du backend pour gérer un traffic d'environ 100 000 visites par mois
- Refonte du backend de la page d'acceuil avec mise en place d'un moteur de recherche (Algolia) et d'un backoffice d'édition.
- Refonte de l'architecture du microservice statistiques et améliorations des performances en utilisant Timescaledb.
- Création d'un pipeline de tests unitaires et fonctionnels intégré à la CI.

## Technologies utilisées

- Le projet est codé en Python (FastAPI) et React (en server side rendering).
- Stripe, Algolia, TimescaleDB, Datadog, AWS (CloudFormation) 


## Liens

- <a href="https://www.kessel.media/" target="_blank" rel="noopener noreferrer">kessel.media</a>
