import pandas as pd  
from sklearn.preprocessing import StandardScaler  

def preprocess_data():  
    # Charger les données depuis le fichier CSV  
    file_path = 'data/matchs.csv'  
    matches_df = pd.read_csv(file_path)  

    # 1. Vérification de la présence de toutes les variables  
    required_columns = [  
        'home_team_id', 'away_team_id', 'home_team_wins', 'away_team_wins',  
        'home_team_rank', 'home_team_goals_scored', 'home_team_goals_conceded',  
        'away_team_rank', 'away_team_goals_scored', 'away_team_goals_conceded'  
        # Ajoutez ici toutes les autres colonnes nécessaires  
    ]  

    missing_columns = [col for col in required_columns if col not in matches_df.columns]  
    if missing_columns:  
        print(f"Colonnes manquantes : {missing_columns}")  
        return  # Arrêter le traitement si des colonnes sont manquantes  

    print("Toutes les colonnes requises sont présentes.")  

    # 2. Remplissage des valeurs manquantes  
    # Remplir les valeurs manquantes avec la moyenne pour les colonnes numériques  
    matches_df.fillna(matches_df.mean(), inplace=True)  

    # Vous pouvez également choisir d'autres méthodes pour remplir les valeurs manquantes  
    # Par exemple, pour les colonnes catégorielles, vous pouvez utiliser la valeur la plus fréquente  
    # matches_df['some_categorical_column'].fillna(matches_df['some_categorical_column'].mode()[0], inplace=True)  

    print("Valeurs manquantes remplies.")  

    # 3. Normalisation des données  
    # Normaliser les colonnes numériques  
    scaler = StandardScaler()  
    numeric_columns = [  
        'home_team_rank', 'home_team_goals_scored', 'home_team_goals_conceded',  
        'away_team_rank', 'away_team_goals_scored', 'away_team_goals_conceded'  
        # Ajoutez ici toutes les autres colonnes numériques à normaliser  
    ]  

    matches_df[numeric_columns] = scaler.fit_transform(matches_df[numeric_columns])  

    print("Données normalisées.")  

    # Sauvegarder le DataFrame prétraité dans un nouveau fichier CSV  
    preprocessed_file_path = 'data/preprocessed_matches.csv'  
    matches_df.to_csv(preprocessed_file_path, index=False)  
    print(f"Données prétraitées sauvegardées dans {preprocessed_file_path}")  

# Appeler la fonction pour prétraiter les données  
if __name__ == "__main__":  
    preprocess_data()  
