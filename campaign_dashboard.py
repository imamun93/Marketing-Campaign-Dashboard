# campaign_dashboard.py
# Simple Plotly Dash dashboard for PostgreSQL marketing campaign analysis

import dash
from dash import dcc, html
import dash_table
import plotly.express as px
import pandas as pd
import psycopg2

# Establish database connection
conn = psycopg2.connect(
    host="localhost",
    database="db/schema.sql",
    user="postgres",
    password=1234
)

# Load data using SQL
df = pd.read_sql_query("""
    SELECT
        campaign_id,
        channel,
        gender,
        age_group,
        COUNT(*) AS impressions,
        SUM(CASE WHEN clicked THEN 1 ELSE 0 END) AS clicks,
        SUM(CASE WHEN converted THEN 1 ELSE 0 END) AS conversions
    FROM campaign_data
    GROUP BY campaign_id, channel, gender, age_group;
""", conn)

df['CTR'] = df['clicks'] / df['impressions']
df['CVR'] = df['conversions'] / df['clicks']

# Initialize app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Marketing Campaign Performance Dashboard"),

    dcc.Dropdown(
        id="campaign_dropdown",
        options=[{"label": c, "value": c} for c in df["campaign_id"].unique()],
        value=df["campaign_id"].unique()[0]
    ),

    dcc.Graph(id="channel_chart"),

    dcc.Graph(id="cvr_chart")
])

@app.callback(
    dash.dependencies.Output("channel_chart", "figure"),
    [dash.dependencies.Input("campaign_dropdown", "value")]
)
def update_channel_chart(campaign_id):
    filtered = df[df["campaign_id"] == campaign_id]
    fig = px.bar(filtered, x="channel", y="CTR", color="gender", barmode="group",
                 title=f"Click-Through Rate by Channel - Campaign {campaign_id}")
    return fig

@app.callback(
    dash.dependencies.Output("cvr_chart", "figure"),
    [dash.dependencies.Input("campaign_dropdown", "value")]
)
def update_cvr_chart(campaign_id):
    filtered = df[df["campaign_id"] == campaign_id]
    fig = px.bar(filtered, x="age_group", y="CVR", color="channel", barmode="group",
                 title=f"Conversion Rate by Age Group - Campaign {campaign_id}")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)