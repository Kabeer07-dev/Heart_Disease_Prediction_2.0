from pydantic import BaseModel, Field
from typing import Literal


class PatientModel(BaseModel):

    age: int = Field(
        ...,
        ge=1,
        le=120,
        description="Patient age in years",
        examples=[54]
    )

    gender: Literal["M", "F"] = Field(
        ...,
        description="Patient gender",
        examples=["M"]
    )

    chest_pain_type: Literal["ATA", "NAP", "ASY", "TA"] = Field(
        ...,
        description="Type of chest pain",
        examples=["ATA"]
    )

    resting_bp: int = Field(
        ...,
        ge=50,
        le=250,
        description="Resting blood pressure in mm Hg",
        examples=[130]
    )

    cholesterol: int = Field(
        ...,
        ge=0,
        le=700,
        description="Serum cholesterol in mg/dL",
        examples=[246]
    )

    fasting_bs: Literal[0, 1] = Field(
        ...,
        description="Fasting blood sugar > 120 mg/dL (1 = Yes, 0 = No)",
        examples=[0]
    )

    resting_ecg: Literal["Normal", "ST", "LVH"] = Field(
        ...,
        description="Resting electrocardiogram result",
        examples=["Normal"]
    )

    max_hr: int = Field(
        ...,
        ge=60,
        le=250,
        description="Maximum heart rate achieved",
        examples=[150]
    )

    exercise_angina: Literal["Y", "N"] = Field(
        ...,
        description="Exercise-induced angina (Y = Yes, N = No)",
        examples=["N"]
    )

    oldpeak: float = Field(
        ...,
        ge=-5,
        le=10,
        description="ST depression induced by exercise",
        examples=[1.2]
    )

    st_slope: Literal["Up", "Flat", "Down"] = Field(
        ...,
        description="Slope of the peak exercise ST segment",
        examples=["Flat"]
    )

    