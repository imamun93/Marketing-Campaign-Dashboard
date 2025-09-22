# SQLQueries.py
# Save useful SQL queries into /sql_queries folder

from pathlib import Path

# Relative path for GitHub friendliness
base_path = Path(__file__).parent
sql_dir = base_path / "sql_queries"
sql_dir.mkdir(parents=True, exist_ok=True)

sql_queries = {
    "overall_performance.sql": """
    SELECT
        campaign,
        COUNT(*) AS impressions,
        SUM(clicks) AS clicks,
        SUM(conversions) AS conversions,
        ROUND(SUM(conversions)::numeric / NULLIF(SUM(clicks),0), 4) AS conversion_rate,
        ROUND(SUM(revenue)::numeric / NULLIF(SUM(cost),0), 2) AS roas,
        ROUND(SUM(cost)::numeric / NULLIF(SUM(conversions),0), 2) AS cpa
    FROM campaign_data
    GROUP BY campaign;
    """,
    "channel_performance.sql": """
    SELECT
        campaign,
        channel,
        SUM(clicks) AS clicks,
        SUM(conversions) AS conversions,
        ROUND(SUM(conversions)::numeric / NULLIF(SUM(clicks),0), 4) AS cvr
    FROM campaign_data
    GROUP BY campaign, channel
    ORDER BY campaign, channel;
    """
}

for filename, content in sql_queries.items():
    with open(sql_dir / filename, "w") as f:
        f.write(content.strip())

print(f"SQL queries saved in {sql_dir}")
