# 🏀 NBA 2K25 Player Data Pipeline

An end-to-end data engineering project demonstrating extraction, transformation, and loading (ETL) of NBA 2K25 player data, with an interactive dashboard.

## 🏀 Project Overview

This project:

1. Extracts raw NBA 2K25 player data from CSV.
2. Transforms the data:
   - Cleans and fills missing values
   - Adds derived columns (BMI, rating buckets, position group, salary in millions)
3. Loads cleaned data into PostgreSQL
4. Provides an interactive dashboard built with Dash & Plotly:
   - Top 10 players by overall rating
   - Overall rating distribution
   - Number of players per team
   - KPI cards: Average Rating, Tallest Player, Total Players
   - Filters by team, position, and rating bucket

## 📂 Repo Structure

data/ # raw and cleaned CSVs
src/ # ETL scripts
dashboard/ # Dash app


## ⚡ How to Run




1. Clone the repo

```bash
python3 -m venv nba_venv
source nba_venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Run extraction:

python3 src/extract.py


Run transformation:

python3 src/transform.py


Load data into PostgreSQL:

python3 src/load.py


Launch dashboard:

python3 dashboard/app.py



5. Open link in browser 
Open your browser at: http://127.0.0.1:8050/




🛠 Tech Stack

Python, pandas

PostgreSQL + SQLAlchemy

Dash + Plotly for visualization



🎯 Key Skills Demonstrated

End-to-end data engineering workflow

Data cleaning & transformation

Database loading & schema design

Interactive dashboard creation with filters, charts, and KPI cards

Professional repository organization




📸 Screenshots - Check images folder to see screenshots! 







