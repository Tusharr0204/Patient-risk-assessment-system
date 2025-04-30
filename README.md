# Patient-risk-assessment-system

# AI-Based Patient Risk Assessment System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0.1-green)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.0.2-orange)
![Transformers](https://img.shields.io/badge/transformers-4.11.3-yellow)

A machine learning system that predicts patient health risks using clinical data with explainable AI insights.

## Features

- **Risk Prediction**: Classifies patients into Low/Moderate/High risk categories
- **Explainable AI**: Generates natural language explanations for predictions
- **Web Interface**: Flask-based dashboard for easy interaction
- **Modular Design**: Easily extendable for new risk factor

  ### Prerequisites
- Python 3.8+
- pip 20.0+

### Steps
1.Clone the repository:
   bash
   git clone https://github.com/yourusername/patient-risk-assessment.git
   cd patient-risk-assessment
   
2.Create and activate virtual environment:
   bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate  # Windows   

3.Install dependencies:
    bash
    pip install -r requirements.txt

4.Train the model (optional):
    bash
    python models/train_model.py

Usage
Start the Flask server:

bash
python -m flask run
Enter patient data and view AI-generated risk assessment.

Project Structure
patient-risk-assessment/
├── app/                  # Flask application
├── data/                 # Sample datasets
├── models/               # ML model training code
├── config.py             # Configuration
├── requirements.txt      # Dependencies
└── README.md

Dataset
Sample synthetic dataset includes:
Demographic data (age, gender)
Clinical metrics (BMI, blood pressure)
Lifestyle factors (smoking status, activity level)

Technologies Used
Machine Learning: scikit-learn, Transformers
Web Framework: Flask
Explainability: Hugging Face Transformers (GPT-2 for explanations)
Visualization: Bootstrap, Progress bars
 
