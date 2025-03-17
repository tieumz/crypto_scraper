#!/bin/bash

# URL de la page CoinPaprika pour Cardano (ADA)
URL="https://coinpaprika.com/coin/ada-cardano/"

# Récupérer le HTML de la page
HTML=$(curl -s "$URL")

# Extraire le prix depuis la balise <span class="font-bold">
PRICE=$(echo "$HTML" | grep -oP '(?<=<span data-recalc=")[0-9]+\.[0-9]+')

# Afficher le prix
echo "Prix actuel de Cardano (ADA) : $PRICE USD"

# Sauvegarder dans un fichier CSV avec timestamp
echo "$(date +'%Y-%m-%d %H:%M:%S'),$PRICE" >> prices.csv
