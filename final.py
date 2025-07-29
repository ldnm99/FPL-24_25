import pandas as pd
from utils import fetch_data, fetch_managers_ids, get_player_gw_data

# Define URLs
BASE_URL            = "https://draft.premierleague.com/api"
GW_URL              = f"{BASE_URL}/event/"
TEAMS_URL           = f"{BASE_URL}/entry/"
GAME_STATUS_URL     = f"{BASE_URL}/game"

combined_data = []
current_gameweek = fetch_data(GAME_STATUS_URL)['current_event']

# Get managers IDs from the CSV file
managers_ids = fetch_managers_ids()

# Load player names from CSV
players_df = pd.read_csv("Data/players_data.csv")
players_df['player_name'] = players_df['First_Name'] + ' ' + players_df['Last_Name']
players_df = players_df[['ID', 'player_name']]
players_df['ID'] = players_df['ID'].astype(int)  # Ensure ID type matches for merge

def main():
    """Main function to fetch player stats and merge with managers' teams."""
    print("Starting final data processing...")
    print('----------------------------------------------------------------------')

    # Loop through each gameweek
    for gw in range(1, current_gameweek + 1):
        """Fetch player stats and merge them with each manager's team picks for each gameweek."""
        gw_stats = get_player_gw_data(gw)
        gw_stats['gameweek'] = gw
        gw_stats = gw_stats[['ID', 'gameweek', 'minutes', 'goals_scored', 'assists', 'bonus',
                             'clean_sheets', 'expected_goals', 'expected_assists',
                             'expected_goal_involvements', 'expected_goals_conceded', 'total_points']]

        gw_stats['ID'] = gw_stats['ID'].astype(int)
        gw_stats['gameweek'] = gw_stats['gameweek'].astype(int)

        # Merge player names
        gw_stats = gw_stats.merge(players_df, on='ID', how='left')

        # Fetch each manager's team picks for each gameweek
        for manager_id in managers_ids:
            team_data = fetch_data(f"{TEAMS_URL}{manager_id}/event/{gw}")
            if not team_data or 'picks' not in team_data:
                continue
            
            picks = pd.DataFrame(team_data['picks'])
            picks['manager_id'] = manager_id
            picks['gameweek'] = gw
            picks.rename(columns={'element': 'ID', 'position': 'team_position'}, inplace=True)

            picks['ID'] = picks['ID'].astype(int)
            picks['gameweek'] = picks['gameweek'].astype(int)

            # Merge gameweek picks with stats + player name
            merged = picks.merge(gw_stats, on=['ID', 'gameweek'], how='left')
            combined_data.append(merged)

    # Concatenate all manager-team-player-gameweek data
    final_df = pd.concat(combined_data, ignore_index=True)

    # Save to CSV
    final_df.to_csv("Data/final_data.csv", index=False)
    print("Saved final_data.csv")
