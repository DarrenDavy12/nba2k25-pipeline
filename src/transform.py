import pandas as pd
import os

# ---- Paths ----
raw_path = "../data/raw/current_nba_players.csv"
clean_path = "../data/clean/players_clean.csv"


os.makedirs("data/clean", exist_ok=True)

# ---- Load raw ----
df = pd.read_csv(raw_path)

# ---- Drop useless columns ----
df = df.drop(columns=["Unnamed: 0"], errors="ignore")

# ---- Feature Engineering ----

# Rating bucket
def bucket_rating(r):
    if r >= 90: 
        return "Elite"
    if r >= 80:
        return "Great"
    if r >= 70:
        return "Good"
    if r >= 60:
        return "Average"
    return "Below Average"

df["rating_bucket"] = df["overall"].apply(bucket_rating)

# Salary in millions
df["salary_million"] = df["season_salary"] / 1_000_000

# Position group
def position_group(pos):
    if pos in ["PG", "SG"]:
        return "Guard"
    if pos in ["SF", "PF"]:
        return "Wing"
    return "Big"

df["position_group"] = df["position_1"].apply(position_group)

# BMI
df["bmi"] = df["weight_kg"] / (df["height_cm"]/100)**2

# ---- Fill missing values ----
df = df.fillna({
    "nationality_2": "None",
    "position_2": "None",
    "prior_to_nba": "Unknown"
})

# ---- Save cleaned data ----
df.to_csv(clean_path, index=False)

print(f"Transformation complete. Saved cleaned dataset to: {clean_path}")
print(df.head())
print(df.shape)
