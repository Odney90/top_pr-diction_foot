import pandas as pd  
from sklearn.preprocessing import StandardScaler  

def preprocess_data(file_path):  
    # Charger les données  
    df = pd.read_csv(file_path)  

    # Vérifier la présence de toutes les variables  
    expected_columns = [  
        'league_id', 'league_name', 'country', 'season', 'team1', 'team2',   
        'points_team1', 'points_team2', 'wins_team1', 'wins_team2',   
        'draws_team1', 'draws_team2', 'losses_team1', 'losses_team2',   
        'goals_scored_team1', 'goals_scored_team2',   
        'goals_conceded_team1', 'goals_conceded_team2',   
        'average_possession_team1', 'average_possession_team2',   
        'average_shots_team1', 'average_shots_team2',   
        'average_shots_on_target_team1', 'average_shots_on_target_team2',   
        'yellow_cards_team1', 'yellow_cards_team2',   
        'fouls_team1', 'fouls_team2',   
        'injuries_team1', 'injuries_team2'  
    ]  
    
    for col in expected_columns:  
        if col not in df.columns:  
            print(f"Colonne manquante : {col}")  

    # Remplir les valeurs manquantes  
    df.fillna(method='ffill', inplace=True)  

    # Normaliser les données  
    numeric_columns = [  
        'points_team1', 'points_team2', 'wins_team1', 'wins_team2',   
        'draws_team1', 'draws_team2', 'losses_team1', 'losses_team2',   
        'goals_scored_team1', 'goals_scored_team2',   
        'goals_conceded_team1', 'goals_conceded_team2',   
        'average_possession_team1', 'average_possession_team2',   
        'average_shots_team1', 'average_shots_team2',   
        'average_shots_on_target_team1', 'average_shots_on_target_team2',   
        'yellow_cards_team1', 'yellow_cards_team2',   
        'fouls_team1', 'fouls_team2',   
        'injuries_team1', 'injuries_team2'  
    ]  
    
    scaler = StandardScaler()  
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])  

    # Sauvegarder les données prétraitées  
    df.to_csv(file_path, index=False)  
    print("Données prétraitées et sauvegardées.")  

if __name__ == "__main__":  
    preprocess_data('data/matchs.csv')  
