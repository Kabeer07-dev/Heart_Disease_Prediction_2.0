from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.model import load_model
from schema.user import PatientModel

app = FastAPI(title="Heart Disease Prediction",version=2.0)

rf_model = load_model()

@app.get('/')
def root():
    return JSONResponse({
        'message':'Heart Disease Prediction API'
    })


@app.get('/health')
def health():
    return JSONResponse({
        'Status' : 'OK',
        'version': '2.0'
    })




