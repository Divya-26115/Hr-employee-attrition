import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("attrition_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("HR Attrition Prediction")

age = st.number_input("Age")
income = st.number_input("Monthly Income")
years = st.number_input("Years at Company")
overtime = st.selectbox("OverTime", [0,1])

if st.button("Predict"):
    data = np.array([[age, income, years, overtime]])
    data = scaler.transform(data)
    pred = model.predict(data)

    if pred[0] == 1:
        st.error("Employee Likely to Leave")
    else:
        st.success("Employee Likely to Stay")