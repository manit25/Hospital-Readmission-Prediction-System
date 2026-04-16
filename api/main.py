from fastapi import FastAPI
import pickle
import numpy as np
import os

app = FastAPI()

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
model_path = os.path.join(project_root, "model", "model.pkl")

model = pickle.load(open(model_path, "rb"))

@app.get("/")
def home():
    return {"message": "Hospital Readmission API Running"}

@app.post("/predict")
def predict(data: dict):
    values = np.array([list(data.values())])
    prediction = model.predict(values)

    return {
        "prediction": int(prediction[0]),
        "risk": "High" if prediction[0] == 1 else "Low"
    }