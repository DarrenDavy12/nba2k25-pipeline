# 🏀 NBA 2K25 Player Data Pipeline

## 📌 Project Overview

This project is an **end-to-end data engineering pipeline** that ingests, transforms, and loads NBA 2K25 player data into a **PostgreSQL database** and exposes it for basic analytics.  

The goal is to demonstrate **core data engineering skills**: data ingestion, transformation, validation, storage, and simple visualization.

---

## 🏗️ Architecture

**High-level flow:**

1. **Extract** – Python script loads CSV of NBA 2K25 player data  
2. **Bronze Layer** – Timestamped raw CSV snapshot saved locally  
3. **Silver Layer** – Cleaned and validated dataset  
4. **Load** – Data loaded into PostgreSQL database  
5. **Analytics** – Query top players, stats, and trends  
6. **Dashboard** – Simple interactive visualization using Plotly/Dash


```markdown
CSV / API
↓
Raw CSV (Bronze)
↓
Clean Data (Silver)
↓
PostgreSQL Database
↓
Plotly/Dash Dashboard


---

## 🛠️ Tech Stack

- 🐍 **Python & pandas** – data extraction and transformation  
- 🐘 **PostgreSQL** – relational storage  
- 🛠️ **SQLAlchemy** – Python → PostgreSQL connection  
- 📊 **Plotly / Dash** – interactive dashboard  
- 🔧 **Git & GitHub** – version control  

---

## 📂 Repository Structure

```markdown
nba2k25-pipeline/
│
├── data/
│ ├── raw/ # Raw CSV snapshots
│ └── clean/ # Cleaned CSV outputs
│
├── src/
│ ├── extract.py # Load raw CSV
│ ├── transform.py # Clean & validate data
│ └── load.py # Load into PostgreSQL
│
├── dashboard/
│ └── app.py # Plotly/Dash dashboard
│
├── README.md
└── requirements.txt


---

## 🔄 Data Pipeline Steps

### 1️⃣ Extract

- Reads CSV of NBA 2K25 player stats  
- Saves timestamped snapshot for auditability

### 2️⃣ Transform

- Cleans missing values and duplicates  
- Normalizes column names  
- Computes derived fields (if needed)  

### 3️⃣ Load

- Loads data into PostgreSQL tables using SQLAlchemy  
- Database schema enforces data types

### 4️⃣ Analytics / Dashboard

- Query database for:
  - 🏆 Top players by overall rating  
  - 📊 Team stats  
  - 🏀 Positional and archetype trends  
- Interactive dashboard visualizes trends

---

## ✅ Data Quality Checks

- ❌ No missing critical fields (`name`, `team`, `overall`)  
- ❌ Duplicate rows removed  
- ✅ Numeric columns validated for realistic ranges  

Failures are logged to console.

---

## 🚀 How to Run

1. **Create a virtual environment:**

```bash
python3 -m venv nba_venv
source nba_venv/bin/activate



2. **Create a virtual environment:**

``` bash
pip install -r requirements.txt



3. **Run extraction:**

```bash
python3 src/extract.py



4. **Run transformation:**

```bash
python3 src/transform.py



5. **Load data into PostgreSQL:**

```bash
python3 src/load.py



6. **Launch dashboard:**

```bash
python3 dashboard/app.py




