import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier, XGBRegressor

# Chemin des données et des modèles
DATA_PATH = "../data/matchs.csv"
MODEL_DIR = "../models"
os.makedirs(MODEL_DIR, exist_ok=True)

def load_data():
    df = pd.read_csv(DATA_PATH)
    df = df.dropna()  # Supprimer les valeurs manquantes
    return df

def preprocess_data(df):
    X = df.drop(columns=["resultat_match", "buts_equipe1", "buts_equipe2"])
    y_classification = df["resultat_match"]  # 1 = Victoire équipe 1, 0 = Nul, -1 = Victoire équipe 2
    y_regression_team1 = df["buts_equipe1"]
    y_regression_team2 = df["buts_equipe2"]
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y_classification, y_regression_team1, y_regression_team2

def train_and_save_model(model, X, y, model_name):
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    print(f"📊 {model_name} - Précision moyenne : {np.mean(scores):.4f}")
    
    model.fit(X, y)
    model_path = os.path.join(MODEL_DIR, f"{model_name}.pkl")
    joblib.dump(model, model_path)
    print(f"✅ Modèle {model_name} enregistré dans {model_path}\n")

def train_models():
    df = load_data()
    X, y_classification, y_regression_team1, y_regression_team2 = preprocess_data(df)
    
    # Modèles de classification
    train_and_save_model(LogisticRegression(), X, y_classification, "LogisticRegression_classifier")
    train_and_save_model(RandomForestClassifier(n_estimators=100), X, y_classification, "RandomForest_classifier")
    train_and_save_model(SVC(kernel='linear', probability=True), X, y_classification, "SVM_classifier")
    train_and_save_model(XGBClassifier(use_label_encoder=False, eval_metric='logloss'), X, y_classification, "XGBoost_classifier")
    
    # Modèles de régression pour le nombre de buts
    train_and_save_model(RandomForestRegressor(n_estimators=100), X, y_regression_team1, "RandomForest_regressor_team1")
    train_and_save_model(RandomForestRegressor(n_estimators=100), X, y_regression_team2, "RandomForest_regressor_team2")
    train_and_save_model(XGBRegressor(), X, y_regression_team1, "XGBoost_regressor_team1")
    train_and_save_model(XGBRegressor(), X, y_regression_team2, "XGBoost_regressor_team2")

if __name__ == "__main__":
    train_models()
