import pandas as pd
from sqlalchemy import create_engine

# ---- Database connection ----
DB_USER = "<mac_username>"         # your Mac username
DB_PASS = "<server_pwd>"       # the password you set
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "nba2k25"

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# ---- Load cleaned CSV ----
csv_path = "../data/clean/players_clean.csv"
df = pd.read_csv(csv_path)

# ---- Load into Postgres ----
table_name = "players_clean"
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Loaded {len(df)} rows into table '{table_name}' in database '{DB_NAME}'")
