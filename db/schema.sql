
DROP TABLE IF EXISTS campaign_data;
CREATE TABLE campaign_data (
    id SERIAL PRIMARY KEY,
    channel VARCHAR(50),
    campaign VARCHAR(50),
    impressions INT,
    clicks INT,
    conversions INT,
    cost FLOAT,
    revenue FLOAT,
    ctr FLOAT,
    cvr FLOAT,
    roas FLOAT,
    cpa FLOAT
);
