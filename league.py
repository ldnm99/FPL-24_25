import sys
import os

# Add the parent directory of 'src' to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import fetch_data,save_csv

# Define URLs
BASE_URL            = "https://draft.premierleague.com/api"

#Our league ID you can change it to your league ID
LEAGUE_ID           = '70113'

#Endpoint to get league data info like standings
LEAGUE_DETAILS_URL  = f"{BASE_URL}/league/"f"{LEAGUE_ID}/details"

#Gets the current league standings and saves into a CSV file  called league_standings.csv in data folder
def get_league_standings():
    """
    Fetches the league standings data, processes it, and saves it to a CSV file.

    This function performs the following steps:
    1. Fetches the league data from a specified URL.
    2. Extracts the standings information from the fetched data.
    3. Processes the standings data to extract relevant fields.
    4. Saves the processed standings data to a CSV file.
    5. Returns the standings data as a pandas DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing the league standings with columns:
                      ['manager_id', 'ID', 'First Name', 'Last Name', 'short_name', 'waiver_pick', 'Team Name']
    """
    data = fetch_data(LEAGUE_DETAILS_URL.format(league_id=LEAGUE_ID))
    if data:
        standings = data.get('league_entries', [])
        standings_data = [
            [entry['entry_id'],
             entry['id'], 
             entry['player_first_name'],
             entry['player_last_name'],
             entry['short_name'],
             entry['waiver_pick'],
             entry['entry_name']]
            for entry in standings
        ]
        headers = ['manager_id', 'ID','First Name', 'Last Name','short_name','waiver_pick','Team Name']
        save_csv('Data/league_standings.csv', headers, standings_data)
