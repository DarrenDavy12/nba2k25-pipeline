import pandas as pd
from sqlalchemy import create_engine
from dash import Dash, dcc, html, Input, Output
import plotly.express as px




# Filters: Multi-select dropdowns for Team, Position Group, Rating Bucket

# Charts:
# Top 10 players by overall rating (colored by rating bucket)
# Histogram of overall ratings
# Bar chart of number of players per team
# KPI cards: Shows Average Rating, Tallest Player, and total number of players
# NBA colors: Simple red/orange/yellow/green/gray for rating bucket

# ---- Database connection ----
DB_USER = "darrendavy"
DB_PASS = "IgTiYzXEYDs"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "nba2k25"

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# ---- Load cleaned data ----
query = "SELECT * FROM players_clean"
df = pd.read_sql(query, engine)

# ---- Dash app ----
app = Dash(__name__)
server = app.server  # for deployment later if needed

# Dropdown options
teams = [{'label': t, 'value': t} for t in sorted(df['team'].unique())]
positions = [{'label': p, 'value': p} for p in sorted(df['position_group'].unique())]
ratings = [{'label': r, 'value': r} for r in sorted(df['rating_bucket'].unique())]

app.layout = html.Div(style={'font-family':'Arial', 'padding':'20px'}, children=[
    html.H1("NBA 2K25 Player Stats Dashboard", style={'color':'#0B3D91'}),
    html.Div("Interactive dashboard showcasing current NBA 2K25 players.", style={'margin-bottom':'20px'}),

    # Filters
    html.Div([
        html.Div([
            html.Label("Team"),
            dcc.Dropdown(id='team_filter', options=teams, multi=True)
        ], style={'width':'30%', 'display':'inline-block', 'margin-right':'20px'}),
        html.Div([
            html.Label("Position Group"),
            dcc.Dropdown(id='position_filter', options=positions, multi=True)
        ], style={'width':'30%', 'display':'inline-block', 'margin-right':'20px'}),
        html.Div([
            html.Label("Rating Bucket"),
            dcc.Dropdown(id='rating_filter', options=ratings, multi=True)
        ], style={'width':'30%', 'display':'inline-block'})
    ], style={'margin-bottom':'30px'}),

    # KPI cards
    html.Div(id='kpi_cards', style={'display':'flex', 'justify-content':'space-between', 'margin-bottom':'30px'}),

    # Charts
    html.Div([
        dcc.Graph(id='top10_players'),
        dcc.Graph(id='rating_histogram'),
        dcc.Graph(id='team_counts')
    ])
])

# ---- Callbacks ----
@app.callback(
    Output('top10_players', 'figure'),
    Output('rating_histogram', 'figure'),
    Output('team_counts', 'figure'),
    Output('kpi_cards', 'children'),
    Input('team_filter', 'value'),
    Input('position_filter', 'value'),
    Input('rating_filter', 'value')
)
def update_dashboard(selected_teams, selected_positions, selected_ratings):
    filtered = df.copy()
    if selected_teams: filtered = filtered[filtered['team'].isin(selected_teams)]
    if selected_positions: filtered = filtered[filtered['position_group'].isin(selected_positions)]
    if selected_ratings: filtered = filtered[filtered['rating_bucket'].isin(selected_ratings)]

    # Top 10 players by overall
    top10 = filtered.nlargest(10, 'overall')
    fig_top10 = px.bar(top10, x='name', y='overall', title='Top 10 Players by Overall',
                       color='rating_bucket', color_discrete_map={'Elite':'#FF4136','Great':'#FF851B','Good':'#FFDC00','Average':'#2ECC40','Below Average':'#AAAAAA'})

    # Histogram of overall ratings
    fig_hist = px.histogram(filtered, x='overall', nbins=10, title='Overall Ratings Distribution')

    # Team counts
    team_count = filtered['team'].value_counts().reset_index()
    team_count.columns = ['team','count']
    fig_team = px.bar(team_count, x='team', y='count', title='Players per Team', color='count', color_continuous_scale='Blues')

    # KPI cards
    avg_rating = filtered['overall'].mean() if not filtered.empty else 0
    tallest = filtered['height_cm'].max() if not filtered.empty else 0
    num_players = len(filtered)
    kpis = [
        html.Div([html.H4("Average Rating"), html.P(f"{avg_rating:.2f}")], style={'padding':'10px','border':'1px solid #ccc','border-radius':'5px','width':'30%'}),
        html.Div([html.H4("Tallest Player (cm)"), html.P(f"{tallest}")], style={'padding':'10px','border':'1px solid #ccc','border-radius':'5px','width':'30%'}),
        html.Div([html.H4("Number of Players"), html.P(f"{num_players}")], style={'padding':'10px','border':'1px solid #ccc','border-radius':'5px','width':'30%'})
    ]

    return fig_top10, fig_hist, fig_team, kpis

# ---- Run app ----
if __name__ == "__main__":
    app.run(debug=True)
