
# 📊 Marketing Campaign Dashboard (PostgreSQL + Python)

## Objective
Build a fully-functional marketing campaign analytics dashboard pipeline that simulates data, stores it in PostgreSQL, performs analytics via SQL, and visualizes insights using Python (Plotly/Streamlit).

## Features
- Simulated multi-channel marketing campaign data
- PostgreSQL schema & ingestion
- SQL queries for KPIs (CTR, CVR, CPA, ROAS)
- Python-powered analytics & visualization
- Modular, production-ready project structure

## Dataset Fields
- `channel`, `campaign`, `impressions`, `clicks`, `conversions`, `cost`, `revenue`
- Derived: `ctr`, `cvr`, `roas`, `cpa`

## Metrics & Goals
- **CTR (Click-Through Rate)**: `clicks / impressions`
- **CVR (Conversion Rate)**: `conversions / clicks`
- **ROAS (Return on Ad Spend)**: `revenue / cost`
- **CPA (Cost per Acquisition)**: `cost / conversions`

## Statistical Significance Steps
1. Simulate A/B channels with varying performance
2. Apply t-tests or proportion Z-tests to test CTR/CVR differences
3. Calculate confidence intervals for CPA & ROAS
4. Visualize results with distribution plots

## Files Included
- `/data`: Simulated campaign CSV
- `/db`: PostgreSQL schema
- `/scripts`: Simulation, ingestion, query logic
- `/dashboard`: Python dashboard using Plotly

## Requirements
- Python 3.8+
- PostgreSQL
- pandas, numpy, plotly, psycopg2, sqlalchemy

## How to Run
1. Run `simulate_campaign_data.py`
2. Create PostgreSQL DB & run `schema.sql`
3. Execute `insert_to_postgres.py` to load data
4. Run `query_postgres.py` for analysis
5. Launch `dashboard.py` to view metrics
