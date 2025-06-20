# app.py
import streamlit as st
import numpy as np
import joblib

# Load the trained model (ensure the file is in the same directory or provide correct path)
model = joblib.load("model_gps (1).pkl")  # remove (1) or rename your file accordingly

# Set up the Streamlit page
st.set_page_config(page_title=" GPS Fraud Detection", layout="centered")
st.title(" GPS Fraud Detection System")
st.markdown("Enter GPS trip data to detect if the activity is **Fraudulent** or **Normal**.")

# Input form for user
with st.form("prediction_form"):
    blackout_duration = st.number_input("Blackout Duration (seconds)", min_value=0, step=1)
    distance = st.number_input("Distance Travelled (km)", min_value=0.0, step=0.1)
    speed_before = st.number_input("Speed Before Blackout (km/h)", min_value=0.0, step=0.1)
    speed_after = st.number_input("Speed After Blackout (km/h)", min_value=0.0, step=0.1)
    ignition_status = st.selectbox("Ignition Status", [0, 1], format_func=lambda x: "OFF" if x == 0 else "ON")

    submitted = st.form_submit_button(" Detect Fraud")

    if submitted:
        input_data = np.array([[blackout_duration, distance, speed_before, speed_after, ignition_status]])
        prediction = model.predict(input_data)[0]
        result = " Fraudulent Activity Detected!" if prediction == 1 else " Normal Trip"
        st.success(result)
