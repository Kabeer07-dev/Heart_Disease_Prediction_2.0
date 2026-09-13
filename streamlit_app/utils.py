import os
import requests

GENDER_OPTIONS = {"Male": "M", "Female": "F"}

CHEST_PAIN_OPTIONS = {
    "Typical Angina (TA)": "TA",
    "Atypical Angina (ATA)": "ATA",
    "Non-Anginal Pain (NAP)": "NAP",
    "Asymptomatic (ASY)": "ASY",
}

RESTING_ECG_OPTIONS = {
    "Normal": "Normal",
    "ST-T Wave Abnormality (ST)": "ST",
    "Left Ventricular Hypertrophy (LVH)": "LVH",
}

EXERCISE_ANGINA_OPTIONS = {"Yes": "Y", "No": "N"}

ST_SLOPE_OPTIONS = {
    "Upsloping": "Up",
    "Flat": "Flat",
    "Downsloping": "Down",
}

FASTING_BS_OPTIONS = {
    "No (<= 120 mg/dL)": 0,
    "Yes (> 120 mg/dL)": 1,
}


def build_model_input(form_values: dict) -> dict:
    return {
        "age": form_values["age"],
        "gender": GENDER_OPTIONS[form_values["gender"]],
        "chest_pain_type": CHEST_PAIN_OPTIONS[form_values["chest_pain_type"]],
        "resting_bp": form_values["resting_bp"],
        "cholesterol": form_values["cholesterol"],
        "fasting_bs": FASTING_BS_OPTIONS[form_values["fasting_bs"]],
        "resting_ecg": RESTING_ECG_OPTIONS[form_values["resting_ecg"]],
        "max_hr": form_values["max_hr"],
        "exercise_angina": EXERCISE_ANGINA_OPTIONS[form_values["exercise_angina"]],
        "oldpeak": form_values["oldpeak"],
        "st_slope": ST_SLOPE_OPTIONS[form_values["st_slope"]],
    }


def run_prediction(form_values: dict) -> dict:
    model_input = build_model_input(form_values)

    api_url = os.getenv(
        "API_URL",
        "http://localhost:8000/predict"
    )

    response = requests.post(
        api_url,
        json=model_input,
        timeout=10,
    )

    response.raise_for_status()
    data = response.json()


    return {
        "prediction": data["prediction"],
        "probability": data["heart_disease_probability"] / 100,
    }