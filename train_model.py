import pandas as pd  
from sklearn.model_selection import train_test_split, cross_val_score  
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor  
from xgboost import XGBClassifier, XGBRegressor  
from sklearn.svm import SVC  
from sklearn.linear_model import LogisticRegression  
import joblib  

def train_models(file_path):  
    # Charger les données  
    df = pd.read_csv(file_path)  

    # Définir les variables indépendantes et dépendantes  
    X = df.drop(['result', 'goals_team1', 'goals_team2'], axis=1)  # Variables indépendantes  
    y_result = df['result']  # Résultat du match (Victoire/Nul/Défaite)  
    y_goals_team1 = df['goals_team1']  # Nombre de buts pour l'équipe 1  
    y_goals_team2 = df['goals_team2']  # Nombre de buts pour l'équipe 2  

    # Séparer les données  
    X_train, X_test, y_train_result, y_test_result = train_test_split(X, y_result, test_size=0.2, random_state=42)  
    X_train_goals, X_test_goals, y_train_goals_team1, y_test_goals_team1 = train_test_split(X, y_goals_team1, test_size=0.2, random_state=42)  
    X_train_goals, X_test_goals, y_train_goals_team2, y_test_goals_team2 = train_test_split(X, y_goals_team2, test_size=0.2, random_state=42)  

    # Modèles de classification  
    classifiers = {  
        'XGBoost': XGBClassifier(),  
        'RandomForest': RandomForestClassifier(),  
        'SVM': SVC(),  
        'LogisticRegression': LogisticRegression()  
    }  

    for name, model in classifiers.items():  
        model.fit(X_train, y_train_result)  
        score = cross_val_score(model, X, y_result, cv=5)  
        print(f"{name} - Score de validation croisée : {score.mean()}")  
        joblib.dump(model, f'models/{name}_classifier.pkl')  

    # Modèles de régression pour le nombre de buts  
    regressors = {  
        'XGBoost': XGBRegressor(),  
        'RandomForest': RandomForestRegressor()  
    }  

    for name, model in regressors.items():  
        model.fit(X_train_goals, y_train_goals_team1)  # Entraînement pour l'équipe 1  
        joblib.dump(model, f'models/{name}_regressor_team1.pkl')  
        
        model.fit(X_train_goals, y_train_goals_team2)  # Entraînement pour l'équipe 2  
        joblib.dump(model, f'models/{name}_regressor_team2.pkl')  

if __name__ == "__main__":  
    train_models('data/matchs.csv')  
