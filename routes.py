from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import PatientForm
from models.train_model import RiskAssessmentModel
import joblib
import json
import os

# Load model and risk factors
model = RiskAssessmentModel()
model.load_model(app.config['MODEL_PATH'])
model.load_risk_factors(app.config['RISK_FACTORS_PATH'])

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PatientForm()
    
    if form.validate_on_submit():
        # Prepare patient data
        patient_data = {
            'age': form.age.data,
            'gender': int(form.gender.data),
            'bmi': form.bmi.data,
            'blood_pressure': form.blood_pressure.data,
            'cholesterol': form.cholesterol.data,
            'smoker': int(form.smoker.data),
            'diabetes': int(form.diabetes.data),
            'physical_activity': int(form.physical_activity.data)
        }
        
        # Get prediction
        prediction, probabilities = model.predict_risk(list(patient_data.values()))
        
        # Generate explanation
        explanation = model.generate_explanation(patient_data, prediction)
        
        # Format results
        risk_levels = ['Low', 'Moderate', 'High']
        probability_percent = [round(p*100, 1) for p in probabilities]
        risk_probabilities = dict(zip(risk_levels, probability_percent))
        
        return render_template('results.html', 
                             prediction=prediction,
                             probabilities=risk_probabilities,
                             explanation=explanation,
                             patient_data=patient_data)
    
    return render_template('index.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')