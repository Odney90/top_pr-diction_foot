import streamlit as st
import pandas as pd
import joblib
import os

# Charger la liste des équipes (depuis un fichier ou une liste statique)
EQUIPES = ["PSG", "Marseille", "Lyon", "Monaco", "Lille", "Rennes", "Nice", "Bordeaux"]  # Exemple

# Charger les modèles
MODEL_PATH = "../models"
CLASSIFIER_MODEL = os.path.join(MODEL_PATH, "RandomForest_classifier.pkl")
REGRESSOR_TEAM1_MODEL = os.path.join(MODEL_PATH, "RandomForest_regressor_team1.pkl")
REGRESSOR_TEAM2_MODEL = os.path.join(MODEL_PATH, "RandomForest_regressor_team2.pkl")

# Vérifier que les modèles existent
if os.path.exists(CLASSIFIER_MODEL):
    classifier = joblib.load(CLASSIFIER_MODEL)
if os.path.exists(REGRESSOR_TEAM1_MODEL):
    regressor_team1 = joblib.load(REGRESSOR_TEAM1_MODEL)
if os.path.exists(REGRESSOR_TEAM2_MODEL):
    regressor_team2 = joblib.load(REGRESSOR_TEAM2_MODEL)

# Interface utilisateur
st.title("🔮 Prédiction de Match de Football")

# Sélection des équipes
col1, col2 = st.columns(2)
with col1:
    equipe1 = st.selectbox("Sélectionnez l'équipe 1", EQUIPES, key="equipe1")
with col2:
    equipe2 = st.selectbox("Sélectionnez l'équipe 2", [e for e in EQUIPES if e != equipe1], key="equipe2")

# Entrée manuelle des statistiques en cas de panne de l'API
st.subheader("📊 Entrez les statistiques manuellement (optionnel)")
classement_1 = st.number_input("Classement de l'équipe 1", min_value=1, max_value=20, step=1)
classement_2 = st.number_input("Classement de l'équipe 2", min_value=1, max_value=20, step=1)
points_1 = st.number_input("Points équipe 1", min_value=0, max_value=100, step=1)
points_2 = st.number_input("Points équipe 2", min_value=0, max_value=100, step=1)

# Bouton de prédiction
if st.button("Lancer la prédiction"):
    # Création d'un dataframe pour l'entrée du modèle
    X_input = pd.DataFrame({
        "classement_1": [classement_1],
        "classement_2": [classement_2],
        "points_1": [points_1],
        "points_2": [points_2],
    })
    
    # Prédiction du résultat
    prediction_resultat = classifier.predict(X_input)[0]
    prediction_buts_1 = regressor_team1.predict(X_input)[0]
    prediction_buts_2 = regressor_team2.predict(X_input)[0]
    
    # Affichage des résultats
    st.subheader("📢 Résultat de la prédiction")
    st.write(f"🏆 **Résultat du match** : {'Victoire Équipe 1' if prediction_resultat == 1 else 'Victoire Équipe 2' if prediction_resultat == -1 else 'Match Nul'}")
    st.write(f"⚽ **Score prédit** : {round(prediction_buts_1)} - {round(prediction_buts_2)}")
