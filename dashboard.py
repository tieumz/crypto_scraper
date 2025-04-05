import dash
from dash import dcc, html
import pandas as pd
import numpy as np
import plotly.express as px

# Fonction pour charger les données
def load_data():
    try:
        df = pd.read_csv("prices.csv", names=["datetime", "price"])
        df["datetime"] = pd.to_datetime(df["datetime"])  # Convertir en format date
        df = df.dropna()  # Supprimer les lignes avec valeurs manquantes
        df = df[df["price"] > 0]  # Garder uniquement les prix positifs
        df = df.sort_values("datetime")  # Trier par date
        print(df.tail())  # DEBUG : Vérifier les 5 dernières valeurs
        return df
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
        return pd.DataFrame(columns=["datetime", "price"])

# Fonction pour le résumé quotidien
def generate_daily_summary(df):
    now = pd.Timestamp.now()
    today = now.date()
    df_today = df[df["datetime"].dt.date == today]

    if now.hour < 20:
        return "Le résumé sera disponible à partir de 20h UTC."

    if df_today.empty:
        return "Aucune donnée disponible pour aujourd’hui."

    open_price = df_today.iloc[0]["price"]
    close_price = df_today.iloc[-1]["price"]
    change_pct = ((close_price - open_price) / open_price) * 100
    volatility = df_today["price"].std()

    summary = f""" Résumé du {today.strftime('%d/%m/%Y')} :
- Prix d'ouverture : {open_price:.4f} USD
- Prix de clôture : {close_price:.4f} USD
- Évolution : {change_pct:.2f} %
- Volatilité : {volatility:.6f}"""

    return summary

# Initialiser l'application Dash
app = dash.Dash(__name__)
app.title = "Cardano Dashboard"

# Layout
app.layout = html.Div([
    html.H1(id="title", children="Prix de Cardano (ADA) en Temps Réel"),
    dcc.Graph(id="price-chart"),
    html.Pre(id="daily-summary", style={"whiteSpace": "pre-wrap", "fontSize": "16px"}),
    dcc.Interval(id="interval-update", interval=5*60*1000, n_intervals=0)
])

# Callback principal
@app.callback(
    [dash.Output("price-chart", "figure"),
     dash.Output("title", "children"),
     dash.Output("daily-summary", "children")],
    [dash.Input("interval-update", "n_intervals")]
)
def update_dashboard(n):
    print(f" Callback exécuté, intervalle {n}")  # DEBUG
    df = load_data()

    if df.empty:
        return px.line(), "Prix de Cardano (ADA) en Temps Réel", "Pas encore de données disponibles"

    fig = px.line(df, x="datetime", y="price", title="Évolution du prix de Cardano (ADA)")

    last_update = df["datetime"].iloc[-1].strftime("%H:%M")
    title = f"Prix de Cardano (ADA) en Temps Réel (Dernière mise à jour : {last_update})"

    summary = generate_daily_summary(df)

    return fig, title, summary

if __name__ == "__main__":
    print(" Dashboard en cours d'exécution...")
    app.run(debug=True, host="0.0.0.0", port=8050, threaded=True)

