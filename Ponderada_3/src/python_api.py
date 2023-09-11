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
input_model = create_model("python_api_input", **{'age': 0.33707866072654724, 'gender': 1.0, 'impluse': 0.05957837030291557, 'pressurehight': 0.4806629717350006, 'pressurelow': 0.4482758641242981, 'glucose': 0.31027668714523315, 'kcm': 0.0038341025356203318, 'troponin': 0.0046606468968093395})
output_model = create_model("python_api_output", prediction=0.0)


# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
