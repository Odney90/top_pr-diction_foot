import pandas as pd  
from sklearn.model_selection import train_test_split, cross_val_score  
from xgboost import XGBClassifier, XGBRegressor  
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor  
from sklearn.linear_model import LogisticRegression  
from sklearn.svm import SVC  
import pickle  

def train_models():  
    # Charger les données prétraitées  
    df = pd.read_csv('data/preprocessed_matchs.csv')  

    # Séparer les caractéristiques et la cible  
    X = df.drop(columns=['result'])  # Remplacez 'result' par le nom de votre colonne cible  
    y = df['result']  

    # Diviser les données en ensembles d'entraînement et de test  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  

    # Modèles à entraîner  
    models = {  
        'XGBoost': XGBClassifier(),  
        'RandomForest': RandomForestClassifier(),  
        'SVM': SVC(),  
        'LogisticRegression': LogisticRegression()  
    }  

    for name, model in models.items():  
        print(f"Entraînement du modèle {name}...")  
        model.fit(X_train, y_train)  
        score = cross_val_score(model, X_train, y_train, cv=5)  
        print(f"Score de validation croisée pour {name} : {score.mean()}")  

        # Sauvegarder le modèle  
        with open(f'models/{name}.pkl', 'wb') as file:  
            pickle.dump(model, file)  

if __name__ == "__main__":  
    train_models()  
