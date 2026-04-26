import streamlit as st

st.title("HR Attrition Prediction")

age = st.number_input("Age", min_value=18, max_value=60, value=30)
income = st.number_input("Monthly Income", min_value=1000, value=5000)
years = st.number_input("Years at Company", min_value=0, max_value=40, value=5)
overtime = st.selectbox("OverTime", ["No", "Yes"])
job_satisfaction = st.slider("Job Satisfaction (1-4)", 1, 4, 3)

if st.button("Predict"):

    score = 0

    if income < 4000:
        score += 1
    if overtime == "Yes":
        score += 1
    if years < 2:
        score += 1
    if job_satisfaction <= 2:
        score += 1
    if age < 25:
        score += 1

    if score >= 3:
        st.error("Employee Likely to Leave")
    else:
        st.success("Employee Likely to Stay")
