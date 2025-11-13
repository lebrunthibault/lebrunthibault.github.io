---
title: "Protocol 0, script pour Ableton Live"
date: 2024-01-01
description: "Script de customisation avancé pour controller Ableton Live"
keywords:
  - Ableton
  - Ableton Remote Script
  - Python
  - REST API
  - Open API
---

# Protocol 0

Protocol 0 est un script avancé de contrôle d'Ableton Live.
Mon activité secondaire étant la musique et notamment la production de musique électronique (vous pouvez écouter mes tracks <a href="https://soundcloud.com/tib-tales" target="_blank" rel="noopener noreferrer">ici</a>)
j'ai travaillé ces dernières années sur un programme permettant d'étendre les fonctionnalités de mon logiciel 
de production musicale : Ableton Live.

Il s'agit, dans la nomenclature d'Ableton d'un script de contrôle mais il s'agit en réalité d'un projet Python complet
disposant d'un backend, d'un protocole de communication par commande simple via MIDI, de primitives d'ordonnancement
pour gérer l'exécution de tâches complexes asynchrones (création de tracks, édition de notes, changement de paramètres etc..)


## Overview

J'ai écrit un article expliquant certains choix techniques du projet en particulier en ce qui concerne l'utilisation de paradigmes orienté objet et orienté évènement : [ici](/post/music/protocol0/p0-technical-overview/)

## Technologies utilisées

- Python 3.11, FastAPI, Open API, Typescript

## Links

- <a href="https://github.com/lebrunthibault/protocol0" target="_blank" rel="noopener noreferrer">Repository GitHub</a>
