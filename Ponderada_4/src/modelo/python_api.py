import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, Float, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./database.db"
Base = declarative_base()

class Predictions(Base):
    __tablename__ = 'predictions'
    id = Column(Integer, Sequence('predict_id_seq'), primary_key=True)
    prediction = Column(Float, unique=True)

# Create the app
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
html_path = Path("static/index.html")
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Load trained Pipeline
model = load_model("python_api")

# Create input/output pydantic models
class InputModel(BaseModel):
    age: float
    gender: float
    impulse: float
    pressurehigh: float
    pressurelow: float
    glucose: float
    kcm: float
    troponin: float

class OutputModel(BaseModel):
    prediction: float

@app.get("/test")
def read_root():
    return {"message": "Welcome to the API!"}

@app.get("/", response_class=HTMLResponse)
def read_html():
    with open(html_path, "r") as file:
        html_content = file.read()
    return html_content

# Define predict function
@app.post("/predict", response_model=OutputModel)
def predict(data: InputModel):
    input_data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=input_data)
    prediction_value = predictions['Label'].iloc[0]  # Assuming 'Label' is the prediction column
    session = SessionLocal()
    predictions_entry = Predictions(prediction=prediction_value)
    session.add(predictions_entry)
    session.commit()
    session.close()

    return {"prediction": prediction_value}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
