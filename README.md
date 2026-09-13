# ❤️ Heart Disease Prediction 2.0

A machine learning powered web service that predicts the likelihood of heart disease from a patient's clinical data. The project exposes a **FastAPI** REST API backed by a trained **Random Forest** model, along with a companion **Streamlit** UI for interactive use — both packaged in a single Docker image.

## Overview

Given a set of clinical measurements (age, chest pain type, cholesterol, resting blood pressure, etc.), the service returns:
- A binary prediction (heart disease detected / not detected)
- The predicted probability of heart disease (%)
- A human-readable message summarizing the result

## Features

- 🔌 **REST API** built with FastAPI, with request validation via Pydantic
- 🌳 **Random Forest** classifier for prediction
- 🖥️ **Streamlit UI** for a no-code, form-based experience
- 🩺 `/health` endpoint to verify the API and model status
- 🐳 **Dockerized** — runs the API and UI together with a single command

## Tech Stack

| Component        | Technology            |
|-------------------|------------------------|
| API framework      | FastAPI + Uvicorn      |
| Frontend           | Streamlit              |
| ML model           | scikit-learn (Random Forest) |
| Data validation    | Pydantic               |
| Data handling      | pandas, numpy          |
| Model persistence  | joblib                 |
| Containerization   | Docker                 |

## Project Structure

```
Heart_Disease_Prediction_2.0/
├── model/              # Trained model + prediction logic
│   └── model.py         # Loads the Random Forest model, exposes predict_output()
├── schema/              # Request/response data models
│   └── user.py           # Pydantic PatientModel schema
├── streamlit_app/       # Streamlit front-end
│   └── app.py
├── app.py               # FastAPI application (API entry point)
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container build definition
├── start.sh             # Launches both API and UI in the container
└── .dockerignore
```

## Getting Started

### Prerequisites
- Python 3.12+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/Kabeer07-dev/Heart_Disease_Prediction_2.0.git
cd Heart_Disease_Prediction_2.0
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the FastAPI backend

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`, with interactive docs at `http://localhost:8000/docs`.

### 4. Run the Streamlit frontend (in a separate terminal)

```bash
streamlit run streamlit_app/app.py
```

The UI will be available at `http://localhost:8501`.

## Running with Docker

Build and run both the API and the UI together in a single container:

```bash
docker build -t heart-disease-prediction .
docker run -p 8000:8000 -p 8501:8501 heart-disease-prediction
```

- API → `http://localhost:8000`
- Streamlit UI → `http://localhost:8501`

## API Reference

### `GET /`
Returns a welcome message confirming the API is running.

### `GET /health`
Returns the API status, version, and whether the model loaded successfully.

```json
{
  "Status": "OK",
  "version": "2.0",
  "model": true
}
```

### `POST /predict`
Runs a prediction for a given patient.

**Request body:**

```json
{
  "age": 54,
  "gender": "M",
  "chest_pain_type": "ATA",
  "resting_bp": 130,
  "cholesterol": 246,
  "fasting_bs": 0,
  "resting_ecg": "Normal",
  "max_hr": 150,
  "exercise_angina": "N",
  "oldpeak": 1.2,
  "st_slope": "Up"
}
```

**Response:**

```json
{
  "prediction": 1,
  "heart_disease_probability": 78.42,
  "message": "Heart disease detected"
}
```

> ⚠️ Exact field values (e.g. accepted strings/codes for `chest_pain_type`, `resting_ecg`, `st_slope`) follow the schema defined in `schema/user.py` — check the auto-generated docs at `/docs` for the full validation rules.

## Disclaimer

This project is intended for **educational and demonstration purposes only**. It is **not a medical device** and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider with any questions regarding a medical condition.

## License

No license has been specified for this repository. Consider adding one (e.g. MIT) if you plan to share or accept contributions.