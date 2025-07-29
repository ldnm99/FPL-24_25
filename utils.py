import sys
import os
import sqlite3
import pandas as pd
import requests
import csv

# Add the parent directory of 'src' to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Database file
DB_FILE = "fpl_data.db"
# Define URLs
BASE_URL        = "https://draft.premierleague.com/api"

#Player data from the gameweek endpoint
GW_URL      = f"{BASE_URL}/event/"

session = requests.session()

def fetch_data(url):
    response = session.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {url}, status code: {response.status_code}")
        return None
    
def save_csv(filename, headers, rows):
    """Save data to a CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(headers)
        csv_writer.writerows(rows)

def fetch_managers_ids():
    """Fetch the list of manager IDs from the league_standings.csv file."""
    df = pd.read_csv('data/league_standings.csv')
    return df['manager_id'].dropna().unique().tolist()
    
def fetch_players_data():
    """Fetch player data from the players_data table."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players_data")
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    conn.close()
    # Convert data to a DataFrame
    players_df = pd.DataFrame(rows, columns=columns)
    return players_df

#Gets all the players data from a gameweek and returns a dataframe
def get_player_gw_data(gameweek):
    records = []
    data = fetch_data(GW_URL + str(gameweek) + "/live")
    
    for player_id, value in data['elements'].items():
        stats             = value['stats']
        stats['ID']       = player_id       # Add player ID to stats
        stats['gameweek'] = gameweek        # Add gameweek number
        records.append(stats)
    df = pd.DataFrame(records)
    
    return df