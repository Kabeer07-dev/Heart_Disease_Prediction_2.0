import pandas as pd
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "rf_heart.pkl"

rf_model = joblib.load(MODEL_PATH)


def predict_output(user_input: dict):

    input_df = pd.DataFrame([user_input])

    # Encode categorical variables
    input_df = pd.get_dummies(input_df)

    # Exact columns used during training
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

    # Make prediction dataframe identical to training dataframe
    input_df = input_df.reindex(
        columns=expected_columns,
        fill_value=False
    )

    prediction = rf_model.predict(input_df)[0]

    return int(prediction)