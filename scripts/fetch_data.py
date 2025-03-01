import requests  
import pandas as pd  
import os  
from dotenv import load_dotenv  

# Charger les variables d'environnement  
load_dotenv()  
api_key = os.getenv('API_KEY')  

# URL de l'API pour récupérer les données  
matches_api_url = "https://v3.football.api-sports.io/fixtures"  
leagues_api_url = "https://v3.football.api-sports.io/leagues"  

# Définir les en-têtes pour la requête  
headers = {  
    'x-apisports-key': api_key  
}  

def fetch_matches():  # Renommé pour correspondre au contexte  
    response = requests.get(matches_api_url, headers=headers)  
    print(f"Statut de la réponse pour les matchs : {response.status_code}")  # Afficher le code de statut  
    if response.status_code == 200:  
        data = response.json()  
        matchs_data = []  

        # Parcourir les matchs récupérés  
        for match in data['response']:  
            match_info = {  
                # 1. Classement et Performance Actuelle  
                'Classement_1': match['league']['rank'],  # Classement actuel de l'équipe 1  
                'Classement_2': match['league']['rank'],  # Classement actuel de l'équipe 2  
                'Points_1': match['teams']['home']['points'],  # Points de l'équipe 1  
                'Points_2': match['teams']['away']['points'],  # Points de l'équipe 2  

                # 2. Historique des Résultats  
                'Victoires_1': match['teams']['home']['wins'],  # Victoires de l'équipe 1  
                'Victoires_2': match['teams']['away']['wins'],  # Victoires de l'équipe 2  
                'Défaites_1': match['teams']['home']['losses'],  # Défaites de l'équipe 1  
                'Défaites_2': match['teams']['away']['losses'],  # Défaites de l'équipe 2  
                'Nuls_1': match['teams']['home']['draws'],  # Nuls de l'équipe 1  
                'Nuls_2': match['teams']['away']['draws'],  # Nuls de l'équipe 2  

                # 3. Attaque & Défense  
                'ButsMarques_1': match['goals']['home'],  # Buts marqués par l'équipe 1  
                'ButsMarques_2': match['goals']['away'],  # Buts marqués par l'équipe 2  
                'ButsEncaisses_1': match['goals']['away'],  # Buts encaissés par l'équipe 1  
                'ButsEncaisses_2': match['goals']['home'],  # Buts encaissés par l'équipe 2  
                'DiffButs_1': match['goals']['home'] - match['goals']['away'],  # Différence de buts équipe 1  
                'DiffButs_2': match['goals']['away'] - match['goals']['home'],  # Différence de buts équipe 2  

                # 4. Contexte du Match  
                'Domicile_1': 1,  # Équipe 1 joue à domicile  
                'Domicile_2': 0,  # Équipe 2 joue à l'extérieur  
                'JoursDepuisDernierMatch_1': (pd.to_datetime(match['fixture']['date']) - pd.to_datetime(match['teams']['home']['lastMatchDate'])).days if 'lastMatchDate' in match['teams']['home'] else 0,  # Jours depuis le dernier match équipe 1  
                'JoursDepuisDernierMatch_2': (pd.to_datetime(match['fixture']['date']) - pd.to_datetime(match['teams']['away']['lastMatchDate'])).days if 'lastMatchDate' in match['teams']['away'] else 0,  # Jours depuis le dernier match équipe 2  
                'ImportanceMatch_1': 0,  # Importance du match pour l'équipe 1 (à définir)  
                'ImportanceMatch_2': 0,  # Importance du match pour l'équipe 2 (à définir)  

                # 5. Historique des Confrontations (H2H)  
                'H2H_1': 0,  # Résultat moyen des 5 derniers matchs de l'équipe 1 contre l'équipe 2 (à définir)  
                'H2H_2': 0,  # Résultat moyen des 5 derniers matchs de l'équipe 2 contre l'équipe 1 (à définir)  

                # 6. Données Offensives et Défensives  
                'ButsDomicile_1': match['teams']['home']['goals']['home'],  # Buts marqués à domicile par l'équipe 1  
                'ButsDomicile_2': match['teams']['away']['goals']['home'],  # Buts marqués à domicile par l'équipe 2  
                'ButsExterieur_1': match['teams']['home']['goals']['away'],  # Buts marqués à l'extérieur par l'équipe 1  
                'ButsExterieur_2': match['teams']['away']['goals']['away'],  # Buts marqués à l'extérieur par l'équipe 2  
                'Possession_1': match['teams']['home']['possession'],  # Possession de l'équipe 1  
                'Possession_2': match['teams']['away']['possession'],  # Possession de l'équipe 2  
                'Tirs_1': match['teams']['home']['shots'],  # Tirs de l'équipe 1  
                'Tirs_2': match['teams']['away']['shots'],  # Tirs de l'équipe 2  
                'TirsCadrés_1': match['teams']['home']['shotsOn'],  # Tirs cadrés de l'équipe 1  
                'TirsCadrés_2': match['teams']['away']['shotsOn'],  # Tirs cadrés de l'équipe 2  

                # 7. Expected Goals (xG) et Défense Avancée  
                'xG_1': match['teams']['home']['xG'],  # Expected Goals de l'équipe 1  
                'xG_2': match['teams']['away']['xG'],  # Expected Goals de l'équipe 2  
                'xGA_1': match['teams']['home']['xGA'],  # Expected Goals Against de l'équipe 1  
                'xGA_2': match['teams']['away']['xGA'],  # Expected Goals Against de l'équipe 2  

                # 8. Performance Physique et Défensive  
                'DuelsGagnes_1': match['teams']['home']['duelsWon'],  # Duels gagnés par l'équipe 1  
                'DuelsGagnes_2': match['teams']['away']['duelsWon'],  # Duels gagnés par l'équipe 2  
                'Interceptions_1': match['teams']['home']['interceptions'],  # Interceptions de l'équipe 1  
                'Interceptions_2': match['teams']['away']['interceptions'],  # Interceptions de l'équipe 2  

                # 9. Cartons et Fautes  
                'CartonsJaunes_1': match['teams']['home']['yellowCards'],  # Cartons jaunes de l'équipe 1  
                'CartonsJaunes_2': match['teams']['away']['yellowCards'],  # Cartons jaunes de l'équipe 2  
                'Fautes_1': match['teams']['home']['fouls'],  # Fautes de l'équipe 1  
                'Fautes_2': match['teams']['away']['fouls'],  # Fautes de l'équipe 2  

                # 10. État Physique et Absences  
                'Blessures_1': match['teams']['home']['injuries'],  # Blessures de l'équipe 1  
                'Blessures_2': match['teams']['away']['injuries'],  # Blessures de l'équipe 2  

                # 11. Performance des Meilleurs Joueurs  
                'MeilleursButeurs_1': match['teams']['home']['topScorers'],  # Meilleurs buteurs de l'équipe 1  
                'MeilleursButeurs_2': match['teams']['away']['topScorers'],  # Meilleurs buteurs de l'équipe 2  
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
        leagues_data = []  

        # Parcourir les ligues récupérées  
        for league in data['response']:  
            league_info = {  
                'id': league['league']['id'],  
                'name': league['league']['name'],  
                'country': league['country'],  
                'season': league['seasons'][0]['year'],  # Assurez-vous que cette clé existe  
                'logo': league['league']['logo']  
            }  
            leagues_data.append(league_info)  

        # Convertir en DataFrame et sauvegarder  
        leagues_df = pd.DataFrame(leagues_data)  
        leagues_df.to_csv('data/leagues.csv', index=False)  
        print("Données des ligues récupérées et sauvegardées dans leagues.csv")  
    else:  
        print(f"Erreur lors de la récupération des ligues : {response.status_code}")  

if __name__ == "__main__":  
    fetch_matches()  # Récupérer les données des matchs  
    fetch_leagues()   # Récupérer les données des ligues  
