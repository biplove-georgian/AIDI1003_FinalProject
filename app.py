from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the trained RandomForest model
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from POST request
        data = request.get_json(force=True)

        # Convert list of dictionaries to list of lists for model prediction
        features_list = [list(observation.values()) for observation in data]

        # Make prediction using the loaded model
        predictions = model.predict(features_list)
        
        # Generate descriptive response
        results = []
        for i, pred in enumerate(predictions):
            result = {
                "transaction": i + 1,
                "prediction": "Fraud" if pred == 1 else "Not Fraud",
                "message": f"Transaction {i + 1} is predicted as {'Fraud' if pred == 1 else 'Not Fraud'}."
            }
            results.append(result)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)