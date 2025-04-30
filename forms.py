from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, SelectField, 
                     FloatField, SubmitField)
from wtforms.validators import DataRequired, NumberRange

class PatientForm(FlaskForm):
    age = IntegerField('Age', validators=[
        DataRequired(), 
        NumberRange(min=18, max=120, message='Age must be between 18 and 120')
    ])
    gender = SelectField('Gender', choices=[
        ('0', 'Male'), 
        ('1', 'Female')
    ], validators=[DataRequired()])
    bmi = FloatField('BMI', validators=[
        DataRequired(), 
        NumberRange(min=10, max=50, message='BMI must be between 10 and 50')
    ])
    blood_pressure = IntegerField('Blood Pressure (mmHg)', validators=[
        DataRequired(), 
        NumberRange(min=60, max=250, message='Invalid blood pressure')
    ])
    cholesterol = IntegerField('Cholesterol (mg/dL)', validators=[
        DataRequired(), 
        NumberRange(min=100, max=400, message='Cholesterol must be 100-400')
    ])
    smoker = SelectField('Smoker', choices=[
        ('0', 'No'), 
        ('1', 'Yes')
    ], validators=[DataRequired()])
    diabetes = SelectField('Diabetes', choices=[
        ('0', 'No'), 
        ('1', 'Yes')
    ], validators=[DataRequired()])
    physical_activity = SelectField('Physical Activity Level', choices=[
        ('0', 'Sedentary'), 
        ('1', 'Light'), 
        ('2', 'Moderate'), 
        ('3', 'Active')
    ], validators=[DataRequired()])
    submit = SubmitField('Assess Risk')