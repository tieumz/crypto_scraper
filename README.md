# crypto_scraper

Project Adv. Python, Git, Linux – Mathieu Meunier
Ce projet a pour objectif la mise en place d’un système automatisé de récupération et de visualisation en temps réel du prix de Cardano (ADA). Il s’appuie sur un script Bash pour le scraping des données, et sur un tableau de bord interactif développé en Python avec Dash pour l’affichage.

Fonctionnalités
Un script Bash interroge l’API de CoinPaprika à intervalles réguliers à l’aide de curl et filtre les données avec grep. Les résultats sont stockés dans un fichier CSV local, mis à jour automatiquement toutes les cinq minutes via cron.
Le tableau de bord Dash lit ces données et les affiche dynamiquement sous forme de graphique.

Technologies utilisées
Scraping : Bash (curl, grep)

  - Visualisation : Python (Dash, Pandas, Plotly)

  - Automatisation : cron

  - Hébergement : AWS EC2 (Amazon Linux 2023 – t2.micro gratuite)

  - Versioning : Git & GitHub

Objectif:
L'objectif est d'automatiser la collecte et l'affichage des prix d'un actif financier en limitant les dépendances externes et en garantissant une exécution fiable et efficace.

L'URL publique de mon dashboard : http://15.237.191.149:8050/

ATTENTION à l'échelle des prix sur le dashboard, sinon trop petite et le cours de la crypto forme droite horizontale.

Le site web utilisé : https://coinpaprika.com/coin/ada-cardano/

Utilisation de : AWS EC2 avec une instance Amazon Linux gratuite (t2.micro)

Configuration avec cron pour automatiser le scraping.

P.S : Le scraping à 1h de décalage car AWS utilise par défaut l'UTC (et nous CET ou CEST).
