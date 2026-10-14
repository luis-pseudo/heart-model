from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi.middleware.cors import CORSMiddleware

# Cargar el modelo guardado
model = load(pathlib.Path('model/heart-disease-v1.joblib'))

# Definir la estructura de entrada de datos
class InputData(BaseModel):
    age: int = 63
    sex: int = 1
    cp: int = 3
    trestbps: int = 145
    chol: int = 233
    fbs: int = 1
    restecg: int = 0
    thalach: int = 150
    exang: int = 0
    oldpeak: float = 2.3
    slope: int = 0
    ca: int = 0
    thal: int = 1

# Definir la estructura de respuesta
class OutputData(BaseModel):
    score: float = 0.80318881046519

app = FastAPI(title='Heart Disease Prediction')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post('/score', response_model=OutputData)
def score(data: InputData):
    model_input = np.array([list(data.dict().values())])
    result = model.predict_proba(model_input)[:, -1]
    return {'score': float(result[0])}
