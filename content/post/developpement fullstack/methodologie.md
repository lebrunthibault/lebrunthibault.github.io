---
prod: true
draft: false
title: Ma Méthodologie fullstack
description:
  📕 Référentiel technique et méthodologique - playbook de développement web
  détaillé
keywords:
  - Développement fullstack
  - Méthodo
  - Stack web
date: "2025-11-04"
color: "#ba8b92"
---

<br>

_Voici mon playbook de développement détaillant point par point toutes les
bonnes pratiques et technologies que j’utilise dans le développement d’un projet
web._

> J’aborde ce playbook par sections et m’étend parfois sur des sujets un peu techniques.
> N’hésitez pas à consulter la table des matières à droite pour lire directement
> les sections qui vous intéressent.

# 🔥 Développement web moderne

C’est une évidence depuis une dizaine d’année : tout projet de plateforme web
utilise le paradigme Single Page Application et api REST

**Avantages**:

- Un front dynamique, rapide et intelligent (logique d'affichage et de gestion
  du state complexe, gestion granulaire des appels API),
- Aucun rechargement de page pour une expérience utilisateur rapide et
  rassurante
- Utilisation des dernières fonctionnalités des frameworks Javascript moderne
  ([Vue.js](https://vuejs.org/), React ou Angular): réactivité, composants ui réutilisables,
  expérience de développement moderne (hot reload, typing avec typescript,
  devtools intégré, écosystème npm)

# 📞 Une interface mobile par défaut

Même si, en fonction des projets la navigation desktop peut encore être
(largement) dominante (en particulier pour les sites d’entreprise) le mobile
n’est plus une option depuis plusieurs années et le design responsive mobile
compatible est à la base de tous les frameworks CSS modernes et de tous mes
projets. J’utilise en ce moment en priorité Vue.js avec [Quasar](https://quasar.dev/), un
framework Vue.js professionnel et mobile first (design responsive,
composants compatible mobile).

Les design que je propose sont tous responsives (navigation, layout, composants
ou widgets).

## Je veux mon app mobile

Dieu merci la hype autour des apps mobiles s’est dissipée il y a plusieurs
années et les entrepreneurs et clients ont conscience de la réalité : personne
n’installe d’app inconnues. C’est un choix qui est réservé soit aux entreprises
déjà bien connues de l’utilisateur soit à des projets pensés exclusivement pour
le mobile (type jeu mobile).

Pour un projet de plateforme web, la valeur ajoutée est souvent nulle par
rapport à un site mobile ready.

Dans la même veine, la hype sur les progressive web apps a aussi fade out et
pour les même raisons. Aujourd’hui l’état de l’art est de proposer un site pensé
mobile en utilisant si nécessaire des features PWA (navigation offline, service
workers).

# ⚡ Un backend performant et léger

Si les front prennent de plus en plus d’ampleur, la gestion du backend suit une
courbe inverse et aujourd’hui on privilégie (à raison) des backend plus sobres,
ciblés et maintenables. C’est aussi ce que je préconise en utilisant des
frameworks légers et extrêmement performants au lieu de frameworks batteries
included (notamment MVC). J’utilise aujourd’hui en priorité Python / [FastAPI](https://fastapi.tiangolo.com/) (en m’appuyant sur
mes codebases précédentes pour atteindre la maturité de frameworks plus poussés)
et Node.js / [NestJS](https://nestjs.com/) (qui n’est pas un micro framework mais touche un
sweet spot concernant les plateformes web utilisateurs classiques).

A noter que la trend vers les micro frameworks ne se dément pas avec l’arrivée
du développement IA. Il n’a jamais été aussi facile de “recoder” des
fonctionnalités génériques type authentification, autorisation ou emailing sur
un micro framework grâce aux LLM.

## Un setup prêts à scale

L’autre gros avantage des micro framework orientés api REST est la possibilité
de scale facilement plus tard en allant notamment vers des micro services.

Si jamais votre entreprise décolle, ce paradigme permet d’étendre les
fonctionnalités d’un projet sans limite technique et est très apprécié des
développeurs. Par ailleurs, d'un point de vue souveraineté, le backend devient
beaucoup moins dépendant d’un tiers et à la merci d’un abandon même partiel des
développements sur le framework choisi.

## REST, l’approche pragmatique

Même si d’autres approches se développent, tout le monde code en REST, un
standard bien compris. Je m’engage à fournir une api REST pragmatique avec
notamment :

- l’utilisation des verbes et statuts HTTP adaptés
- des routes toujours basées sur des ressources
- pagination et filtrage standards

# 🐘 Une base de données pouponnée

Pour la base de données il n’y a plus qu’un choix aujourd’hui: [PostgreSQL](https://www.postgresql.org/) qui
est devenu le standard de facto. C’est une bdd mature, open source (aucun vendor
lock in) avec de nombreuses fonctionnalités avancées (JSON natif, recherche
plein texte, nombreuses extensions, performances excellentes).

La base de données est gérée avec un ORM (sqlalchemy en python, typeorm en
Node.js), une couche nécessaire pour la gestion des connexions, du
cycle de vie des entités et de la sécurité. Il est parfois nécessaire de
requêter en SQL pur mais c’est rarement le cas.

Par ailleurs je travaille exclusivement avec des migrations (notamment alembic
en python) ce qui permet d’avoir un état iso sur les différents environnements
(local, preprod, prod) et de pouvoir facilement reset ou spawn des base de
données en local (tests ou en utilisant des fixtures). Les migrations
s’intègrent aussi dans un paradigme agile d’évolution progressive de la bdd
selon les besoins (on commence toujours petit pour limiter la dette technique).

## Schéma de bdd

Je design mes bases de données avec les meilleures pratiques. L’idée est d’avoir
d’une part un schéma clair avec un minimum de redondance sauf cas particuliers
(cache, performance). D’autre part de configurer la base pour soulager le
backend (vérification d’unicité avec des contraintes, gestion des enums,
accélération des performances avec des index, voire des vues, soft delete,
colonnes de timestamps).

## Exploration

De mon côté j’utilise [Datagrip](https://www.jetbrains.com/datagrip/) qui est un excellent explorateur me permettant de
gérer facilement l’état de la base sur plusieurs environnements ainsi que mes
requêtes d’analyse ou de debug. C’est un explorateur que je recommande aux
clients orienté tech : je pourrais vous partager mes requêtes voire configurer
des vues pour un contact très direct avec les données.

# 👌🏽 Qualité du code

## 🥸 Garanties sur la qualité de code

Je prends la qualité du code très au sérieux, c’est un des sujets les plus
passionnants et la raison principale pour laquelle je fais du développement.
J’aime respecter des principes généraux de développement comme SOLID ou DRY et
ai une expérience significative sur différents paradigmes de programmation en
particulier l’orienté objet (mais aussi la programmation fonctionnelle ou
l’orienté événement). J’ai aussi été influencé par mes lectures sur le Domain
Driven Design, une influence forte sur ma conception des backends.

La qualité du code est un vaste sujet dont j'aimerais évoquer quelques points, de manière simpliste.

## Limiter la dette technique

J’essaye au maximum de limiter la duplication de la logique métier, un point
encore plus important aujourd’hui qu’il ne l’était avec l’arrivée des IA et du
vibe coding. Il n’a jamais été aussi facile de générer de la dette technique, une
dette qui sera payée des mois voire des années plus tard et peut complètement
tuer un projet.

## Limiter les bugs en production

Un livre pourrait être écrit là dessus, mon approche consiste à:

- toujours relire mes commits entièrement avant de merge
- mettre en place une CI sur mes projets même simples (au minimum linting, type
  checking et formatting). Cela permet en plus d’être sûr de son historique git
  et de pouvoir revenir à des versions stables facilement.
- intégrer le linting au développement local via un commit hook
- mettre en place de tests unitaires dès que le projet grossit, voire end to end
  (le test driven design n’est pas toujours un choix pragmatique pour tenir un
  budget compétitif)
- écrire un code typé (checké par mypy ou typescript)
- déployer en continu sur la production
- limiter les conflits git au maximum graĉé à
  - un bon git flow (j’utilise le github flow)
  - des commits associés à des features spécifiques
  - jamais de branches ouvertes pour plus de quelques heures
- générique un historique git cohérent pour pouvoir annuler une mise à jour et
  déboguer facilement. Je rebase et génère un historique git linéaire et
  documenté (avec des commit messages clairs comprenant un lien vers le ticket
  associé)

# 🐱‍💻 Un développement ouvert aux agents IA

Je développe avec assistance d'un agent IA (en l'occurence [Claude Code](https://www.claude.com/)) et vous propose de consulter [ce billet](/post/developpement-fullstack/workflow-ia/) résumant mes réflexions principales sur l'utilisation de ces outils.

D'un point de vue technique je fais en sorte que la codebase soit aussi lisible et maintenable pour un développeur humain qu'un agent IA
(spoiler alert c'est souvent la même chose).

# 🔒 Sécurité shift left

La sécurité est un sujet transversal et complexe qui fait partie intégrante de
mon travail dès le départ (ce que les développeurs appellent shift left
websecurity).

J’y tiens d’une part car elle rejoint les bonnes pratiques d’un développement
web solide et professionnel et d’autre part car j’ai travaillé un an chez
GitGuardian, une startup leader dans la cybersécurité et qui m’a formé à un
certain nombre de bonnes pratiques websec.

J’ai conscience des failles principales du développement web (en consultant par
exemple [OWASP](https://owasp.org/)) et suit dans tous mes projets une roadmap
sécurité claire :

**Authentification & autorisation** - Throttling anti brute force, contrôle des
droits sur chaque route, mots de passe hachés (SHA-2+), JWT sécurisé

**Protection des données sensibles** - credentials stockés hors de la code base
(.env, .gitignore), pas de données privées dans les logs/cookies/réponses API

**Prévention des injections** - Protection contre les injections SQL (avec
l’ORM), validation stricte des inputs (DTO), protection contre le XSS sur le
contenu utilisateur

**RGPD & données personnelles** - Solution analytics minimale (sans nécessité de
consentement cookies), minimisation des données exposées, anonymisation à la
suppression de compte, page de politique claire

**Sécurité infrastructure** - Accès au serveur par clé SSH, accès aux services
par reverse proxy (Nginx), fichiers sensibles (.env, .git) non exposés, accès
prod restreint (création d’un utilisateur avec droit restreint pour l’accès SSH
et le lancement de commandes sur le serveur)

**Monitoring & résilience** - plan de sauvegarde testé (dernier backup bdd
testé, script de backup ajouté au crontab), backups bdd géographiquement
distribués et chiffrés ([Backblaze](https://www.backblaze.com/)). Historique des logs stockés et testés avec
Loki et Grafana. Mise en place optionnelle de Sentry pour le monitoring des
erreurs serveur et front.

**Mises à jour régulières** - Paquets logiciels et OS à jour pour corriger les
failles connues (bump régulier des paquets, Dockerfile configurés sur les
versions latest des OS)

Ces sujets sont pris en compte dès le début du développement et je réalise un
point complet en m’appuyant sur un document de référence (google sheet partagé
au client) avant l’ouverture de la plateforme au public.

# 🚀 Déploiement et infra

De la configuration du nom de domaine à la mise en production finale je m’occupe
de tout et vous propose une solution d’hébergement et de déploiement continue
clef en main.

Cette solution comporte les caractéristiques suivantes:

## Conteneurisation

- Développement conteneurisé (Docker) pour avoir des environnements local /
  preprod / prod ISO, minimiser les bugs en prod et accélérer l’onboarding et le
  déploiement
- Déploiement des conteneurs pragmatique avec Docker compose pour un MVP ou
  petite plateforme. Possibilité de passer sur Kubernetes pour scale.

## Traffic web

- Le trafic passe par un reverse proxy (Nginx) avant d’atteindre l’orchestrateur
  (Docker compose en MVP) permettant notamment une gestion du HTTPS, une
  meilleure sécurisation (protection DDOS notamment) et une flexibilité accrue
  dans la configuration des domaines et sous domaines.
- Le HTTPS est géré et renouvelé automatiquement avec [Certbot / Lets encrypt](https://letsencrypt.org/)
  (certificats gratuit)

## Hébergement

La solution pragmatique que j’utilise le plus souvent est le déploiement
semi-automatique sur un serveur virtuel ([OVH](https://www.ovhcloud.com/fr/) pour rester en France, sinon
[DigitalOcean](https://www.digitalocean.com/) par exemple). L’accès au serveur se fait par SSH, la mise en place
d’une couche d’infrastructure as code (IAAC) et d’un déploiement cloud natif
n’est pas nécessaire pour des MVP mais peut être ajoutée ensuite.

Concernant le provisionnement du serveur, j’utilise Ansible (installation des
paquets, de Docker, configuration du reverse proxy, script de backup bdd etc..)
avant de peaufiner les réglages manuellement au cours du projet (lancement de
commande d’import de données, configuration du .env..) sans perdre de temps de
développement sur des sujets cloud qui sont surtout intéressants sur des projets
à fort traffic ou forte complexité (notamment avec les micro services)

## Déploiement continu

Le déploiement continu (CI / CD) est intégré de base dans tous mes projets. Tous
mes commits, une fois revus sont mergés, validés par la CI et déployés
automatiquement en préprod ou en production limitant ainsi le risque de bugs et
facilitant le débogage et le rollback le cas échéant.

- Il n’y a pas de grandes mises en production (génératrice de friction et
  d’erreurs) et les utilisateurs bénéficient de mises à jour quotidiennes.
- couplé à Docker le downtime est proche de zéro

## Base de données

La base de données est intégrée à la configuration Docker. Le script de backup
est géré par Ansible, testé dès le début des développements et à la MEP finale.
Je propose au client un backup sur un service externe (Backblaze) dans le cas
(très rare) d’une panne matérielle ou incendie dans le datacenter.

# 📈 Monitoring et analytics: une approche pragmatique

## Monitoring

Le monitoring d’une app mise en production est parfois laissé de côté mais il
est intégré à mon template web nativement. Mon déploiement minimal contient en
effet la stack monitoring [Prometheus](https://prometheus.io/) (métriques), Loki (logs) et [Grafana](https://grafana.com/)
(dashboard des visualisation) permettant pour un MVP un suivi plus que
satisfaisant et extensible à souhait.

Concernant le suivi des bugs je peux mettre en place si nécessaire [Sentry](https://sentry.io/welcome/?utm_source=google&utm_medium=cpc&utm_id={20398270056}&utm_campaign=Google_Search_Brand_SentryKW_EMEA-Tier1_Alpha&utm_content=g&utm_term=sentry&gad_source=1&gad_campaignid=20398270056&gbraid=0AAAAADua1WLdGm94YaKteF8xS4lRislSL&gclid=CjwKCAiAw9vIBhBBEiwAraSATuBarcrrP-97O7WvkWgFjZICHJW8IWnIQ8okG-eeJgp__xTU0UvJoxoCiUcQAvD_BwE)
(service payant) et je branche gratuitement
[Uptime Robot](https://uptimerobot.com/) qui alerte en cas de défaillance du
site (scans de certaines pages).

A noter que dans le cas d’un projet plus conséquent (startup en train de scale)
j’ai une expérience sur [Datadog](https://www.datadoghq.com/), pour un monitoring et forensic exhaustif (mais
cher et coûteux à paramétrer).

## Analytics

Concernant les analytics j’opte généralement pour une solution analytics
minimale ([Goat Counter](https://www.goatcounter.com/)) qui permet de suivre le
traffic web de manière responsable sans être intrusif et compatible RGPD sans
nécessité de bannière cookie.

Google Analytics peut être installé sur demande mais demande une bannière
cookie.

Je travaille de temps en temps avec Matomo pour un suivi plus précis des
interactions sur le site.

# 🤖 SEO: un site ouvert à nos amis les robots

Je ne suis pas expert SEO mais j'applique un ensemble de bonnes pratiques SEO.

J’utilise notamment:

- un markup sémantique (headers, article..)
- des tags meta appropriés (title, description)
- une attention à la performance de chargement de la page (LCP réduit, taille
  des images)
- des urls claires

Je vérifie la performance des pages principales avec Lighthouse.

## Server Side Rendering (SSR)

Pour les sites qui ont besoin d’un SEO particulièrement performant je travaille
avec [Nuxt](https://nuxt.com/) en SSR. Cela demande un peu plus de travail côté
développement mais permet une indexation idéale par les moteurs de recherche et
IA. Cela a été le cas dans ma mission chez [Kessel](/projects/kessel), une startup dans l'édition numérique

# 🎨 UX / UI ou comment rivaliser avec Da Vinci

Mon expérience de développement web me permet aujourd’hui de proposer des
interfaces intuitives : navigation claire, formulaires réactifs, gestion des
erreurs transparentes, layouts responsifs, interfaces aérées, composants au look
moderne (design material généralement) ou encore intégration d’une charte
graphique (ou d’éléments graphiques).

Pour ce qui est du développement d’interface d’administration, de dashboards ou
de tunnels d’inscription, je fournis une solution clef en main responsive ou le
client peut modifier les paramètres d’affichage nécessaires.

Je référence de temps en temps des articles d’autorité sur ce sujet comme
[celui ci](https://www.nngroup.com/articles/ten-usability-heuristics/)

En revanche je ne suis pas un expert en UX et pour des projets qui attendent un
traffic conséquent de la part d’utilisateurs extérieurs (et selon le budget) je
préfère travailler avec [Elina Lapierre](https://www.linkedin.com/in/elinalapierre/)

## Approche CSS

L’approche actuelle avec css et de garder le css au plus proche du markup html.
Je suis d’accord avec ces pratiques et j’utilise donc l’approche utility-first
(multiples classes utilitaires pour un contrôle fin avec
[TailwindCSS](https://tailwindcss.com/)). Je les factorise le cas échéant avec
des composants JS.

# 🤝🏽 Une gestion de projet agile et inclusive

## Une gestion de projet agile et proche du client

Le début de projet nécessite toujours un temps de réflexion et de questions pour
interroger au maximum le besoin du client, en comprendre ses certitudes et ses
limites. C’est le moment où j’écris ou réécris des spécifications, plus ou moins
techniques, que je partage au client. Ces documents permettent de dialoguer et
de garder une trace utile mais sont généralement rapidement désynchronisés avec
le développement de la plateforme et c’est un bon signe car ce qui compte est
justement l’évolution dynamique du besoin dans un contexte agile.

Inversement dès le début du développement, le focus est centré sur le dialogue
avec le client, des déploiements fréquents (déploiement continu, généralement
plusieurs fois par jour) avec à chaque fois un message de ma part, et des points
fréquents de feedbacks, de discussion du besoin et d’affinage et priorisation du
backlog.

Pour les projets plus conséquents, des ateliers thématiques (fonctionnalités,
UX, retours utilisateurs) peuvent être intéressants pour structurer et prioriser
l’effort de développement.

D’un point de vue tooling, je travaille en ce moment avec [Clickup](https://clickup.com) mais je peux
m’adapter aux outils du client le cas échéant. Je donne toujours au client un
accès admin à l’outil de gestion de projet et je l’incite à participer
activement à la spécification, priorisation et gestion des tickets (c’est le
cœur de l’esprit agile).

# 📖 La documentation, laisser une trace pour les générations futures 

La documentation et la traçabilité des intentions sont un sujet important sur
lequel il faut avoir une approche pragmatique et efficace. La documentation,
comme la sécurité, doit être une réflexion globale qui s’intègre de manière
granulaire à la gestion de projet comme au développement.

Je ne suis pas partisan des documents longs et verbeux que personne ne lira. Ils
peuvent en revanche être utiles pour les IA.

Ma manière de procéder consiste à répartir la documentation sur 3 niveaux :

- des documents textes hors de la codebase et éditables librement pas le client
- des documents markdown intégrés à la codebase et adressés aux développeurs et
  agents IA
- le code lui même (naming, commentaires)

## Documentations au format texte

- partage d’un dossier drive avec le client qui regroupe les différentes
  itérations des documents de spécifications (en particulier ceux créés au début
  du projet) ou des notes de réunion. Ce dossier est plus une archive qu’une
  documentation vivante.
- documents types que je partage au client:
  - PRA (plan de reprise d’activité): document centralisant les informations
    nécessaires au fonctionnement du projet (contacts, credentials, type d’infra
    et de déploiement utilisés, informations utiles à l’onboarding)
  - checklist de mise en production finale à affiner avec le client:
    vérification des contenus, du fonctionnement du tooling de monitoring, des
    accès à l’infra, des backup etc..
  - checklist de sécurité : voir point détaillés plus haut
- Spécifier un maximum les tickets. Les tickets (ou tâches) sont la source
  d’autorité principale sur l’intention produit juste après le code.
  L’élaboration d’un backlog bien spécifié et découpé est une partie importante
  du travail de développement qui fait gagner du temps à tout le monde. C’est un
  travail qui est idéalement fait à deux (le client / product owner et moi).

### Documentation intégré à la codebase

- Création d’un README centralisant les informations nécessaires à l’onboarding,
  les technologies utilisées et les spécificités éventuelles à connaître. Ce
  document sera en particulier utile aux développeurs à qui le projet serait
  transmis (même si je suis toujours joignable).
- Création de fichiers markdowns de documentation résumant d’une part mes
  pratiques de développement et la structure du projet et d'autre part des
  parties spécifiques de la codebase. Ces fichiers peuvent être aussi utiles aux
  développeurs futurs qu’aux IA.
- Un fichier [CLAUDE.md](https://www.anthropic.com/engineering/claude-code-best-practices) est toujours présent dans mes projets et est
  explicitement destiné à Claude code (mais peut être exploité par d’autres
  modèles).

### Code as documentation

Enfin, les plus important pour la fin: écrire un code sémantique ou les
intentions business sont claires. Utiliser la même nomenclature que celle
utilisée pour le produit et par le client (vocabulaire commun). Avoir un naming
cohérent et explicite des fonctions, modules, classes, variables.. De manière
générale, s'inspirer des bonnes pratiques du Domain Driven Development.

Concernant les commentaires on dit souvent qu’un code clair et sémantique est un
code qui ne nécessite pas énormément de commentaires.

Certains commentaires peuvent être utiles (les agents IA en génèrent d’ailleurs
“gratuitement”). D’autres peuvent être superflus voire gênants car ils peuvent
vite être obsolètes (évolutions du code ou copier / coller) et participer à la
création d’une dette technique.

Par ailleurs je fais usage de fichiers standards en développement web qui
rassemblent un certain nombre de commandes que tout développeur comprendra
facilement : package.json notamment mais surtout un Makefile présent dans chaque
projet.

# ⚙️ Les fonctionnalités que j'intègre de base

## 👥 Gestion des utilisateurs

La gestion des utilisateurs est un besoin très fréquent sur les plateforme que
je développe et mon template de base inclut une gestion exhaustive des
utilisateurs avec notamment

- le formulaire d’inscription (email / mdp sécurisé). Possibilité d’intégrer un
  login social.
- la confirmation d’inscription par email
- la gestion du mot de passe oublié et changement du mot de passe
- un espace administrateur avec gestion des utilisateurs
- une gestion des rôles (Admin et Utilisateur par défaut, extensible) et
  d’autorisations granulaires

## ✉️ Emailing

Mon template web comprend la gestion de l’envoi d’emails (templates emails)
envoyés par API avec [Brevo](https://www.brevo.com/).

## 🔎 Barre de recherche

Une barre de recherche peut être utile à certains projets et dans ce cas je
recommande généralement [Algolia](https://www.algolia.com/) qui est un service très performant et
configurable de recherche plein texte facetée.

Pour des projets demandeurs en termes de complexité ou de volume, on peut
basculer sur Elasticsearch, que j’ai utilisé dans plusieurs projets.

## Sites Statiques (JAMstack)

Parfois rien de tout ce que j’ai évoqué plus haut est nécessaire et seule une
interface en Javascript suffit. Dans ce cas précis (pas de bdd, pas de
logique serveur, d’utilisateurs etc), il est plus cohérent de déployer un site
statique sur un CDN (type netlify ou Vercel) ce qui permet d’obtenir une haute
disponibilité et d’excellentes performance pour un très faible coût en terme de
dev.

C’est le choix que j’ai fait pour ce blog ! ([Hugo](https://gohugo.io/), html sémantique, TailwindCSS, JS vanilla, CDN Netlify)

Dans le cas où il est nécessaire aux admins d’éditer du contenu régulièrement un
CMS peut être préférable et intégrable de manière autonome ou associé à une
plateforme web existante.

J’ai travaillé notamment avec [Strapi](https://strapi.io/), une solution CMS headless qui permet de
découpler la génération de contenu de l’affichage qui peut être fait directement
en JAMStack (cependantStrapi nécessite d'être déployé sur un serveur).
