import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
model = joblib.load(r'D:\shadow_knight\Heart disease prediction\training_model\heart_disease_model.pkl')


# Streamlit page title
st.title('Heart Disease Prediction')

# Create user inputs
age = st.number_input('Age', min_value=0, max_value=120, value=25)
sex = st.selectbox('Sex', ['Male', 'Female'])
cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])  # 0: typical, 1: atypical, 2: non-anginal, 3: asymptomatic
trestbps = st.number_input('Resting Blood Pressure', min_value=0, max_value=300, value=120)
chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0, max_value=600, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['True', 'False'])
restecg = st.selectbox('Resting Electrocardiographic results', [0, 1, 2])  # 0: normal, 1: having ST-T wave abnormality, 2: showing probable or definite left ventricular hypertrophy
thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=250, value=150)
exang = st.selectbox('Exercise Induced Angina', ['True', 'False'])
oldpeak = st.number_input('Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])  # 0: upsloping, 1: flat, 2: downsloping
ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', [0, 1, 2, 3])  # 0: none, 1-3: number of colored vessels
thal = st.selectbox('Thalassemia', [1, 2, 3])  # 1: normal, 2: fixed defect, 3: reversable defect

# Map inputs to numerical values
sex = 1 if sex == 'Male' else 0
fbs = 1 if fbs == 'True' else 0
exang = 1 if exang == 'True' else 0

# Prepare the input features
input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

# Make prediction
if st.button('Predict'):
    prediction = model.predict(input_data)
    result = 'Heart Disease Detected' if prediction[0] == 1 else 'No Heart Disease'
    st.write(result)

# Display some additional info
st.write("### Example Inputs:")
st.write("Age: 45, Sex: Male, Chest Pain Type: 1, Resting Blood Pressure: 130, Cholesterol: 250, Fasting Blood Sugar: False, etc.")
