import pandas as pd
import os
from datetime import datetime

# Ensure the raw data folder exists
os.makedirs("Users/darrendavy/projects/data/raw", exist_ok=True)

# Load the original CSV
csv_path = "/Users/darrendavy/projects/nba2k25-pipeline/data/raw/current_nba_players.csv"
players_df = pd.read_csv(csv_path)

# Save a timestamped snapshot
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
snapshot_path = f"../data/raw/players_raw_{timestamp}.csv"
players_df.to_csv(snapshot_path, index=False)

print(f"Extraction complete: {len(players_df)} rows saved as {snapshot_path}")

