# crypto_scraper

Project Adv. Python, Git, Linux 

Ce projet consiste en la mise en place d'un système automatisé de récupération et d'affichage des prix de Cardano (ADA) en temps réel. Il repose sur un script Bash pour l'extraction des données et un tableau de bord interactif développé avec Dash en Python.

Fonctionnalités:
Le script de scraping, écrit en Bash, récupère les prix depuis le site CoinPaprika en utilisant curl et grep. Les données sont stockées dans un fichier CSV et mises à jour automatiquement toutes les cinq minutes via cron. Un tableau de bord développé avec Dash permet de visualiser l'évolution des prix au fil du temps.

Technologies utilisées:
Le projet repose sur Bash pour le scraping, Python (Dash, Pandas, Plotly) pour l'affichage des données, GitHub pour le versioning et un environnement Linux (VM) pour assurer une exécution continue.

Objectif:
L'objectif est d'automatiser la collecte et l'affichage des prix d'un actif financier en limitant les dépendances externes et en garantissant une exécution fiable et efficace.


Le site web utilisé : https://coinpaprika.com/coin/ada-cardano/
