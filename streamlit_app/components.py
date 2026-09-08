"""
Reusable UI components for the Heart Disease Prediction dashboard.
Each function renders one section of the page. Kept free of ML logic --
all prediction calls happen in streamlit_app/app.py via utils.py.
"""

import streamlit as st

from utils import (
    GENDER_OPTIONS,
    CHEST_PAIN_OPTIONS,
    RESTING_ECG_OPTIONS,
    EXERCISE_ANGINA_OPTIONS,
    ST_SLOPE_OPTIONS,
    FASTING_BS_OPTIONS,
)


def render_hero():
    st.markdown(
        '<div class="hero-wrap">'
        '<div class="hero-badge">🫀 AI &nbsp;•&nbsp; Machine Learning &nbsp;•&nbsp; Healthcare</div>'
        '<h1 class="hero-title">Heart Disease Prediction</h1>'
        '<p class="hero-subtitle" '
        'style="max-width:620px; margin:0 auto; text-align:center; line-height:1.6;">'
        "AI-powered heart disease prediction using Machine Learning. "
        "Enter patient clinical data below to get an instant, model-based risk assessment."
        "</p>"
        "</div>",
        unsafe_allow_html=True,
    )


def section_header(icon: str, title: str, caption: str = ""):
    st.markdown(
        f"""
        <div class="section-header">
            <span class="section-icon">{icon}</span>
            <p class="section-title">{title}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if caption:
        st.markdown(f'<p class="section-caption">{caption}</p>', unsafe_allow_html=True)


def render_patient_form():
    """Renders the patient information form and returns a dict of raw UI values."""
    section_header("📋", "Patient Information", "Fill in the clinical details below.")

    st.markdown('<div class="form-card">', unsafe_allow_html=True)

    st.markdown('<p class="form-group-label">👤 Demographics</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        age = st.number_input("Age (years)", min_value=1, max_value=120, value=54, step=1)
    with c2:
        gender = st.selectbox("Gender", options=list(GENDER_OPTIONS.keys()), index=0)

    st.markdown('<p class="form-group-label">❤️ Vitals</p>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        resting_bp = st.number_input(
            "Resting Blood Pressure (mm Hg)", min_value=50, max_value=250, value=130, step=1
        )
    with c2:
        cholesterol = st.number_input(
            "Cholesterol (mg/dL)", min_value=0, max_value=700, value=246, step=1
        )
    with c3:
        max_hr = st.number_input(
            "Max Heart Rate Achieved", min_value=60, max_value=250, value=150, step=1
        )

    st.markdown('<p class="form-group-label">🩺 Clinical Findings</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        chest_pain_type = st.selectbox(
            "Chest Pain Type", options=list(CHEST_PAIN_OPTIONS.keys()), index=1
        )
    with c2:
        resting_ecg = st.selectbox(
            "Resting ECG Result", options=list(RESTING_ECG_OPTIONS.keys()), index=0
        )

    c1, c2, c3 = st.columns(3)
    with c1:
        fasting_bs = st.selectbox(
            "Fasting Blood Sugar", options=list(FASTING_BS_OPTIONS.keys()), index=0
        )
    with c2:
        exercise_angina = st.selectbox(
            "Exercise-Induced Angina", options=list(EXERCISE_ANGINA_OPTIONS.keys()), index=1
        )
    with c3:
        st_slope = st.selectbox(
            "ST Slope (Peak Exercise)", options=list(ST_SLOPE_OPTIONS.keys()), index=1
        )

    st.markdown('<p class="form-group-label">📈 Exercise Test</p>', unsafe_allow_html=True)
    oldpeak = st.slider(
        "Oldpeak — ST Depression Induced by Exercise",
        min_value=-5.0,
        max_value=10.0,
        value=1.2,
        step=0.1,
    )

    st.markdown("</div>", unsafe_allow_html=True)

    return {
        "age": age,
        "gender": gender,
        "chest_pain_type": chest_pain_type,
        "resting_bp": resting_bp,
        "cholesterol": cholesterol,
        "fasting_bs": fasting_bs,
        "resting_ecg": resting_ecg,
        "max_hr": max_hr,
        "exercise_angina": exercise_angina,
        "oldpeak": oldpeak,
        "st_slope": st_slope,
    }


def render_result(prediction: int, probability: float):
    """
    prediction: 0 or 1 (from the unmodified RF model)
    probability: float 0-1, probability of class 1 (heart disease)
    """
    pct = round(probability * 100, 2)
    is_positive = prediction == 1

    status_class = "positive" if is_positive else "negative"
    icon = "⚠️" if is_positive else "✅"
    title = "Heart Disease Detected" if is_positive else "No Heart Disease Detected"
    subtitle = (
        "The model predicts a higher likelihood of heart disease based on the provided data."
        if is_positive
        else "The model predicts a lower likelihood of heart disease based on the provided data."
    )
    value_color = "#f87171" if is_positive else "#4ade80"

    st.markdown(
        f"""
        <div class="result-card {status_class}">
            <div class="result-icon">{icon}</div>
            <p class="result-title {status_class}">{title}</p>
            <p class="result-subtitle">{subtitle}</p>
            <p class="probability-value" style="color:{value_color};">{pct}%</p>
            <p class="probability-label">Model-Estimated Probability of Heart Disease</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.progress(min(max(probability, 0.0), 1.0))

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f"""<div class="mini-card">
                    <div class="mini-card-value">{prediction}</div>
                    <div class="mini-card-label">Raw Prediction Class</div>
                </div>""",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f"""<div class="mini-card">
                    <div class="mini-card-value">{pct}%</div>
                    <div class="mini-card-label">Heart Disease Probability</div>
                </div>""",
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f"""<div class="mini-card">
                    <div class="mini-card-value">{round(100 - pct, 2)}%</div>
                    <div class="mini-card-label">No Disease Probability</div>
                </div>""",
            unsafe_allow_html=True,
        )


def render_about_model():
    section_header("🤖", "About the Model")
    st.markdown(
        """
        <div class="glass-card">
            <p style="color:#cbd5e1; line-height:1.7; margin:0 0 0.8rem 0;">
                This app is powered by a <strong>Random Forest Classifier</strong>, a machine
                learning model that builds many decision trees on different subsets of the
                training data and combines their votes into a single, more reliable prediction.
                Think of it as asking a large panel of doctors instead of just one — each "tree"
                gives its own opinion, and the forest goes with the majority.
            </p>
            <p style="color:#cbd5e1; line-height:1.7; margin:0;">
                The model was trained on historical patient records containing clinical
                measurements such as blood pressure, cholesterol, ECG results, and exercise
                test outcomes, learning the patterns that are statistically associated with
                heart disease. It outputs both a class prediction (disease / no disease) and a
                probability score reflecting the model's confidence.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_feature_glossary():
    section_header("📖", "What Do These Parameters Mean?")

    features = [
        ("Age", "The patient's age in years."),
        ("Gender", "Biological sex of the patient (Male / Female)."),
        ("Chest Pain Type", "The category of chest pain experienced — Typical Angina, Atypical Angina, Non-Anginal Pain, or Asymptomatic."),
        ("Resting Blood Pressure", "Blood pressure measured at rest, in mm Hg."),
        ("Cholesterol", "Serum cholesterol level in mg/dL."),
        ("Fasting Blood Sugar", "Whether fasting blood sugar exceeds 120 mg/dL (a diabetes indicator)."),
        ("Resting ECG", "Resting electrocardiogram results — Normal, ST-T wave abnormality, or signs of left ventricular hypertrophy."),
        ("Max Heart Rate", "The highest heart rate achieved during a stress/exercise test."),
        ("Exercise-Induced Angina", "Whether chest pain was triggered by physical exercise."),
        ("Oldpeak", "ST depression on the ECG induced by exercise relative to rest — a marker of reduced blood flow to the heart."),
        ("ST Slope", "The slope of the ST segment during peak exercise — Upsloping, Flat, or Downsloping."),
    ]

    cols = st.columns(2)
    for i, (name, desc) in enumerate(features):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="feature-item">
                    <div class="feature-name">{name}</div>
                    <div class="feature-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_developer_section():
    section_header("👨‍💻", "About the Developer")

    st.markdown(
        """
        <div class="dev-card">
            <div class="dev-avatar">MK</div>
            <p class="dev-name">Muhammad Kabeer Jawed</p>
            <p class="dev-role">Computer Science Student | AI/ML Enthusiast</p>
            <div>
                <span class="dev-tag">🤖 Machine Learning</span>
                <span class="dev-tag">🐍 Python</span>
                <span class="dev-tag">⚡ FastAPI</span>
                <span class="dev-tag">📊 Streamlit</span>
                <span class="dev-tag">📈 Data Science</span>
            </div>
            <div class="dev-link-row">
                <a class="dev-link" href="#" target="_blank">🐙 GitHub — add your profile URL</a>
                <a class="dev-link" href="#" target="_blank">💼 LinkedIn — add your profile URL</a>
                <a class="dev-link" href="#" target="_blank">✉️ Email — add your email address</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer():
    st.markdown(
        """
        <div class="app-footer">
            <p>Built with <span class="footer-strong">Python, Streamlit and Scikit-learn</span></p>
            <div class="disclaimer-box">
                ⚕️ <strong>Medical Disclaimer:</strong> This application is a machine learning
                portfolio project intended for educational and demonstration purposes only.
                It is <strong>not</strong> a certified medical device and must not be used as a
                substitute for professional medical advice, diagnosis, or treatment. Always
                consult a qualified healthcare provider with any questions regarding a medical
                condition.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
