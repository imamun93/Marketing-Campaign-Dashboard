# campaign_dashboard.py
# Plotly Dash dashboard for PostgreSQL marketing campaign analysis

import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import psycopg2

# Establish database connection
conn = psycopg2.connect(
    host="localhost",
    database="marketing_dashboard",
    user="postgres",
    password="1234"
)

# Load data into Pandas
df = pd.read_sql_query("""
    SELECT * FROM campaign_data;
""", conn)

conn.close()

# Derived metrics for KPIs
df['CTR'] = df['clicks'] / df['impressions']
df['CVR'] = df['conversions'] / df['clicks']
df['ROAS'] = df['revenue'] / df['cost']
df['CPA'] = df['cost'] / df['conversions']

# Initialize app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("📊 Marketing Campaign Performance Dashboard"),

    dcc.Dropdown(
        id="campaign_dropdown",
        options=[{"label": c, "value": c} for c in df["campaign"].unique()],
        value=df["campaign"].unique()[0]
    ),

    dcc.Graph(id="channel_chart"),
    dcc.Graph(id="cvr_chart")
])

@app.callback(
    dash.dependencies.Output("channel_chart", "figure"),
    [dash.dependencies.Input("campaign_dropdown", "value")]
)
def update_channel_chart(campaign):
    filtered = df[df["campaign"] == campaign]
    fig = px.bar(filtered, x="channel", y="CTR", color="channel",
                 title=f"CTR by Channel - {campaign}")
    return fig

@app.callback(
    dash.dependencies.Output("cvr_chart", "figure"),
    [dash.dependencies.Input("campaign_dropdown", "value")]
)
def update_cvr_chart(campaign):
    filtered = df[df["campaign"] == campaign]
    fig = px.bar(filtered, x="channel", y="CVR", color="channel",
                 title=f"CVR by Channel - {campaign}")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
