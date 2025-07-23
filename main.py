import os
# Importing functions from other modules
import league, players
###########################################################Endpoints###########################################################
# Define URLs
BASE_URL            = "https://draft.premierleague.com/api"

#Our league ID 
LEAGUE_ID           = '70113'

#Endpoint to get league data info like standings
LEAGUE_DETAILS_URL  = f"{BASE_URL}/league/"f"{LEAGUE_ID}/details"

#Endpoint to get the managers teams for each gameweek
TEAMS_URL           = f"{BASE_URL}/entry/"

#Endpoint to get the current gameweek
GAME_STATUS_URL     = f"{BASE_URL}/game"

#Player data from the gameweek endpoint
GW_URL              = f"{BASE_URL}/event/"

#Player data endpoint
PLAYER_DATA_URL     = f"{BASE_URL}/bootstrap-static"
#################################################################################################################################

# Main function to execute the data extraction script
def main():
    """
    Main function to execute the data extraction script.
    This function performs the following tasks:
    1. Prints a starting message.
    2. Ensures the 'Data' directory exists.
    3. Fetches and saves league standings data.
    4. Fetches and saves player data.
    5. Prints a completion message.
    6. Saves the data as CSV files in the 'Data' folder.
    Returns:
        None
    """

    print("Starting data extraction script...")
    print('----------------------------------------------------------------------')

    # Ensure the data directory exists
    if not os.path.exists('Data'):
        os.makedirs('Data', exist_ok=True)

    # Fetch and save league standings data with just managers' information
    print("Fetching league standings data...")
    league.get_league_standings()
    print('----------------------------------------------------------------------')
    players.get_player_data()
    print('----------------------------------------------------------------------')
    print("Data extraction from endpoints script completed successfully.")
    print("Data saved as .csv in the 'Data' folder.")

# Main function
if __name__ == "__main__":
    main()