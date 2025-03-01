import pandas as pd  

def process_data(file_path):  
    # Charger les données depuis le fichier CSV  
    data = pd.read_csv(file_path)  

    # Afficher les premières lignes des données pour vérification  
    print("Données brutes :")  
    print(data.head())  

    # Effectuer le prétraitement des données  
    # Suppression des colonnes inutiles (ajustez les noms selon vos données)  
    columns_to_drop = ['colonne_inutile1', 'colonne_inutile2']  # Remplacez par les colonnes réelles si nécessaire  
    data = data.drop(columns=columns_to_drop, errors='ignore')  

    # Normalisation ou encodage si nécessaire  
    # Exemple de normalisation pour une colonne spécifique  
    # data['colonne'] = (data['colonne'] - data['colonne'].mean()) / data['colonne'].std()  

    # Afficher les données traitées pour vérification  
    print("Données traitées :")  
    print(data.head())  

    return data  

# Exemple d'utilisation  
if __name__ == "__main__":  
    # Chemin vers votre fichier CSV  
    processed_data = process_data('data/matchs.csv')  
