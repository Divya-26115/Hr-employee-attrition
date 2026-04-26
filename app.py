import streamlit as st
import pickle
import numpy as np

# Load model only
model = pickle.load(open("attrition_model.pkl", "rb"))

st.title("HR Attrition Prediction")

age = st.number_input("Age", min_value=18, max_value=60, value=30)
income = st.number_input("Monthly Income", min_value=1000, value=5000)
years = st.number_input("Years at Company", min_value=0, max_value=40, value=5)
overtime = st.selectbox("OverTime", ["No", "Yes"])

ot = 1 if overtime == "Yes" else 0

if st.button("Predict"):
    data = np.array([[age, income, years, ot]])

    pred = model.predict(data)

    if pred[0] == 1:
        st.error("Employee Likely to Leave")
    else:
        st.success("Employee Likely to Stay")
