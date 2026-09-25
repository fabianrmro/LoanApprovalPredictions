import os

import mlflow
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


MLFLOW_TRACKING_URI = os.getenv(
    "MLFLOW_TRACKING_URI",
    "http://host.docker.internal:5001",
)

MODEL_URI = os.getenv(
    "MODEL_URI",
    "models:/m-5f6d82857fa142349e24023bfc55b5e2",
)

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

model = mlflow.pyfunc.load_model(MODEL_URI)

app = FastAPI(
    title="Loan Approval Prediction API",
    description="API for the Loan Approval Prediction model deployed with Docker and MLflow.",
    version="1.0.0",
)


class LoanApplication(BaseModel):
    person_age: int
    person_income: float
    person_home_ownership: str
    person_emp_length: float
    loan_intent: str
    loan_grade: str
    loan_amnt: float
    loan_int_rate: float
    loan_percent_income: float
    cb_person_default_on_file: str
    cb_person_cred_hist_length: float


@app.get("/")
def root():
    return {
        "message": "Loan Approval Prediction API is running",
        "model_uri": MODEL_URI,
    }


@app.post("/predict")
def predict(application: LoanApplication):
    input_data = pd.DataFrame([application.model_dump()])

    prediction = model.predict(input_data)

    return {
        "prediction": int(prediction[0])
    }

class LoanApplication(BaseModel):
    person_age: int
    person_income: float
    person_home_ownership: str
    person_emp_length: float
    loan_intent: str
    loan_grade: str
    loan_amnt: float
    loan_int_rate: float
    loan_percent_income: float
    cb_person_default_on_file: str
    cb_person_cred_hist_length: float


@app.get("/")
def root():
    return {
        "message": "Loan Approval Prediction API is running",
        "model_uri": MODEL_URI,
    }


@app.post("/predict")
def predict(application: LoanApplication):
    input_data = pd.DataFrame([application.model_dump()])

    prediction = model.predict(input_data)

    return {
        "prediction": int(prediction[0])
    }
