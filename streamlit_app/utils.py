"""
Utility layer: wires streamlit_app/ up to the existing, unmodified
model.model.predict_output function, and does the light field-name
mapping needed for the UI ("Gender" -> "Sex").

No ML logic, preprocessing, or model artifacts are touched here.
"""

import sys
from pathlib import Path

# Make the project root importable so `from model.model import predict_output` works
# regardless of the working directory `streamlit run` is launched from.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from model.model import predict_output  # noqa: E402  (import after sys.path fix)


# Human-readable UI options -> exact values the trained model expects
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

ST_SLOPE_OPTIONS = {"Upsloping": "Up", "Flat": "Flat", "Downsloping": "Down"}

FASTING_BS_OPTIONS = {"No (<= 120 mg/dL)": 0, "Yes (> 120 mg/dL)": 1}


def build_model_input(form_values: dict) -> dict:
    """
    Convert friendly UI values (e.g. Gender='Male') into the exact
    field names/values model.model.predict_output expects (Sex='M').
    This is purely a UI-label translation layer -- it does not alter
    any ML preprocessing.
    """
    return {
        "Age": form_values["age"],
        "Sex": GENDER_OPTIONS[form_values["gender"]],
        "ChestPainType": CHEST_PAIN_OPTIONS[form_values["chest_pain_type"]],
        "RestingBP": form_values["resting_bp"],
        "Cholesterol": form_values["cholesterol"],
        "FastingBS": FASTING_BS_OPTIONS[form_values["fasting_bs"]],
        "RestingECG": RESTING_ECG_OPTIONS[form_values["resting_ecg"]],
        "MaxHR": form_values["max_hr"],
        "ExerciseAngina": EXERCISE_ANGINA_OPTIONS[form_values["exercise_angina"]],
        "Oldpeak": form_values["oldpeak"],
        "ST_Slope": ST_SLOPE_OPTIONS[form_values["st_slope"]],
    }


def run_prediction(form_values: dict) -> dict:
    """Translate UI values and call the existing, unmodified model pipeline."""
    model_input = build_model_input(form_values)
    return predict_output(model_input)
