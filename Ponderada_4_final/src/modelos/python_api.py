# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("python_api")

# Create input/output pydantic models
input_model = create_model("python_api_input", **{'age': 0.4, 'gender': 1.0, 'impluse': 0.060494959354400635, 'pressurehight': 0.5745856165885925, 'pressurelow': 0.4655172526836395, 'glucose': 0.16403162479400635, 'kcm': 0.005369078367948532, 'troponin': 0.0004854840226471424})
output_model = create_model("python_api_output", prediction=0.0)


@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}
# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
