import os  
import requests  
import pandas as pd  
from dotenv import load_dotenv  

# Charger les variables d'environnement à partir du fichier .env  
load_dotenv()  

# Récupérer la clé API  
api_key = os.getenv('API_KEY')
print("📌 Test de récupération de la clé API")
print(f"🔑 Clé API récupérée depuis .env : {api_key}")
print(f"🔑 Clé API dans les headers : {headers}")



# Vérifier si la clé API a été chargée correctement  
if api_key is None:  
    raise ValueError("La clé API n'a pas été trouvée. Assurez-vous que le fichier .env est correctement configuré.")  

# URL de l'API pour récupérer les données  
matches_api_url = "https://v3.football.api-sports.io/fixtures"  
leagues_api_url = "https://v3.football.api-sports.io/leagues"  

# Définir les en-têtes pour la requête  
headers = {  
    'x-apisports-key': api_key  
}  

def fetch_matches():  
    response = requests.get(matches_api_url, headers=headers)  
    print(f"Statut de la réponse pour les matchs : {response.status_code}")  # Afficher le code de statut  
    if response.status_code == 200:  
        data = response.json()  
        print("Données des matchs :", data)  # Afficher les données des matchs  
        if 'errors' in data and data['errors']:  
            print(f"Erreur dans la réponse de l'API : {data['errors']}")  
            return  
        matchs_data = []  

        # Parcourir les matchs récupérés  
        for match in data['response']:  
            match_info = {  
                'Classement_1': match['league']['rank'],  
                'Classement_2': match['league']['rank'],  
                'Points_1': match['teams']['home']['points'],  
                'Points_2': match['teams']['away']['points'],  
                'Victoires_1': match['teams']['home']['wins'],  
                'Victoires_2': match['teams']['away']['wins'],  
                'Défaites_1': match['teams']['home']['losses'],  
                'Défaites_2': match['teams']['away']['losses'],  
                'Nuls_1': match['teams']['home']['draws'],  
                'Nuls_2': match['teams']['away']['draws'],  
                'ButsMarques_1': match['goals']['home'],  
                'ButsMarques_2': match['goals']['away'],  
                'ButsEncaisses_1': match['goals']['away'],  
                'ButsEncaisses_2': match['goals']['home'],  
                'DiffButs_1': match['goals']['home'] - match['goals']['away'],  
                'DiffButs_2': match['goals']['away'] - match['goals']['home'],  
                'Domicile_1': 1,  
                'Domicile_2': 0,  
                'JoursDepuisDernierMatch_1': (pd.to_datetime(match['fixture']['date']) - pd.to_datetime(match['teams']['home']['lastMatchDate'])).days if 'lastMatchDate' in match['teams']['home'] else 0,  
                'JoursDepuisDernierMatch_2': (pd.to_datetime(match['fixture']['date']) - pd.to_datetime(match['teams']['away']['lastMatchDate'])).days if 'lastMatchDate' in match['teams']['away'] else 0,  
                'ImportanceMatch_1': 0,  
                'ImportanceMatch_2': 0,  
                'H2H_1': 0,  
                'H2H_2': 0,  
                'ButsDomicile_1': match['teams']['home']['goals']['home'],  
                'ButsDomicile_2': match['teams']['away']['goals']['home'],  
                'ButsExterieur_1': match['teams']['home']['goals']['away'],  
                'ButsExterieur_2': match['teams']['away']['goals']['away'],  
                'Possession_1': match['teams']['home']['possession'],  
                'Possession_2': match['teams']['away']['possession'],  
                'Tirs_1': match['teams']['home']['shots'],  
                'Tirs_2': match['teams']['away']['shots'],  
                'TirsCadrés_1': match['teams']['home']['shotsOn'],  
                'TirsCadrés_2': match['teams']['away']['shotsOn'],  
                'xG_1': match['teams']['home']['xG'],  
                'xG_2': match['teams']['away']['xG'],  
                'xGA_1': match['teams']['home']['xGA'],  
                'xGA_2': match['teams']['away']['xGA'],  
                'DuelsGagnes_1': match['teams']['home']['duelsWon'],  
                'DuelsGagnes_2': match['teams']['away']['duelsWon'],  
                'Interceptions_1': match['teams']['home']['interceptions'],  
                'Interceptions_2': match['teams']['away']['interceptions'],  
                'CartonsJaunes_1': match['teams']['home']['yellowCards'],  
                'CartonsJaunes_2': match['teams']['away']['yellowCards'],  
                'Fautes_1': match['teams']['home']['fouls'],  
                'Fautes_2': match['teams']['away']['fouls'],  
                'Blessures_1': match['teams']['home']['injuries'],  
                'Blessures_2': match['teams']['away']['injuries'],  
                'MeilleursButeurs_1': match['teams']['home']['topScorers'],  
                'MeilleursButeurs_2': match['teams']['away']['topScorers'],  
            }  
            matchs_data.append(match_info)  

        # Convertir en DataFrame et sauvegarder  
        matchs_df = pd.DataFrame(matchs_data)  
        matchs_df.to_csv('data/matchs.csv', index=False)  
        print("Données récupérées et sauvegardées dans matchs.csv")  
    else:  
        print(f"Erreur lors de la récupération des données des matchs : {response.status_code}")  

def fetch_leagues():  
    response = requests.get(leagues_api_url, headers=headers)  
    print(f"Statut de la réponse pour les ligues : {response.status_code}")  # Afficher le code de statut  
    if response.status_code == 200:  
        data = response.json()  
        print("Données des ligues :", data)  # Afficher les données des ligues  
        if 'errors' in data and data['errors']:  
            print(f"Erreur dans la réponse de l'API : {data['errors']}")  
            return  
        leagues_data = []  

        # Parcourir les ligues récupérées  
        for league in data['response']:  
            league_info = {  
                'id': league['league']['id'],  
                'name': league['league']['name'],  
                'country': league['country'],  
                'season': league['seasons'][0]['year'],  
                'logo': league['league']['logo']  
            }  
            leagues_data.append(league_info)  

        # Convertir en DataFrame et sauvegarder  
        leagues_df = pd.DataFrame(leagues_data)  
        leagues_df.to_csv('data/leagues.csv', index=False)  
        print("Données des ligues récupérées et sauvegardées dans leagues.csv")  
    else:  
        print(f"Erreur lors de la récupération des ligues : {response.status_code}")  

# Exécuter les fonctions  
fetch_matches()  # Récupérer les données des matchs  
fetch_leagues()  # Récupérer les données des ligues  
