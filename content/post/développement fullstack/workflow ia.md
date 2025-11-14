---
prod: true
draft: false
title: 🤖 Mon workflow avec les agents IA
description:
  Bonnes pratiques pour coder avec agents IA de manière sobre et controlée
keywords:
  - Développement logiciel
  - Agent IA
  - LLM
date: "2025-09-01"
---

# Les agents IA, un pouvoir qui implique des responsabilités

Les agents IA ont débarqué il y a quelques mois dans le monde du développement
et sont en train ~~de se préparer dans l'ombre à prendre le pouvoir et prévoient de faire de nous des esclaves regardant des vidéos de chats sur tiktok~~ d’opérer une vraie révolution tant leurs capacités sont
épatantes sur tout type de développement et en particulier sur le développement
web.

Aujourd’hui c’est presque impossible de ne pas intégrer ces agents comme
citoyens à part entière d’un tooling de développement moderne.

Malgré tout, l’utilisation de l’IA pose beaucoup de questions et est loin d’être
aussi évidente et bénéfique que ne le laisse penser les premières impressions.

> Après une utilisation quotidienne ces derniers mois et de nombreuses réflexions
> j’ai décidé de faire un retour d’expérience et de parler de mon workflow avec
> les agents IA, de ses avantages et ses limites.

## Des questions éthiques

Avant de discuter technique je tiens à aborder certaines questions éthiques
entourant l’utilisation de ces outils.

Tout d’abord concernant l’impact carbone. L’impact carbone d’un LLM comme Claude
Sonnet peut être conséquent mais dépend énormément de l’usage. Aujourd’hui mon
usage mensuel tourne autour de 10 millions de tokens soit

- en conso électrique (estimation courante de 0,0005 kWh / 1 000 tokens): 5 kWh,
  soit 1 à 2 kg équivalent CO2
- En prenant en compte le coût de l’infra (fabrication, maintenance) on peut
  multiplier par 2 soit potentiellement pas loin de 50 kg de CO2 par an.

En résumé, ce n’est pas une catastrophe mais c’est un coût notable.

**Pourquoi c’est acceptable ?**

## Une utilisation sobre, pas du vibe coding 🤮

Tout est une question de mesure et d’impact. Là où l’utilisation de ces LLM peut
être éthique c’est si elle vient remplacer le travail d’un dev sans effet rebond
notable. Autrement dit, si le développeur profite de ce temps libéré pour
générer encore plus de revenus, on entre dans une boucle néfaste ou les coûts et
l’impact peuvent exploser.

Ma vision est différente: j’utilise l’IA pour travailler moins et c’est le sens
que les innovations techniques doivent avoir. Le fait que tant de personnes
(bien payées) continuent de travailler aussi dur à notre époque m’interroge. Personne n’aime son travail à ce point là haha.

Autrement dit, je ne compte pas augmenter mes revenus grâce à l’IA, juste mes revenus horaires ^^. J'espère pouvoir me
libérer du temps pour un impact que j’estime encore faible à l’heure actuelle.
D’autres actions sont beaucoup plus significatives (comme manger végétarien ou
ne pas prendre l’avion).

D’autre part, mon positionnement en tant que dev expert et mon workflow avec une
utilisation contrôlée préviennent une explosion des coûts. Quelles que soient
les évolutions je compte garder le contrôle du code que je déploie et maintient
aujourd’hui un équilibre développement manuel / agent IA favorable au manuel. \
Sur beaucoup de sujets (et passé le tout premier MVP), rien ne va plus vite et
ne génère un code aussi sémantique et maintenable qu’un développeur expérimenté.

## Des agents sans intention

D’autre part et c’est le cas pour de nombreux domaines abordés par l’IA, un
sujet qui me frappe malgré l’exactitude et la rapidité des modèles récents est
la propension des agents à proposer des réponses ou il n’y a pas d’intention
claire et j'oserais presque dire pas d’émotions.

C’est un ressenti évident quand on demande à un LLM de produire du texte à visée
artistique ou de la musique. On ne ressent pas de connection émotionnelle et on a
l’impression (au mieux) d’assister à un exercice scolaire par un étudiant pressé
de partir en vacances. Toute la richesse et la portée des interactions humaines,
qu’elles qu’en soient le moyen d’expression repose sur la communication d’une
intention qui en fin de compte exprime une forme d’émotion.

Lire un code généré par IA est ennuyeux et lassant. C’est un code sans
fantaisie, verbeux et générique.

Que ce soit en termes d’impact ou de résultats, la pratique incite à utiliser
les agents de manière contrôlée et segmentée au risque d’appauvrir la code base
et ce qu’elle évoquera aux futures développeurs. Je me vois déjà reprendre des
codebases dans quelques années et me dire “encore un truc codé par une IA..” 😂

## Savoir quand utiliser l’IA

L’informatique existe depuis un moment et de nombreux outils excellents existent
autour de nous. Il faut résister à l’envie et au confort (relatif) de passer par
l’IA pour tout et n’importe quoi. \
> J’ai envie de donner un exemple, j’ai écris ce document sur google doc et
> souhaitait le passer en markdown pour le publier sur ce blog. J’ai d’abord pensé
> à copier coller ce texte dans Claude avant de réaliser qu’une extension gdoc
> existait déjà et fait le travail mieux de manière algorithmique et beaucoup plus
> rapidement !

**Abordons maintenant mes recommandations techniques sur l’utilisation
d’agents.**

## Un workflow hybride tout en contrôle

La vraie révolution pour le développement web a été l’arrivée d’agents capables
de travailler sur une codebase entière.

Les outils se divisent en 2 camps, les IDE IA (comme Cursor) et les agents IA
CLI (comme Claude Code).

Je préfère largement la seconde solution qui me permet de garder un contrôle
total de mon éditeur (Jetbrains), sans érosion ni de mon plaisir à coder ni de mon screen space.

J’utilise donc Claude Code (Sonnet 4.5) connecté à mon éditeur Jetbrains (via la
commande [/ide](https://code.claude.com/docs/en/jetbrains), les fichiers ouverts
et la sélection sont intégrés au contexte de Claude Code).

## 💫 Claude Code, une CLI stellaire

J’avoue ne pas avoir testé d’autres outils CLI comme Codex mais je considère
Claude Sonnet comme le meilleur LLM pour le code (c’est celui que j’utilise en
version web et il me semble plus précis et utile que ChatGPT).

Par ailleurs l'expérience de CLI de Claude Code est bluffante, Anthropic a
produit un travail exceptionnel sur cet aspect là, bravo à eux.

## Bonus tips

Claude, comme tous les LLM produit une impression de fini out of the box et n’a
pas besoin de configuration supplémentaire pour être très utile.

Par exemple, le plan mode qui a été rajouté récemment me semble inutile et plus
adressé à des vibe codeurs qu’à des personnes qui savent ce qu’elles font.

Malgré tout j’ai expérimenté avec succès quelques [recommandations d’Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices):

- J’utilise un claude.local.md générique pour tous mes projets mettant claude
  code au parfum de ma manière de développer dès que je commence un nouveau
  projet (utilisation du Makefile, préférences d’architecture etc..)
- Pour les projets existants, je demande à Claude d’enrichir ce fichier en
  analysant la codebase. Ce qui permet ensuite d’avoir des modifications
  intelligentes qui dépassent le contexte des fichiers analysés (ex: utilisation
  de services ou librairies internes, exécution de commandes de lint..)
