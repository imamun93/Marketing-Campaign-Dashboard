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