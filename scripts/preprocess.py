import pandas as pd  

def preprocess_data(file_path):  
    # Charger les données  
    df = pd.read_csv(file_path)  

    # Vérifier la présence de toutes les variables  
    print("Vérification des colonnes manquantes...")  
    missing_columns = df.columns[df.isnull().any()].tolist()  
    if missing_columns:  
        print("Colonnes manquantes :", missing_columns)  
        # Remplir les valeurs manquantes (exemple : avec la moyenne)  
        for column in missing_columns:  
            df[column].fillna(df[column].mean(), inplace=True)  

    # Normaliser les données (exemple : Min-Max Scaling)  
    df = (df - df.min()) / (df.max() - df.min())  

    # Sauvegarder les données prétraitées  
    df.to_csv('data/preprocessed_matchs.csv', index=False)  
    print("Données prétraitées sauvegardées dans data/preprocessed_matchs.csv")  

if __name__ == "__main__":  
    preprocess_data('data/matchs.csv')  
