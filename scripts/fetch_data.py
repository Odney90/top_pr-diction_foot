import requests
import pandas as pd
from datetime import datetime

# Nouvelle clé API pour l'API-Football v2
API_KEY = "BA0C8BD117B1DA04666F51DF03AFF8E1"
headers = {
    "X-Api-Key": API_KEY
}

# Dictionnaire des championnats à récupérer (les IDs sont à vérifier dans la documentation officielle)
leagues = {
    "Premier League": 39,
    "La Liga": 140,
    "Serie A": 135,
    "Bundesliga": 78,
    "Ligue 1": 61,
    "Turkish Super Lig": 65,
    "Danish Superliga": 77,
    "Premier League 2nd Division": 50,  # Exemple, à adapter
    "La Liga 2": 141,
    "Serie B": 136,
    "Bundesliga 2": 79,
    "Ligue 2": 62,
    "Champions League": 2,
    "Europa League": 3,
    "Conference League": 4
}

season = 2023  # Saison cible

# Fonction auxiliaire pour calculer le nombre de jours depuis une date donnée
def calculate_days_since(last_match_date_str):
    try:
        last_match_date = datetime.strptime(last_match_date_str, "%Y-%m-%d")
        delta = datetime.now() - last_match_date
        return delta.days
    except Exception:
        return None

all_matches = []  # Liste pour stocker les données de chaque match

# Parcours de chaque ligue pour récupérer les données
for league_name, league_id in leagues.items():
    url = f"https://v2.api-football.com/leagueTable/{league_id}/{season}"
    print(f"Fetching data for {league_name} from URL: {url}")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        # Afficher la réponse complète pour déboguer
        print(f"Response for {league_name}:")
        print(data)
        
        # Tenter d'extraire les 'standings'
        standings = data.get("api", {}).get("standings", [])
        if not standings:
            print(f"Aucun 'standings' trouvé pour {league_name}.")
        else:
            # Association simplifiée des équipes par paires
            for i in range(0, len(standings) - 1, 2):
                team1 = standings[i]
                team2 = standings[i+1]
                
                match_record = {
                    "Competition": league_name,
                    # --- Équipe 1 ---
                    "Equipe_1": team1.get("name"),
                    "Classement_1": team1.get("rank"),
                    "Points_1": team1.get("points"),
                    "Victoires_1": team1.get("all", {}).get("win"),
                    "Défaites_1": team1.get("all", {}).get("lose"),
                    "Nuls_1": team1.get("all", {}).get("draw"),
                    "ButsMarques_1": team1.get("all", {}).get("goals", {}).get("for"),
                    "ButsEncaisses_1": team1.get("all", {}).get("goals", {}).get("against"),
                    "DiffButs_1": team1.get("all", {}).get("goalsDiff"),
                    "Domicile_1": 1,  # Supposons que l'équipe 1 joue à domicile
                    "JoursDepuisDernierMatch_1": calculate_days_since("2023-05-01"),
                    "ImportanceMatch_1": 0,
                    "H2H_1": None,
                    "ButsDomicile_1": team1.get("home", {}).get("goals", {}).get("for") if team1.get("home") else None,
                    "ButsExterieur_1": team1.get("away", {}).get("goals", {}).get("for") if team1.get("away") else None,
                    "Possession_1": None,
                    "Tirs_1": None,
                    "TirsCadrés_1": None,
                    "TirsSubis_1": None,
                    "xG_1": None,
                    "xGA_1": None,
                    "DuelsGagnes_1": None,
                    "Interceptions_1": None,
                    "CartonsJaunes_1": None,
                    "Fautes_1": None,
                    "Blessures_1": None,
                    "MeilleursButeurs_1": None,
                    
                    # --- Équipe 2 ---
                    "Equipe_2": team2.get("name"),
                    "Classement_2": team2.get("rank"),
                    "Points_2": team2.get("points"),
                    "Victoires_2": team2.get("all", {}).get("win"),
                    "Défaites_2": team2.get("all", {}).get("lose"),
                    "Nuls_2": team2.get("all", {}).get("draw"),
                    "ButsMarques_2": team2.get("all", {}).get("goals", {}).get("for"),
                    "ButsEncaisses_2": team2.get("all", {}).get("goals", {}).get("against"),
                    "DiffButs_2": team2.get("all", {}).get("goalsDiff"),
                    "Domicile_2": 0,  # Supposons que l'équipe 2 joue à l'extérieur
                    "JoursDepuisDernierMatch_2": calculate_days_since("2023-05-01"),
                    "ImportanceMatch_2": 0,
                    "H2H_2": None,
                    "ButsDomicile_2": team2.get("home", {}).get("goals", {}).get("for") if team2.get("home") else None,
                    "ButsExterieur_2": team2.get("away", {}).get("goals", {}).get("for") if team2.get("away") else None,
                    "Possession_2": None,
                    "Tirs_2": None,
                    "TirsCadrés_2": None,
                    "TirsSubis_2": None,
                    "xG_2": None,
                    "xGA_2": None,
                    "DuelsGagnes_2": None,
                    "Interceptions_2": None,
                    "CartonsJaunes_2": None,
                    "Fautes_2": None,
                    "Blessures_2": None,
                    "MeilleursButeurs_2": None
                }
                all_matches.append(match_record)
    else:
        print(f"Erreur pour {league_name} : {response.status_code}")

# Création d'un DataFrame et sauvegarde dans matchs.csv
df = pd.DataFrame(all_matches)
df.to_csv("matchs.csv", index=False)
print("Les données ont été sauvegardées dans matchs.csv")
print("Nombre de matchs récupérés :", len(df))
