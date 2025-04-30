import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import json
from transformers import pipeline

class RiskAssessmentModel:
    def __init__(self):
        self.model = None
        self.explainer = None
        self.risk_factors = None
        self.nlp = pipeline("text-generation", model="gpt2")
        
    def load_data(self, data_path):
        """Load and preprocess patient data"""
        data = pd.read_csv(data_path)
        
        # Convert categorical variables
        data['gender'] = data['gender'].map({'Male': 0, 'Female': 1})
        data['smoker'] = data['smoker'].map({'No': 0, 'Yes': 1})
        data['diabetes'] = data['diabetes'].map({'No': 0, 'Yes': 1})
        
        # Define features and target
        features = ['age', 'gender', 'bmi', 'blood_pressure', 'cholesterol', 
                   'smoker', 'diabetes', 'physical_activity']
        target = 'risk_level'
        
        X = data[features]
        y = data[target]
        
        return X, y, features
    
    def train(self, X, y):
        """Train the risk assessment model"""
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42)
        
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))
        
    def save_model(self, path):
        """Save trained model to file"""
        joblib.dump(self.model, path)
        
    def load_model(self, path):
        """Load trained model from file"""
        self.model = joblib.load(path)
        
    def load_risk_factors(self, path):
        """Load risk factor descriptions"""
        with open(path, 'r') as f:
            self.risk_factors = json.load(f)
    
    def predict_risk(self, patient_data):
        """Predict risk level for a patient"""
        if not self.model:
            raise ValueError("Model not loaded or trained")
            
        prediction = self.model.predict([patient_data])[0]
        proba = self.model.predict_proba([patient_data])[0]
        
        return prediction, proba
    
    def generate_explanation(self, patient_data, prediction):
        """Generate natural language explanation for the prediction"""
        if not self.risk_factors:
            raise ValueError("Risk factors not loaded")
            
        # Get feature importances
        importances = self.model.feature_importances_
        top_features = np.argsort(importances)[::-1][:3]
        
        # Prepare explanation
        prompt = f"The patient has been assessed with {prediction} risk level. "
        prompt += "The main contributing factors are: "
        
        factors = []
        for i in top_features:
            feature_name = list(patient_data.keys())[i]
            feature_value = patient_data[feature_name]
            factors.append(f"{feature_name} ({feature_value})")
        
        prompt += ", ".join(factors) + ". "
        prompt += "Here's a detailed explanation: "
        
        # Generate detailed explanation using GPT
        explanation = self.nlp(
            prompt,
            max_length=150,
            num_return_sequences=1,
            temperature=0.7,
            truncation=True
        )[0]['generated_text']
        
        return explanation

if __name__ == "__main__":
    # Train and save the model
    model = RiskAssessmentModel()
    X, y, _ = model.load_data('patient-risk-assessment\data\synthetic data.csv')
    model.train(X, y)
    model.save_model('models/risk_predictor.pkl')
    model.load_risk_factors('data/risk_factors.json')
    
    # Test prediction
    sample_patient = {
        'age': 45,
        'gender': 1,
        'bmi': 28,
        'blood_pressure': 140,
        'cholesterol': 220,
        'smoker': 0,
        'diabetes': 1,
        'physical_activity': 2
    }
    
    prediction, proba = model.predict_risk(list(sample_patient.values()))
    print(f"Prediction: {prediction}, Probabilities: {proba}")
    
    explanation = model.generate_explanation(sample_patient, prediction)
    print("\nExplanation:", explanation)