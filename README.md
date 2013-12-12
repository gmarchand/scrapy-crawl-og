scrapy-crawl-og
===============

Voici la configuration pour faire un crawl complet d'un site pour récupérer l'ensemble des metas open graph de chaque page.
Cela permet de vérifier l'intégration sociale (Twitter & Facebook) du site.

Le script produit : 
+ des fichiers csv consultable dans Excel 
+ des enregistrements dans une base de données MongoDB pour pouvoir ensuite la requêter via des tests unitaires. Par exemple si le player est embarqué alors le og:type doit être video)


