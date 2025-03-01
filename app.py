import streamlit as st
import pandas as pd
import joblib
import os

# Charger la liste des équipes
EQUIPES = ["PSG", "Marseille", "Lyon", "Monaco", "Lille", "Rennes", "Nice", "Bordeaux"]

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
    equipe1 = st.selectbox("Sélectionnez l'équipe qui reçoit", EQUIPES, key="equipe1")
with col2:
    equipe2 = st.selectbox("Sélectionnez l'équipe en déplacement", [e for e in EQUIPES if e != equipe1], key="equipe2")

# Entrée des statistiques
st.subheader("📊 Entrez les statistiques manuellement (optionnel)")

# Variables générales
st.markdown("### 📌 Variables Générales")
classement_1 = st.number_input("Classement équipe qui reçoit", min_value=1, max_value=20, step=1)
classement_2 = st.number_input("Classement équipe en déplacement", min_value=1, max_value=20, step=1)
points_1 = st.number_input("Points équipe qui reçoit", min_value=0, max_value=100, step=1)
points_2 = st.number_input("Points équipe en déplacement", min_value=0, max_value=100, step=1)
h2h = st.number_input("Historique des confrontations (H2H, % de victoires à domicile)", min_value=0, max_value=100, step=1)

# Performance à domicile
st.markdown("### 🏠 Performance à domicile (Équipe qui reçoit)")
buts_domicile_1 = st.number_input("Buts marqués à domicile", min_value=0.0, max_value=10.0, step=0.1)
buts_encaisse_domicile_1 = st.number_input("Buts encaissés à domicile", min_value=0.0, max_value=10.0, step=0.1)
tirs_domicile_1 = st.number_input("Tirs tentés à domicile", min_value=0, max_value=30, step=1)
tirs_cadres_domicile_1 = st.number_input("Tirs cadrés à domicile", min_value=0, max_value=20, step=1)
possession_domicile_1 = st.slider("Possession moyenne à domicile (%)", 0, 100, 50)
fautes_domicile_1 = st.number_input("Fautes commises à domicile", min_value=0, max_value=30, step=1)
cartons_domicile_1 = st.number_input("Cartons jaunes reçus à domicile", min_value=0, max_value=10, step=1)
duels_gagnes_domicile_1 = st.number_input("Duels gagnés à domicile", min_value=0, max_value=50, step=1)
interceptions_domicile_1 = st.number_input("Interceptions à domicile", min_value=0, max_value=30, step=1)
tirs_subis_domicile_1 = st.number_input("Tirs subis à domicile", min_value=0, max_value=30, step=1)
cartons_rouges_domicile_1 = st.number_input("Cartons rouges à domicile", min_value=0, max_value=5, step=1)

# Performance à l'extérieur
st.markdown("### ✈️ Performance à l'extérieur (Équipe en déplacement)")
buts_exterieur_2 = st.number_input("Buts marqués à l'extérieur", min_value=0.0, max_value=10.0, step=0.1)
buts_encaisse_exterieur_2 = st.number_input("Buts encaissés à l'extérieur", min_value=0.0, max_value=10.0, step=0.1)
tirs_exterieur_2 = st.number_input("Tirs tentés à l'extérieur", min_value=0, max_value=30, step=1)
tirs_cadres_exterieur_2 = st.number_input("Tirs cadrés à l'extérieur", min_value=0, max_value=20, step=1)
possession_exterieur_2 = st.slider("Possession moyenne à l'extérieur (%)", 0, 100, 50)
fautes_exterieur_2 = st.number_input("Fautes commises à l'extérieur", min_value=0, max_value=30, step=1)
cartons_exterieur_2 = st.number_input("Cartons jaunes reçus à l'extérieur", min_value=0, max_value=10, step=1)
duels_gagnes_exterieur_2 = st.number_input("Duels gagnés à l'extérieur", min_value=0, max_value=50, step=1)
interceptions_exterieur_2 = st.number_input("Interceptions à l'extérieur", min_value=0, max_value=30, step=1)
tirs_subis_exterieur_2 = st.number_input("Tirs subis à l'extérieur", min_value=0, max_value=30, step=1)
cartons_rouges_exterieur_2 = st.number_input("Cartons rouges à l'extérieur", min_value=0, max_value=5, step=1)

# Bouton de prédiction
if st.button("Lancer la prédiction"):
    st.subheader("📢 Résultat de la prédiction")
    st.write("🏆 **Résultat du match** : (Prédiction à intégrer)")
