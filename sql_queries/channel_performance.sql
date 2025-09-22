SELECT
        campaign,
        channel,
        SUM(clicks) AS clicks,
        SUM(conversions) AS conversions,
        ROUND(SUM(conversions)::numeric / NULLIF(SUM(clicks),0), 4) AS cvr
    FROM campaign_data
    GROUP BY campaign, channel
    ORDER BY campaign, channel;