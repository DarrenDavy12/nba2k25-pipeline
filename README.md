# NBA 2K25 Pipeline

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

# raw and cleaned CSVs
data/ 

# ETL scripts
src/ 


# Dash app
dashboard/





## ⚡ How to Run

1. Clone the repo

```bash
git clone https://github.com/DarrenDavy12/nba2k25-pipeline.git
cd nba2k25-pipeline



2. Create a virtual environment

python3 -m venv nba_venv
source nba_venv/bin/activate
pip install -r requirements.txt



3. Run ETL scripts

python3 src/extract.py
python3 src/transform.py
python3 src/load_clean.py




4. Launch the dashboard

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







