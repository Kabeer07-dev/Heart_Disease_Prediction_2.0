import pandas as pd
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "rf_heart.pkl"

rf_model = joblib.load(MODEL_PATH)


def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])
    prediction = rf_model.predict(input_df)[0]
    return prediction





