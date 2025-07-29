# ⚽ Fantasy Premier League Draft Data Extractor

This project extracts data from the [Fantasy Premier League Draft API](https://draft.premierleague.com/api), including:
- League standings
- Player statistics
- Gameweek data

It processes and saves the extracted data into structured `.csv` files stored in a local `Data/` folder.

For the 2024/2025 season endpoints and data format may have changed since

---

## 📁 Project Structure
FPL-24_25/

├── main.py # Main script to run the data extraction

├── league.py # Extracts league standings data

├── players.py # Extracts player stats from the API

├── utils.py # Common utilities: fetch API data, save CSV, etc.

├── Data/ # Folder where CSV files will be saved

└── README.md # This file


---

## 🚀 Features

- Fetches and saves:
  - League standings with manager info
  - Player stats and metadata
  - Gameweek-specific player performance
- Organizes results into CSV files in `Data/`
- Modular code: logic is split between `league.py`, `players.py`, and `utils.py`

---

## 🔧 Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/fpl-draft-data-extractor.git
cd fpl-draft-data-extractor
```

2. Install dependencies
This project uses standard libraries, but make sure you have the following installed:
```
pip install pandas requests
```
This will:

- Create a Data/ folder (if it doesn’t exist)

- Fetch and save league_standings.csv

- Fetch and save players_data.csv

## 📦 Output Files
Inside the Data/ folder:

- league_standings.csv: Manager IDs, names, waiver pick, and team name

- players_data.csv: Detailed stats for all available players

## 📚 API Endpoints Used
https://draft.premierleague.com/api/league/{league_id}/details

https://draft.premierleague.com/api/bootstrap-static

https://draft.premierleague.com/api/event/{gameweek}/live

https://draft.premierleague.com/api/game

## 🛠 Modules Overview
main.py
Orchestrates the full data extraction pipeline:

Creates the Data/ directory if needed

Fetches league standings and player data

league.py
Fetches the league standings and saves them to league_standings.csv.

players.py
Fetches static player data and saves it to players_data.csv.

utils.py
## Shared utilities:

- fetch_data(): Handles GET requests

- save_csv(): Saves lists of data to .csv files

- Additional helper functions (e.g. SQLite support)

📌 Notes
- Default league ID is 70113. You can change this in main.py and league.py.

- All output data is saved locally inside the Data/ folder.

- Gameweek data handling (from event/{gameweek}/live) is available via get_player_gw_data(gameweek) in utils.py.

