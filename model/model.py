import pandas as pd
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "rf_heart.pkl"

rf_model = joblib.load(MODEL_PATH)


def predict_output(user_input: dict):

    input_df = pd.DataFrame([user_input])

    input_df = pd.get_dummies(input_df)

    expected_columns = [
        "Age",
        "RestingBP",
        "Cholesterol",
        "FastingBS",
        "MaxHR",
        "Oldpeak",
        "Sex_M",
        "ChestPainType_ATA",
        "ChestPainType_NAP",
        "ChestPainType_TA",
        "RestingECG_Normal",
        "RestingECG_ST",
        "ExerciseAngina_Y",
        "ST_Slope_Flat",
        "ST_Slope_Up"
    ]

    input_df = input_df.reindex(
        columns=expected_columns,
        fill_value=False
    )

    # Prediction: 0 or 1
    prediction = rf_model.predict(input_df)[0]

    # Probability of each class
    probabilities = rf_model.predict_proba(input_df)[0]

    # Probability of class 1 (Heart Disease)
    heart_disease_probability = probabilities[1]

    return {
        "prediction": int(prediction),
        "probability": float(heart_disease_probability)
    }