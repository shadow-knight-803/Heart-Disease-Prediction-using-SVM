# Heart Disease Prediction using SVM

This project uses a **Support Vector Machine (SVM)** model to predict the likelihood of heart disease based on various health parameters. The model is trained using a dataset containing attributes like age, sex, blood pressure, cholesterol levels, and more.

## Features

- Predicts the presence or absence of heart disease.
- Uses **Support Vector Machine (SVM)** for classification.
- Built using **Python**, with libraries like **scikit-learn**, **pandas**, **streamlit**, and **joblib** for deployment.
- Allows users to input medical information and receive a prediction for heart disease.

## Dataset

The dataset used for this project contains various attributes related to heart disease prediction. These include:
- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Serum Cholesterol
- Fasting Blood Sugar
- Resting Electrocardiographic results
- Maximum Heart Rate Achieved
- Exercise-Induced Angina
- Oldpeak
- Slope of the Peak Exercise ST Segment
- Number of Major Vessels Colored by Fluoroscopy
- Thalassemia
- Target (Presence of Heart Disease)

### Data Source
The dataset can be found in the `heart.csv` file in this repository.

## Requirements

- Python 3.x
- pandas
- scikit-learn
- joblib
- imbalanced-learn (for SMOTE)
- streamlit

You can install the required libraries using:

```bash
pip install -r requirements.txt
