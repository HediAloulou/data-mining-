import re
import pickle
import streamlit as st # type: ignore

model = pickle.load(open("best_model.pickle", "rb"))

st.title("Heart Disease Prediction")

# Input fields for the features
age = st.number_input("Age")
sex = st.selectbox("Sex", ["M", "F"])
chest_pain_type = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure")
cholesterol = st.number_input("Cholesterol")
fasting_bs = st.selectbox("Fasting Blood Sugar", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.number_input("Maximum Heart Rate")
exercise_angina = st.selectbox("Exercise-Induced Angina", ["N", "Y"])
oldpeak = st.number_input("Oldpeak")
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# Preprocess the input data
sex={"M":1,"F":0}[sex]
chest_pain_type = {"ATA": 1, "NAP": 2, "ASY": 0}[chest_pain_type]
resting_ecg = {"Normal": 1, "ST": 2, "LVH": 0}[resting_ecg]
exercise_angina = {"N": 0, "Y": 1}[exercise_angina]
st_slope = {"Up": 2, "Flat": 1, "Down": 0}[st_slope]

# Predict whether the person has heart disease or not
pred = model.predict([[age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope]])

# Display the prediction result
if st.button("Predict"):
    if pred == 0:
        st.success("No heart disease detected.")
    else:
        st.error("Heart disease detected.")