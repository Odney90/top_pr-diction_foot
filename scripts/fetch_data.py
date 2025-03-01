import requests
import pandas as pd
import os

# Définition des paramètres de l'API
API_URL = "https://api.soccersapi.com/v2.2/leagues/?user=lundiodney&token=623654d91c81ceed9379be5968f089d8&t=list"

# Chemin du fichier de stockage
DATA_DIR = "../data"
DATA_PATH = os.path.join(DATA_DIR, "matchs.csv")  # Chemin absolu

def fetch_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        if "data" not in data or not isinstance(data["data"], list):
            print("❌ Erreur: La réponse de l'API ne contient pas de données valides.")
            return

        matches = []
        for league in data['data']:
            match_info = {
                "league_id": league.get("id", "N/A"),
                "league_name": league.get("name", "N/A"),
                "country": league.get("country_name", "N/A"),
                "season": league.get("current_season_id", "N/A"),
            }
            matches.append(match_info)

        # Vérification après la boucle
        print("🔹 Contenu final de matches :", matches)
        print(f"🔹 Nombre total d'éléments dans matches : {len(matches)}")
        
        if not matches:
            print("❌ Aucune donnée récupérée !")
            return

        # Création du DataFrame
        df = pd.DataFrame(matches)
        print("🔹 Aperçu du DataFrame avant enregistrement :")
        print(df)
        print(f"Nombre de lignes dans df : {len(df)}")

        # Vérifier et créer le dossier data
        os.makedirs(DATA_DIR, exist_ok=True)
        
        # Forcer l'écriture et éviter les problèmes de cache
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            df.to_csv(f, index=False)
            f.flush()
            os.fsync(f.fileno())
        
        print(f"✅ Données enregistrées dans {DATA_PATH}")

        # Vérification immédiate après écriture
        if os.path.exists(DATA_PATH):
            print(f"✅ Le fichier {DATA_PATH} a bien été créé.")
            with open(DATA_PATH, "r") as f:
                content = f.read()
                print("🔹 Contenu de matchs.csv après écriture :")
                print(content)
        else:
            print(f"❌ Erreur : {DATA_PATH} n'a pas été créé !")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la récupération des données : {e}")

def handle_manual_entry():
    print("📝 Saisie manuelle des données...")
    matches = []
    while True:
        league_id = input("ID de la ligue : ")
        league_name = input("Nom de la ligue : ")
        country = input("Pays : ")
        season = input("Saison : ")

        matches.append({
            "league_id": league_id,
            "league_name": league_name,
            "country": country,
            "season": season,
        })
        
        cont = input("Ajouter une autre ligue ? (o/n) : ")
        if cont.lower() != 'o':
            break
    
    df = pd.DataFrame(matches)
    os.makedirs(DATA_DIR, exist_ok=True)
    df.to_csv(DATA_PATH, index=False, mode='a', header=not os.path.exists(DATA_PATH))
    print("✅ Données ajoutées manuellement et enregistrées !")

if __name__ == "__main__":
    fetch_data()
