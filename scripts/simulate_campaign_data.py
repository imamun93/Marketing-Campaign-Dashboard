
""" Simulate marketing campaign data with metrics """
import pandas as pd
import numpy as np

np.random.seed(0)
n = 1000
channels = ['Email', 'Social', 'Search', 'Display']
data = {
    'channel': np.random.choice(channels, n),
    'campaign': [f'Campaign_{i%5}' for i in range(n)],
    'impressions': np.random.randint(1000, 10000, size=n),
    'clicks': np.random.randint(100, 1000, size=n),
    'conversions': np.random.randint(10, 200, size=n),
    'cost': np.random.uniform(500, 5000, size=n),
    'revenue': np.random.uniform(1000, 10000, size=n)
}
df = pd.DataFrame(data)
df['ctr'] = df['clicks'] / df['impressions']
df['cvr'] = df['conversions'] / df['clicks']
df['roas'] = df['revenue'] / df['cost']
df['cpa'] = df['cost'] / df['conversions']
df.to_csv('../simulated_campaign_data.csv', index=False)
