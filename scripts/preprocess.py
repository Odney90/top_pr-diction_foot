import pandas as pd  

def process_data(file_path):  
    # Charger les données depuis le fichier CSV  
    data = pd.read_csv(file_path)  

    # Afficher les premières lignes des données pour vérification  
    print("Données brutes :")  
    print(data.head())  

    # Effectuer le prétraitement des données  
    # Exemple : Suppression des colonnes inutiles  
    # Remplacez 'colonne_inutile1' et 'colonne_inutile2' par les noms réels des colonnes à supprimer  
    data = data.drop(columns=['colonne_inutile1', 'colonne_inutile2'], errors='ignore')  

    # Normalisation ou encodage si nécessaire  
    # Exemple de normalisation  
    # data['colonne'] = (data['colonne'] - data['colonne'].mean()) / data['colonne'].std()  

    # Afficher les données traitées pour vérification  
    print("Données traitées :")  
    print(data.head())  

    return data  

# Exemple d'utilisation  
if __name__ == "__main__":  
    # Remplacez 'data/matchs.csv' par le chemin vers votre fichier CSV  
    processed_data = process_data('data/matchs.csv')  
