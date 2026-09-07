from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.model import predict_output,rf_model
from schema.user import PatientModel
import pandas as pd


app = FastAPI(title="Heart Disease Prediction")



@app.get('/')
def root():
    return JSONResponse({
        'message':'Heart Disease Prediction API'
    })


@app.get('/health')
def health():
    return JSONResponse({
        'Status' : 'OK',
        'version': '2.0',
        'model':rf_model is not None
    })


@app.get('/predict')
def predict_heart_disease(user:PatientModel):
    try:
        prediction = predict_output(user)
        return JSONResponse(status_code=200,content=[f'Disease risk: {prediction}'])
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))

