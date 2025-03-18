#!/bin/bash

# URL de la page CoinPaprika pour Cardano (ADA)
URL="https://coinpaprika.com/coin/ada-cardano/"

# Récupérer le HTML de la page
HTML=$(curl -s "$URL")

# Extraire le prix avec grep (il faut adapter la regex en fonction du HTML de la page)
PRICE=$(echo "$HTML" | grep -oP '(?<=<span class="text-xl font-bold">)[0-9]+\.[0-9]+')

# Vérification si le prix a bien été récupéré
if [[ -n "$PRICE" ]]; then
    # Afficher le prix
    echo "Prix actuel de Cardano (ADA) : $PRICE USD"

    # Sauvegarder dans un fichier CSV avec timestamp
    echo "$(date '+%Y-%m-%d %H:%M:%S'),$PRICE" >> /mnt/c/Users/mathi/crypto_scraper/crypto_scraper/prices.csv

    # Debug log pour vérifier l'ajout
    echo "Ajouté à prices.csv : $(date '+%Y-%m-%d %H:%M:%S'),$PRICE" >> /mnt/c/Users/mathi/crypto_scraper/debug.log
else
    # Enregistrer un message d'erreur si la récupération du prix échoue
    echo "Erreur : Prix non récupéré à $(date)" >> /mnt/c/Users/mathi/crypto_scraper/debug.log
fi
