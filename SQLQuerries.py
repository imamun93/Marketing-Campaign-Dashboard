# Set up directory structure and save SQL queries + Python dashboard script
import os
from pathlib import Path

base_path = Path("/marketing_campaign_dashboard")

# Define paths
sql_dir = base_path / "sql_queries"
dashboard_script_path = base_path / "campaign_dashboard.py"

# Create directories if they don't exist
sql_dir.mkdir(parents=True, exist_ok=True)
dashboard_script_path.parent.mkdir(parents=True, exist_ok=True)

# SQL queries to be saved
sql_queries = {
    "overall_performance.sql": """
-- Query to calculate key campaign performance metrics
SELECT
    campaign_id,
    COUNT(*) AS impressions,
    SUM(CASE WHEN clicked THEN 1 ELSE 0 END) AS clicks,
    SUM(CASE WHEN converted THEN 1 ELSE 0 END) AS conversions,
    ROUND(SUM(CASE WHEN converted THEN 1 ELSE 0 END) * 1.0 / NULLIF(SUM(CASE WHEN clicked THEN 1 ELSE 0 END), 0), 2) AS conversion_rate
FROM campaign_data
GROUP BY campaign_id;
""",
    "demographic_performance.sql": """
-- Query to analyze campaign effectiveness by demographic segment
SELECT
    campaign_id,
    gender,
    age_group,
    COUNT(*) AS impressions,
    SUM(CASE WHEN clicked THEN 1 ELSE 0 END) AS clicks,
    SUM(CASE WHEN converted THEN 1 ELSE 0 END) AS conversions
FROM campaign_data
GROUP BY campaign_id, gender, age_group
ORDER BY campaign_id, gender, age_group;
""",
    "channel_performance.sql": """
-- Query to evaluate performance by marketing channel
SELECT
    campaign_id,
    channel,
    COUNT(*) AS impressions,
    SUM(CASE WHEN clicked THEN 1 ELSE 0 END) AS clicks,
    SUM(CASE WHEN converted THEN 1 ELSE 0 END) AS conversions
FROM campaign_data
GROUP BY campaign_id, channel
ORDER BY campaign_id, channel;
"""
}

# Save each SQL query
for filename, content in sql_queries.items():
    with open(sql_dir / filename, "w") as f:
        f.write(content.strip())

# Create the Python dashboard script using Plotly Dash
dashboard_code = """
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
    database="campaign_db",
    user="postgre",
    password=1234
)

# Load data using SQL
df = pd.read_sql_query(\"\"\"
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
\"\"\", conn)

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
"""

# Save the dashboard Python script
with open(dashboard_script_path, "w") as f:
    f.write(dashboard_code.strip())

# Return final paths
sql_dir, dashboard_script_path
Result
(PosixPath('/marketing_campaign_dashboard/sql_queries'),
 PosixPath('/marketing_campaign_dashboard/campaign_dashboard'))