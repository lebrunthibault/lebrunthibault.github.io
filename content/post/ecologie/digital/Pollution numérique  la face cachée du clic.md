> [Podcast France culture La méthode scientifique](https://www.franceculture.fr/emissions/la-methode-scientifique/pollution-numerique-la-face-cachee-du-clic)
>
> Intervenants : 
>
> - Guillaume Pitron : journaliste, réalisateur de documentaire et auteur de [*"L’enfer numérique : voyage au bout d’un like"*](https://livre.fnac.com/a16007777/Guillaume-Pitron-L-enfer-numerique)
> - Anne-Cécile Orgerie : chercheuse au CNRS en informatique

# Introduction

On vit dans un paradis numérique. Le numérique est :

- un grand récit de préservation de la croissance en respectant le climat
- un rêve de croissance virtuelle
- hors tout est matériel, rien n'est virtuel
- internet = Iceberg dont on voit la partie émergée

certaines idées semblent immatérielles :

- Idée du cloud

- Perfection esthétique du téléphone

# Impact du numérique aujourd'hui

- évaluer consommation en usage : plus difficile qu'avec une voiture (parce que ca se repose sur l'infra)
- consommation en production : très difficile aussi (problème pluri disciplinaire)
- autre pb : un certain nombre de données d'utilisation sont propriétaires 

Deux choses majeurs dans l'impact : 

- Consommation de métaux rares à la production
- Consommation énergétique surtout à l'utilisation

### Téléphone

- devenus bcp plus complexe
- 10 (1950), 30 (1990), 50 (2020) matières premières pour la construction (certains métaux < 1g)

#### [MIPS](https://en.wikipedia.org/wiki/Material_input_per_unit_of_service#:~:text=Material%20input%20per%20unit%20of%20service%20(MIPS)%20is%20an%20economic,single%20product%20to%20complex%20systems.)

- indicateur MIPS (material input per unit of service) : permet de mesure le nombre de matière première (MP) par unité
- plus on va vers le numérique plus le MIPS augmente
- produit habituel : 10:1, 30:1 a 100:1 de kg de MP pour kg de produit fini
- électronique : 1000:1 voir **jusqu'à 16 000:1** pour une puce

Votre téléphone ne pèse sans doute pas 150g mais 183 kg

*"Plus c'est virtuel plus c'est matériel"*

- ordi : 2kg, 1,8T MP
- smartphone : 1200 fois son poids
- puce électronique 2g: 32kg de MP (plus complexe a construire qu'un Boeing 747)
- les téléphones sont plus puissants que le programme informatique Apollo

# Data centers

- nos comptes sont dans des data centers
- chaque jour on se connecte a **peut être 100 data centers**
- infrastructure stratégique très sécurisée
- facile d'évaluer la conso énergétique pour le coup
- les outils de **climatisation = moitié de la conso énergétique** du data center
- selon l'ADEME, les data centers seront **les 1er poste de consommation électrique du 21ème siècle**

## Redondance

- répond à la peur du manque de continuité numérique
- nécessite des infras qui soient dimensionnées pour répondre au pic d'utilisation
- et capable de réagir en cas de panne
- soit avoir des batteries pour prendre en charge de petites coupures
- et des groupes électrogènes pour répondre a des moyennes coupures
- toutes ces infras sont testées (démarrées) régulièrement
- pour une grosse infra cela veut dire : multiples FAI et multiples accès électriques
- redondance des peaks : les serveurs doivent restés allumés en attendant le peak qui n'est pas toujours prévisible
- gaspillage de ressources conséquentes

## Impatience

**"Ce qui coute écologiquement c'est de vouloir tout tout le temps tout de suite"**

- drogués à l'immédiateté, a l'impatience
- **"il faudrait pas qu'un tremblement de terre ait raison d'un match Tinder"**
- problème de **latence** quand le data center est trop loin
- donc on rajoute beaucoup de petits data centers proches des centres de consommation

# 5G

## 4G

- déjà 23 fois plus énergivore que le wifi

## Consommation par rapport à la 4G

- selon certains équipementiers : pas d'augmentation car il s'agit d'augmenter le trafic sans conso d'énergie (+ efficacité énergétique)
- selon les études indépendantes il y a surconsommation
- cependant : l'efficacité énergétique peut être augmentée avec plus d'antennes

## Veille des antennes

- antennes : 20% gèrent 80% de tout le trafic et des améliorations ont été faites sur la veille
- en 4G : les antennes ne sont jamais en veille du au protocole (ack ..)
- en 5G : peut se mettre en veille
- cela dit même les équipements 4G deviennent plus efficaces

## Pourquoi la 5G va amener une surconsommation

- stratification : les autres couchent ne s'arrêtent pas ! Aujourd'hui 2g et 3g fonctionnent toujours comme avant et sont exploitées par l'IOT.
- 5G : portée plus courte donc multiplication des stations
- Paradoxe : même si l'efficacité énergétique peut être multipliée par 10, la conso électrique va quand même augmenter de manière très importante
- Pourquoi : parce qu'on va densifier le réseau, et avoir une performance plus forte. Va répondre à des besoins d'industries avec une qualité professionnel
- Quantifier la conso d'un réseau ? Difficile car constructeurs frileux a donner les valeurs
- Pour quantifier : faire des modèles théoriques ou utiliser les données publiques
- Possibilité en regardant l'historique de la consommation et recouper avec le début des technologies. On peut observer des ruptures de courbe
- la 5G va changer totalement notre rapport à internet (débit x10, IOT). Internet va devenir *un internet de tout* (internet des corps ..)
- ce qui arrive : une explosion de l'univers numérique dont on a pas idée 

# Que faire ?

- gérer l'effet rebond en voyant ca avec des gens des sciences sociales
- limiter les débits (comme la vitesse sur route)
- règlementer la technologie, ne pas la laisser au libre marché

## Lois d'efficacité

- Loi de Moore : densité x2 tous les 2 ans pour un transistor, empirique 
- [Loi de Dennard](https://en.wikipedia.org/wiki/Dennard_scaling) : densité énergétique reste constante (efficacité énergétique rattrape la multiplication de Moore), empirique et vrai que jusqu'en 2006 (a cause des pertes de courants dans les transistors dues à la taille infime). 
- Pour répondre à ca : augmentation du nombre de cœurs en parallèle. 
- Malgré tout, problèmes de dissipation thermique (silicone sombre)
- on atteint la limite physique de l'utilisation des performances d'un matériel  

# Green IT

> Interview avec une doctorante sur le transfert de compétences dans le numérique et dans le Green IT

- Sobriété numérique
- transfert de savoir faire université, centre de recherches, entreprise
- Green IT entre hardware, middleware et software
- progrès mal communiqué au client (notamment les manière d'économiser de l'énergie)
- Pas besoin de consommation h24

# Solutions

- Des solutions techniques existent
- Socialement difficile d'**introduire la limitation** vue comme un tabou
- Travailler sur la durée de vie des interfaces (téléphone ..) : la production représente la moitié de la pollution numérique 
- Plus inquiet sur les données : 
  - oui certains gestes peuvent être faits (nettoyer emails, vidéos etc ..)
  - Hélas en terme d'ordre de grandeur c'est totalement dépassé par l'explosion de l'IOT
- Ex de limitation : Chine qui limite internet pour les jeunes
- Limiter la bande passante pose la question du bon et du mauvais internet

## Solutions de Orgerie 

- Efficacité énergétique (5g)
- problème c'est cassé par l'effet rebond
- Parle de sobriété numérique qui appartient plus à la sociologie qu'a l'ingénierie

## Solutions pratiques

- Fair Phone
- projets de recyclages de câbles sous marin ou de vieux téléphones africains
- Repair Café, FabLab : réparer, rendre les produits durables
- Allonger la durée de vie des équipements
- Eteindre les infra structures (veille)

## La Captologie

- Effet psychologique de difficulté de concentration
- Circuit de dopamine
- La comprendre permettrait de moins consommer
- Attrait / symbolique psychologique des couleurs (bleu / rouge) 
