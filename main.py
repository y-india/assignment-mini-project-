from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Load model
model = joblib.load("LogisticRegression.pkl")

# FastAPI app
app = FastAPI(title="Loan Approval Prediction API")

# Request Body Model
class LoanInput(BaseModel):
    Age: int
    Income: float
    Credit_Score: float
    Loan_Amount: float

@app.get("/")
def home():
    return {"message": "Loan Prediction API is running..."}

@app.post("/predict")
def predict(data: LoanInput):
    # Convert to numpy array
    X = np.array([[data.Age,
                   data.Income,
                   data.Credit_Score,
                   data.Loan_Amount]])

    # Prediction
    prediction = model.predict(X)[0]          # "Yes" or "No"

    return {
        "prediction": prediction
    }

