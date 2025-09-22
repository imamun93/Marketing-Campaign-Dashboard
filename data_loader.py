# load_data.py
import psycopg2
import csv

# --- Connection Details ---
conn = psycopg2.connect(
    host="localhost",
    database="marketing_dashboard",
    user="postgres",
    password="1234" # Use your actual password
)
cur = conn.cursor()

# --- File and Table Details ---
# IMPORTANT: Replace with the actual name of your CSV file
csv_file_name = 'simulated_campaign_data.csv' 
table_name = 'campaign_data'

# --- Load the Data ---
try:
    with open(csv_file_name, 'r') as f:
        # Skip the header row
        next(f) 
        # Use copy_from for efficient bulk loading
        # IMPORTANT: Based on your sample, the delimiter is a tab ('\t'). 
        # If it's a comma, change to ','
        cur.copy_from(f, table_name, sep=',', columns=(
            'channel', 'campaign', 'impressions', 'clicks', 'conversions', 
            'cost', 'revenue', 'ctr', 'cvr', 'roas', 'cpa'
        ))
    
    conn.commit()
    cur.execute(f"SELECT COUNT(*) FROM {table_name};")
    row_count = cur.fetchone()[0]
    print(f"✅ Successfully loaded {row_count} rows into the '{table_name}' table.")

except Exception as e:
    conn.rollback()
    print(f"❌ Error loading data: {e}")

finally:
    cur.close()
    conn.close()