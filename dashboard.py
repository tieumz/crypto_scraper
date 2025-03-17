import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime
import numpy as np

# Charger les données du fichier CSV
def load_data():
    df = pd.read_csv("prices.csv", names=["datetime", "price"])
    df["datetime"] = pd.to_datetime(df["datetime"])  # Convertir en format date
    return df

# Initialiser l'application Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(id="title", style={'textAlign': 'left', 'font-weight': 'bold'}),
    
    dcc.Graph(id="price-chart"),

    dcc.Interval(
        id="interval-update",
        interval=5*60*1000,  # Met à jour toutes les 5 minutes
        n_intervals=0
    ),

    html.H3("Résumé de la journée :"),
    html.Div(id="daily-summary"),
])

# Callback pour mettre à jour le graphique et le résumé quotidien
@app.callback(
    [dash.Output("price-chart", "figure"),
     dash.Output("title", "children"),
     dash.Output("daily-summary", "children")],
    [dash.Input("interval-update", "n_intervals")]
)
def update_dashboard(n):
    df = load_data()
    
    if df.empty:
        return go.Figure(), "Prix de Cardano (ADA) en Temps Réel", "Pas de données disponibles"
    
    # Déterminer la couleur de la ligne
    colors = ["green" if df["price"].iloc[i] >= df["price"].iloc[i-1] else "red" for i in range(1, len(df))]
    colors.insert(0, "blue")  # Première valeur en bleu
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["datetime"],
        y=df["price"],
        mode="lines+markers",
        line=dict(color="blue"),
        marker=dict(color=colors, size=8)
    ))
    
    fig.update_layout(
        title="Évolution du prix de Cardano (ADA)",
        xaxis_title="Temps",
        yaxis_title="Prix (USD)",
        template="plotly_white"
    )
    
    # Titre dynamique
    last_update = df["datetime"].iloc[-1].strftime("%H:%M")
    title = f"Prix de Cardano (ADA) en Temps Réel (Dernière mise à jour : {last_update})"
    
    # Résumé quotidien (mis à jour à 20h)
    daily_summary = "Pas encore de résumé disponible"
    if df["datetime"].dt.hour.max() >= 20:
        today_df = df[df["datetime"].dt.date == df["datetime"].max().date()]
        open_price = today_df["price"].iloc[0]
        close_price = today_df["price"].iloc[-1]
        daily_change = (close_price - open_price) / open_price * 100
        volatility = np.std(today_df["price"]) * 100
        
        daily_summary = (
            f"Prix d'ouverture : {open_price:.4f} USD\n"
            f"Prix de clôture : {close_price:.4f} USD\n"
            f"Variation : {daily_change:.2f}% {'🔼' if daily_change > 0 else '🔽'}\n"
            f"Volatilité : {volatility:.2f}%"
        )
    
    return fig, title, daily_summary

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
