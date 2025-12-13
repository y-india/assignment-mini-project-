import streamlit as st
import requests

st.title("Loan Approval Prediction")

st.write("Enter the details below to check loan approval:")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)

income = st.number_input("Income (in 1000s)", min_value=0, max_value=1000, value=50)

credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=700)

loan_amount = st.number_input("Loan Amount (in 1000s)", min_value=1, max_value=1000, value=20)



if st.button("Predict Loan Approval"):
    # Prepare inputs
    inputs = {
        "Age": age,
        "Income": income,
        "Credit_Score": credit_score,
        "Loan_Amount": loan_amount
    }

    # Call FastAPI backend
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=inputs)
        data = response.json()

        if "prediction" in data:
            st.success(f"Prediction: {data['prediction']}")
        

    except Exception as e:
        st.error(f"Failed to connect to API: {e}")
