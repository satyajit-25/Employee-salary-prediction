# api/index.py
from flask import Flask, request, jsonify
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load your pre-trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../random_forest_regressor_salary_predictor_v4.pkl')
# Adjust the path above if your .pkl is in a different location relative to api/index.py

try:
    with open(MODEL_PATH, 'rb') as model_file:
        model = pickle.load(model_file)
    print("Model loaded successfully!")
except FileNotFoundError:
    print(f"Error: Model file not found at {MODEL_PATH}")
    model = None # Handle case where model isn't loaded

@app.route('/')
def home():
    return "Welcome to the Salary Prediction API! Use /predict for predictions."

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded. Check server logs.'}), 500

    try:
        data = request.get_json(force=True)
        # Assuming your model expects a pandas DataFrame with specific columns
        # IMPORTANT: Replace these dummy values and logic with your actual model's input features
        # Example: data = {'YearsOfExperience': 5, 'EducationLevel': 'Bachelors', 'Role': 'Data Scientist'}
        # You'll need to transform 'data' into the exact format your model was trained on
        # This might involve one-hot encoding, scaling, etc.

        # Example: Create a DataFrame from the input data (adjust columns as per your model)
        input_df = pd.DataFrame([data])

        # --- IMPORTANT: ADD YOUR DATA PREPROCESSING HERE ---
        # For example, if 'EducationLevel' needs one-hot encoding:
        # from sklearn.preprocessing import OneHotEncoder
        # encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
        # encoded_features = encoder.fit_transform(input_df[['EducationLevel', 'Role']])
        # encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(['EducationLevel', 'Role']))
        # final_input = pd.concat([input_df.drop(columns=['EducationLevel', 'Role']), encoded_df], axis=1)
        # Make sure all required numerical features are present and scaled if necessary.
        # --- END OF IMPORTANT SECTION ---

        prediction = model.predict(input_df)[0] # Assuming single prediction
        return jsonify({'predicted_salary': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)