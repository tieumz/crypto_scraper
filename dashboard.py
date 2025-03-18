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
        print(df.tail())  # DEBUG : Vérifier les 5 dernières valeurs
        return df
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
        return pd.DataFrame(columns=["datetime", "price"])

# Initialiser l'application Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(id="title", children="Prix de Cardano (ADA) en Temps Réel"),
    
    dcc.Graph(id="price-chart"),
    
    html.Pre(id="daily-summary", style={"white-space": "pre-wrap", "font-size": "16px"}),

    # Ajout d'un intervalle pour rafraîchir les données toutes les 5 minutes
    dcc.Interval(
        id="interval-update",
        interval=5*60*1000,  # Mise à jour toutes les 5 minutes
        n_intervals=0
    )
])

# Callback pour mettre à jour le graphique et le résumé quotidien
@app.callback(
    [dash.Output("price-chart", "figure"),
     dash.Output("title", "children"),
     dash.Output("daily-summary", "children")],
    [dash.Input("interval-update", "n_intervals")]
)
def update_dashboard(n):
    print(f" Callback exécuté, intervalle {n}")  # DEBUG : Voir si le callback est déclenché
    df = load_data()

    if df.empty:
        return px.line(), "Prix de Cardano (ADA) en Temps Réel", "Pas encore de données disponibles"

    fig = px.line(df, x="datetime", y="price", title="Évolution du prix de Cardano (ADA)")

    # Titre dynamique
    last_update = df["datetime"].iloc[-1].strftime("%H:%M")
    title = f"Prix de Cardano (ADA) en Temps Réel (Dernière mise à jour : {last_update})"

    return fig, title, "Mise à jour réussie"

if __name__ == "__main__":
    print(" Dashboard en cours d'exécution...")
    app.run_server(debug=True, host="0.0.0.0", port=8050, threaded=True)
