# Internationalization



**links**:

	- https://symfony.com/doc/current/translation.html#translation-providers
	- https://borntobeglobal.com/2020/05/26/web-application-localization-best-practices/
	- https://lokalise.com/



## Symfony steps

- [Enable and configure](https://symfony.com/doc/current/translation.html#translation-configuration) Symfony's translation service;
- Abstract strings (i.e. "messages") by wrapping them in calls to the `Translator` ("[Translations](https://symfony.com/doc/current/translation.html#translation-basic)");
- [Create translation resources/files](https://symfony.com/doc/current/translation.html#translation-resources) for each supported locale that translate each message in the application;
- Determine, [set and manage the user's locale](https://symfony.com/doc/current/translation/locale.html) for the request and optionally [on the user's entire session](https://symfony.com/doc/current/session/locale_sticky_session.html).



<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220311142156491.png" alt="image-20220311142156491" style="zoom:50%;" />

### Keyword approach

- The choice of which method to use is entirely up to you, but the "keyword" format is often recommended for multi-language applications
- Keywords can be nested in yaml or php



### [ICU message formating](https://unicode-org.github.io/icu/userguide/format_parse/messages/)

- Rearrange messages according to grammar
- complex



### Translatable objects

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220311155800256.png" alt="image-20220311155800256" style="zoom:50%;" />

### [Extracting Translation Contents and Updating Catalogs Automatically](https://symfony.com/doc/current/translation.html#extracting-translation-contents-and-updating-catalogs-automatically)

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220311155918361.png" alt="image-20220311155918361" style="zoom: 33%;" />



### [Database translation with doctrine](https://github.com/doctrine-extensions/DoctrineExtensions/blob/main/doc/translatable.md#entity-domain-object)



## https://borntobeglobal.com/2020/05/26/web-application-localization-best-practices/

- Size of words
- No text in images
- Pseudo localization to test
- Don’t use too little strings and concatenation. Hard to translate for different grammars
- Punctuation in strings
- add a button to switch language (don’t rely on browser)
- don’t use flags, use language names
- sort on server
- give context to translators



# Possible

- définir plusieurs domaines (security, application ..). Le domaine peut etre défini en haut d’un fichier twig : `% trans_default_domain 'app' %}`
- pour chaque domaine : un fichier par langue
- Config translation.yaml avec default lang et définit où sont les fichiers
- en index on peut utiliser :
  - messages
  - code (nestable)
- Les messages peuvent etre traduits :
  - dans les templates (avec filtre trans)
  - ou dans les services avec `new TranslatableMessage` pour ne pas avoir a passer les arguments
- Avoir des parametres en twig grace au tag trans auquel on peut passer un contexte : variable au format %<var>% 
- Commandes utiles:
  - dump tous les messages a traduire pour une langue
  - remplir par défaut les messages a traduire pour une langue

### Stockage :

- en fichiers
- en bdd : https://symfony.com/doc/current/reference/dic_tags.html#dic-tags-translation-loader





## Avec Lokalize

- on connect le repo github
- on donne le dossiers translation
- on pull
- tout s’affiche et est editable dans le saas
- on push : ca fait une pull request
- pas de dépendance

