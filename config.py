import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    MODEL_PATH = 'models/risk_predictor.pkl'
    DATA_PATH = 'data/synthetic_patient_data.csv'
    RISK_FACTORS_PATH = 'data/risk_factors.json'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size