"""
Streamlit UI for the Heart Disease Prediction project.

Run with:
    streamlit run streamlit_app/app.py

This file only handles layout/flow. All prediction logic lives, unmodified,
in model/model.py; utils.py just translates UI-friendly field names
(e.g. "Gender") into the exact schema the trained model expects (e.g. "Sex").
"""

import sys
from pathlib import Path

import streamlit as st

# Allow `import utils` / `import components` regardless of the directory
# `streamlit run` is launched from.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from styles import CUSTOM_CSS
from components import (
    render_hero,
    render_patient_form,
    render_result,
    render_about_model,
    render_feature_glossary,
    render_developer_section,
    render_footer,
    section_header,
)
from utils import run_prediction


st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="🫀",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

render_hero()

form_values = render_patient_form()

predict_clicked = st.button("🔍  Predict Heart Disease", use_container_width=True)

if predict_clicked:
    with st.spinner("Running the Random Forest model..."):
        try:
            result = run_prediction(form_values)
            section_header("🧾", "Prediction Result")
            render_result(result["prediction"], result["probability"])
        except Exception as e:
            st.error(f"Something went wrong while generating the prediction: {e}")

st.markdown("<br>", unsafe_allow_html=True)
render_about_model()
render_feature_glossary()
render_developer_section()
render_footer()
