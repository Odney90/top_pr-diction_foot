import streamlit as st  
import pandas as pd  
import joblib  

# Charger les modèles  
model_classifier = joblib.load('models/XGBoost_classifier.pkl')  
model_regressor_team1 = joblib.load('models/XGBoost_regressor_team1.pkl')  
model_regressor_team2 = joblib.load('models/XGBoost_regressor_team2.pkl')  

# Titre de l'application  
st.title("Prédiction de Match de Football")  

# Formulaire pour entrer les données  
with st.form(key='match_form'):  
    team1 = st.text_input("Nom de l'équipe 1")  
    team2 = st.text_input("Nom de l'équipe 2")  
    # Ajoutez d'autres champs d'entrée selon vos besoins  
    submit_button = st.form_submit_button(label='Prédire')  

if submit_button:  
    # Préparer les données d'entrée pour le modèle  
    # Remplacez ceci par le traitement approprié de vos données  
    input_data = pd.DataFrame({  
        'team1': [team1],  
        'team2': [team2],  
        # Ajoutez d'autres colonnes nécessaires  
    })  

    # Faire des prédictions  
    result = model_classifier.predict(input_data)  
    goals_team1 = model_regressor_team1.predict(input_data)  
    goals_team2 = model_regressor_team2.predict(input_data)  

    # Afficher les résultats  
    st.write(f"Résultat prédit : {result[0]}")  
    st.write(f"Buts prédit pour {team1} : {goals_team1[0]}")  
    st.write(f"Buts prédit pour {team2} : {goals_team2[0]}")  
