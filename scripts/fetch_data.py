import requests  
import pandas as pd  

def fetch_data():  
    url = "https://api.soccersapi.com/v2.2/leagues/?user=lundiodney&token=623654d91c81ceed9379be5968f089d8&t=list"  
    
    # Effectuer la requête GET  
    response = requests.get(url)  
    
    # Vérifier si la requête a réussi  
    if response.status_code == 200:  
        data = response.json()  # Convertir la réponse en JSON  
        print("Données de l'API :", data)  # Afficher les données de l'API  
        
        # Extraire les informations nécessaires  
        leagues = data.get('leagues', [])  
        print("Leagues extraites :", leagues)  # Afficher les ligues extraites  
        
        # Créer un DataFrame à partir des données  
        df = pd.DataFrame(leagues)  
        
        # Enregistrer le DataFrame dans un fichier CSV  
        df.to_csv('data/leagues.csv', index=False)  # Assurez-vous que ce chemin est correct  
        print("Données récupérées et enregistrées dans leagues.csv")  
        
        # Si vous avez besoin de récupérer des matchs, ajoutez cette logique ici  
        # df_matchs = ...  # Remplacez ceci par la logique pour récupérer les matchs  
        # df_matchs.to_csv('data/matchs.csv', index=False)  # Assurez-vous que ce chemin est correct  
    else:  
        print(f"Erreur lors de la récupération des données : {response.status_code}")  

# Appeler la fonction pour récupérer les données  
fetch_data()  
