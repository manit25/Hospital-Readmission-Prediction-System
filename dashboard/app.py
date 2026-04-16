import streamlit as st
import requests

st.title("🏥 Advanced Readmission Predictor")

data = {
    "age": st.slider("Age", 10, 100),
    "time": st.slider("Time in Hospital", 1, 14),
    "lab": st.slider("Lab Procedures", 1, 100),
    "meds": st.slider("Medications", 1, 50),
    "outpatient": st.slider("Outpatient Visits", 0, 10),
    "emergency": st.slider("Emergency Visits", 0, 10),
    "inpatient": st.slider("Inpatient Visits", 0, 10)
}

if st.button("Predict"):
    response = requests.post("http://localhost:8000/predict", json=data)
    result = response.json()

    if result["prediction"] == 1:
        st.error("⚠️ High Risk")
    else:
        st.success("✅ Low Risk")