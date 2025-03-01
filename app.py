from flask import Flask, request, jsonify  
import pickle  
import pandas as pd  
import matplotlib.pyplot as plt  
import io  
import base64  
from process import process_data  # Importer la fonction de traitement  

app = Flask(__name__)  

# Charger les modèles  
def load_model(filename):  
    with open(filename, 'rb') as file:  
        model = pickle.load(file)  
    return model  

logistic_model = load_model('models/LogisticRegression_classifier.pkl')  
random_forest_classifier = load_model('models/RandomForest_classifier.pkl')  

@app.route('/predict', methods=['POST'])  
def predict():  
    try:  
        # Récupérer les données de la requête  
        data = request.json  
        # Convertir les données en DataFrame  
        df = pd.DataFrame(data)  

        # Traitement des données  
        processed_data = process_data('data/matchs.csv')  # Appeler la fonction de traitement  

        # Faire des prédictions avec le modèle choisi  
        predictions = logistic_model.predict(processed_data)  # Exemple avec le modèle de régression logistique  

        # Afficher les résultats sous forme de graphique  
        fig, ax = plt.subplots()  
        ax.bar(range(len(predictions)), predictions)  
        ax.set_title('Prédictions')  
        ax.set_xlabel('Index')  
        ax.set_ylabel('Valeur Prédite')  

        # Convertir le graphique en image  
        img = io.BytesIO()  
        plt.savefig(img, format='png')  
        img.seek(0)  
        img_base64 = base64.b64encode(img.getvalue()).decode('utf8')  

        return jsonify({  
            'predictions': predictions.tolist(),  
            'graph': img_base64  
        })  

    except Exception as e:  
        return jsonify({'error': str(e)}), 400  

if __name__ == '__main__':  
    app.run(debug=True)  
