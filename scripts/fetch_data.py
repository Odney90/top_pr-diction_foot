import requests  
import pandas as pd  

def fetch_data():  
    url = "https://api.soccersapi.com/v2.2/leagues/?user=lundiodney&token=623654d91c81ceed9379be5968f089d8&t=list"  
    
    # Effectuer la requête GET  
    response = requests.get(url)  
    
    # Vérifier si la requête a réussi  
    if response.status_code == 200:  
        data = response.json()  # Convertir la réponse en JSON  
        
        # Extraire les informations nécessaires  
        leagues = data.get('leagues', [])  
        
        # Créer un DataFrame à partir des données  
        df = pd.DataFrame(leagues)  
        
        # Enregistrer le DataFrame dans un fichier CSV  
        df.to_csv('data/matchs.csv', index=False)  
        print("Données récupérées et enregistrées dans matchs.csv")  
    else:  
        print(f"Erreur lors de la récupération des données : {response.status_code}")  

# Appeler la fonction pour récupérer les données  
fetch_data()  
