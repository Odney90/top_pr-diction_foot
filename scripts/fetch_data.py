import requests  
import pandas as pd  

def fetch_data():  
    url = "https://api.soccersapi.com/v2.2/leagues/?user=lundiodney&token=623654d91c81ceed9379be5968f089d8&t=list"  
    response = requests.get(url)  
    
    if response.status_code == 200:  
        data = response.json()  
        leagues = data['data']  
        return leagues  
    else:  
        print("Erreur lors de la récupération des données :", response.status_code)  
        return None  

if __name__ == "__main__":  
    leagues_data = fetch_data()  
    if leagues_data:  
        # Convertir les données en DataFrame et les sauvegarder dans un fichier CSV  
        leagues_df = pd.DataFrame(leagues_data)  
        leagues_df.to_csv('data/leagues.csv', index=False)  
        print("Données des ligues sauvegardées dans data/leagues.csv")  
