import requests  
import pandas as pd  

def fetch_data(api_url):  
    response = requests.get(api_url)  
    if response.status_code == 200:  
        data = response.json()  
        # Supposons que les données soient sous forme de liste de dictionnaires  
        leagues = data.get('response', [])  # Accéder à la clé 'response' pour obtenir les données  
        df = pd.DataFrame(leagues)  
        df.to_csv('data/matchs.csv', index=False)  
        print("Données récupérées et sauvegardées dans data/matchs.csv")  
    else:  
        print("Erreur lors de la récupération des données :", response.status_code)  

if __name__ == "__main__":  
    api_url = "https://api.soccersapi.com/v2.2/leagues/?user=lundiodney&token=623654d91c81ceed9379be5968f089d8&t=list"  
    fetch_data(api_url)  
