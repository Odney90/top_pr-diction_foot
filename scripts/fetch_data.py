import requests  
import pandas as pd  

def fetch_data():  
    # Construire l'URL pour récupérer les ligues  
    url = f"{api_url}/leagues"  # Endpoint pour récupérer les ligues  
    
    # Définir les en-têtes pour la requête  
    headers = {  
        'x-apisports-key': api_key  # Utiliser la clé API dans les en-têtes  
    }  
    
    # Effectuer la requête GET  
    response = requests.get(url, headers=headers)  
    
    # Vérifier si la requête a réussi  
    if response.status_code == 200:  
        data = response.json()  # Convertir la réponse en JSON  
        print("Données de l'API :", data)  # Afficher les données de l'API  
        
        # Extraire les informations nécessaires  
        leagues = data.get('response', [])  # Les données des ligues sont dans 'response'  
        print("Leagues extraites :", leagues)  # Afficher les ligues extraites  
        
        # Créer un DataFrame à partir des données  
        df = pd.DataFrame(leagues)  
        
        # Créer le répertoire 'data' s'il n'existe pas  
        os.makedirs('data', exist_ok=True)  
        
        # Enregistrer le DataFrame dans un fichier CSV  
        df.to_csv('data/leagues.csv', index=False)  # Assurez-vous que ce chemin est correct  
        print("Données récupérées et enregistrées dans leagues.csv")  
    else:  
        print(f"Erreur lors de la récupération des données : {response.status_code}")  

# Appeler la fonction pour récupérer les données  
fetch_data()  # N'oubliez pas les parenthèses pour appeler la fonction  
