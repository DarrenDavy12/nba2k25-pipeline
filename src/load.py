import pandas as pd
from sqlalchemy import create_engine
import os

# Database connection details
DB_USER = "darrendavy"  # usually your Mac username
DB_PASS = "IgTiYzXEYDs"                   # leave blank if no password
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "nba2k25"

# CSV file to load
csv_folder = "/Users/darrendavy/projects/nba2k25-pipeline/data/clean"
# pick the latest cleaned CSV
clean_csv = sorted([f for f in os.listdir(csv_folder) if f.startswith("clean_current_nba_players")])[-1]
csv_path = os.path.join(csv_folder, clean_csv)

# Load CSV into pandas
df = pd.read_csv(csv_path)

# Create SQLAlchemy engine
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Load into SQL table (replace if exists)
table_name = "current_nba_players"
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Loaded {len(df)} rows into table '{table_name}' in database '{DB_NAME}'")
print(df.columns.tolist())
