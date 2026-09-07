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


@app.post('/predict')
def predict_heart_disease(user:PatientModel):
    input_data = {
    "Age": user.age,
    "Sex": user.gender,
    "ChestPainType": user.chest_pain_type,
    "RestingBP": user.resting_bp,
    "Cholesterol": user.cholesterol,
    "FastingBS": user.fasting_bs,
    "RestingECG": user.resting_ecg,
    "MaxHR": user.max_hr,
    "ExerciseAngina": user.exercise_angina,
    "Oldpeak": user.oldpeak,
    "ST_Slope": user.st_slope
    }
    try:
        prediction = predict_output(input_data)

        return JSONResponse(
            status_code=200,
            content={
                "prediction": prediction,
                "message": "Heart disease detected"
                if prediction == 1
                else "No heart disease detected"
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

