Heart Disease Prediction Using SVM
This project leverages machine learning to predict the likelihood of heart disease based on various health parameters such as age, cholesterol, blood pressure, and exercise-induced angina. The model is trained using the Cleveland Heart Disease dataset and deployed via a Streamlit web application for interactive predictions.

Features
Predicts the likelihood of heart disease based on user inputs.
Utilizes machine learning (SVM) to train the model on the Cleveland Heart Disease dataset.
Deployed using Streamlit to create an interactive web interface for predictions.
Dataset
The model is trained on the Cleveland Heart Disease dataset, which includes the following features:

Age
Sex
Chest Pain Type
Resting Blood Pressure
Serum Cholesterol
Fasting Blood Sugar > 120 mg/dl
Resting Electrocardiographic Results
Maximum Heart Rate Achieved
Exercise Induced Angina
Oldpeak (Depression Induced by Exercise Relative to Rest)
Slope of the Peak Exercise ST Segment
Number of Major Vessels Colored by Fluoroscopy
Thalassemia
Installation
To run the project locally, follow these steps:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/heart-disease-prediction.git
Navigate to the project directory:

bash
Copy
Edit
cd heart-disease-prediction
Set up a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Train the model (if you haven't already):

Run the following Python script to train the model and save it:
bash
Copy
Edit
python train_model.py
Run the Streamlit app:

Launch the Streamlit app to start the web interface:
bash
Copy
Edit
streamlit run app.py
Make Predictions:

Input the required health parameters in the web interface, and the model will provide a prediction on whether the person is likely to have heart disease or not.
Example Input
Here’s a sample input you can try:

Age: 55
Sex: Male
Chest Pain Type: Atypical angina
Resting Blood Pressure: 140
Cholesterol: 240
Fasting Blood Sugar > 120 mg/dl: False
Resting Electrocardiographic results: ST-T wave abnormality
Max Heart Rate Achieved: 145
Exercise Induced Angina: Yes
Oldpeak: 1.5
Slope of Peak Exercise ST Segment: Flat
Number of Major Vessels Colored by Fluoroscopy: 2
Thalassemia: Fixed defect
Dependencies
Python 3.x
Streamlit
Scikit-learn
Pandas
Numpy
Imbalanced-learn (for SMOTE)
Joblib
To install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome!