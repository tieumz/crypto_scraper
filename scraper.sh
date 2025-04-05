#!/bin/bash

# API officielle de CoinPaprika
URL="https://api.coinpaprika.com/v1/tickers/ada-cardano"

# Extraire le prix avec jq
PRICE=$(curl -s "$URL" | jq -r '.quotes.USD.price')

# Vérification du prix
if [[ -n "$PRICE" ]]; then
    echo "Prix actuel de Cardano (ADA) : $PRICE USD"
    echo "$(date '+%Y-%m-%d %H:%M:%S'),$PRICE" >> prices.csv
    echo "Ajouté à prices.csv : $(date '+%Y-%m-%d %H:%M:%S'),$PRICE" >> debug.log
else
    echo "Erreur : Prix non récupéré à $(date)" >> debug.log
fi
