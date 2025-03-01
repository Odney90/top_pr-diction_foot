import requests
import pandas as pd
import os

# Définition des paramètres de l'API
API_TOKEN = "623654d91c81ceed9379be5968f089d8"
API_USER = "lundiodney"
API_BASE_URL = "https://api.soccersapi.com/v2.2"

# Chemins des fichiers de stockage
DATA_DIR = "../data"
LIGUES_PATH = os.path.join(DATA_DIR, "ligues.csv")
MATCHS_PATH = os.path.join(DATA_DIR, "matchs.csv")

def fetch_data(endpoint, params):
    url = f"{API_BASE_URL}/{endpoint}/"
    params.update({"user": API_USER, "token": API_TOKEN})
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la récupération des données depuis {endpoint} : {e}")
        return None

def fetch_ligues():
    data = fetch_data("leagues", {"t": "list"})
    if not data or "data" not in data:
        print("❌ Aucune donnée de ligues récupérée.")
        return

    ligues = []
    for league in data["data"]:
        ligues.append({
            "league_id": league.get("id", "N/A"),
            "league_name": league.get("name", "N/A"),
            "country": league.get("country_name", "N/A"),
            "season": league.get("current_season_id", "N/A"),
        })
    
    df = pd.DataFrame(ligues)
    os.makedirs(DATA_DIR, exist_ok=True)
    df.to_csv(LIGUES_PATH, index=False)
    print(f"✅ Données des ligues enregistrées dans {LIGUES_PATH}")

def fetch_matchs():
    data = fetch_data("matches", {"t": "schedule"})
    if not data or "data" not in data:
        print("❌ Aucune donnée de matchs récupérée.")
        return

    matchs = []
    for match in data["data"]:
        matchs.append({
            "match_id": match.get("id", "N/A"),
            "league_id": match.get("league_id", "N/A"),
            "home_team": match.get("home", {}).get("name", "N/A"),
            "away_team": match.get("away", {}).get("name", "N/A"),
            "date": match.get("date", "N/A"),
            "status": match.get("status", "N/A"),
        })
    
    df = pd.DataFrame(matchs)
    os.makedirs(DATA_DIR, exist_ok=True)
    df.to_csv(MATCHS_PATH, index=False)
    print(f"✅ Données des matchs enregistrées dans {MATCHS_PATH}")

if __name__ == "__main__":
    fetch_ligues()
    fetch_matchs()
