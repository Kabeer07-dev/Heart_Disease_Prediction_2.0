"""
Custom CSS for the Heart Disease Prediction dashboard.
Injected once from streamlit_app/app.py via st.markdown(..., unsafe_allow_html=True).
"""

CUSTOM_CSS = """
<style>

/* ---------- Fonts ---------- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ---------- Palette (CSS variables) ---------- */
:root {
    --bg-primary: #0b1220;
    --bg-secondary: #111a2e;
    --card-bg: #141d33;
    --card-border: #223257;
    --accent-teal: #14b8a6;
    --accent-blue: #3b82f6;
    --accent-red: #ef4444;
    --accent-green: #22c55e;
    --text-primary: #f1f5f9;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
}

/* ---------- App background ---------- */
.stApp {
    background: radial-gradient(circle at 15% 0%, #14264a 0%, #0b1220 45%, #0a0f1c 100%);
    color: var(--text-primary);
}

/* Hide default streamlit chrome for a cleaner look */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header[data-testid="stHeader"] {background: transparent;}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1150px;
}

/* ---------- Hero ---------- */
.hero-wrap {
    text-align: center;
    padding: 2.6rem 1.5rem 2.2rem 1.5rem;
    margin-bottom: 1.8rem;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(20,184,166,0.14) 0%, rgba(59,130,246,0.14) 100%);
    border: 1px solid rgba(148, 163, 184, 0.12);
    
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(20, 184, 166, 0.15);
    color: #2dd4bf;
    border: 1px solid rgba(45, 212, 191, 0.35);
    padding: 6px 16px;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-bottom: 1.1rem;
}

.hero-title {
    font-family: 'Poppins', sans-serif;
    font-weight: 800;
    font-size: 2.6rem;
    line-height: 1.15;
    margin: 0 0 0.6rem 0;
    background: linear-gradient(90deg, #5eead4 0%, #60a5fa 55%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle {
    font-size: 1.08rem;
    color: var(--text-secondary);
    max-width: 620px !important;
    margin: 0 auto !important;
    font-weight: 400;
    text-align: center !important;
    line-height: 1.6;
    display: block;
}
/* ---------- Section headers ---------- */
.section-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 2.2rem 0 1rem 0;
}

.section-icon {
    font-size: 1.4rem;
}

.section-title {
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
    font-size: 1.35rem;
    color: var(--text-primary);
    margin: 0;
}

.section-caption {
    color: var(--text-secondary);
    font-size: 0.92rem;
    margin: -0.4rem 0 1.1rem 0;
}

/* ---------- Cards ---------- */
.glass-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 18px;
    padding: 1.6rem 1.7rem;
    margin-bottom: 1.1rem;
    box-shadow: 0 4px 24px rgba(0,0,0,0.25);
}

.form-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 20px;
    padding: 1.8rem 2rem 1.4rem 2rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 30px rgba(0,0,0,0.3);
}

.form-group-label {
    font-weight: 600;
    font-size: 1rem;
    color: #5eead4;
    margin: 0.4rem 0 0.9rem 0;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* ---------- Streamlit input theming ---------- */
div[data-testid="stNumberInput"] input,
div[data-baseweb="select"] > div,
div[data-testid="stTextInput"] input {
    background-color: #0e1830 !important;
    border: 1px solid var(--card-border) !important;
    border-radius: 10px !important;
    color: var(--text-primary) !important;
}

div[data-baseweb="select"] > div:hover {
    border-color: var(--accent-teal) !important;
}

label[data-testid="stWidgetLabel"] p {
    color: var(--text-secondary) !important;
    font-weight: 500;
    font-size: 0.88rem;
}

/* Slider */
div[data-testid="stSlider"] > div > div > div > div {
    background: linear-gradient(90deg, #2dd4bf, #60a5fa) !important;
}

/* ---------- Predict button ---------- */
div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #14b8a6 0%, #3b82f6 100%);
    color: #ffffff;
    font-weight: 700;
    font-size: 1.08rem;
    padding: 0.85rem 1rem;
    border-radius: 14px;
    border: none;
    box-shadow: 0 8px 24px rgba(20, 184, 166, 0.25);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    letter-spacing: 0.01em;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 32px rgba(59, 130, 246, 0.35);
    color: #ffffff;
    border: none;
}

div.stButton > button:active {
    transform: translateY(0px);
}

/* ---------- Result cards ---------- */
.result-card {
    border-radius: 20px;
    padding: 2rem 2.2rem;
    margin: 1.2rem 0 1.6rem 0;
    border: 1px solid;
    text-align: center;
}

.result-card.positive {
    background: linear-gradient(135deg, rgba(239,68,68,0.14) 0%, rgba(239,68,68,0.04) 100%);
    border-color: rgba(239, 68, 68, 0.4);
}

.result-card.negative {
    background: linear-gradient(135deg, rgba(34,197,94,0.14) 0%, rgba(34,197,94,0.04) 100%);
    border-color: rgba(34, 197, 94, 0.4);
}

.result-icon {
    font-size: 2.6rem;
    margin-bottom: 0.4rem;
}

.result-title {
    font-family: 'Poppins', sans-serif;
    font-weight: 800;
    font-size: 1.6rem;
    margin: 0.2rem 0 0.3rem 0;
}

.result-title.positive { color: #f87171; }
.result-title.negative { color: #4ade80; }

.result-subtitle {
    color: var(--text-secondary);
    font-size: 0.98rem;
    margin-bottom: 0.2rem;
}

.probability-value {
    font-family: 'Poppins', sans-serif;
    font-weight: 800;
    font-size: 2.4rem;
    margin: 0.6rem 0 0.1rem 0;
}

.probability-label {
    color: var(--text-muted);
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-weight: 600;
}

/* ---------- Metric-style mini cards ---------- */
.mini-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 14px;
    padding: 1.1rem 1.3rem;
    text-align: center;
}

.mini-card-value {
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
    font-size: 1.3rem;
    color: var(--text-primary);
}

.mini-card-label {
    color: var(--text-muted);
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 0.2rem;
}

/* ---------- Feature glossary ---------- */
.feature-item {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-left: 3px solid var(--accent-teal);
    border-radius: 12px;
    padding: 0.85rem 1.1rem;
    margin-bottom: 0.6rem;
}

.feature-name {
    font-weight: 700;
    color: #5eead4;
    font-size: 0.92rem;
}

.feature-desc {
    color: var(--text-secondary);
    font-size: 0.86rem;
    margin-top: 2px;
}

/* ---------- Developer card ---------- */
.dev-card {
    background: linear-gradient(135deg, rgba(59,130,246,0.10) 0%, rgba(20,184,166,0.10) 100%);
    border: 1px solid var(--card-border);
    border-radius: 20px;
    padding: 1.8rem 2rem;
}

.dev-avatar {
    width: 68px;
    height: 68px;
    border-radius: 50%;
    background: linear-gradient(135deg, #2dd4bf, #60a5fa);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Poppins', sans-serif;
    font-weight: 800;
    font-size: 1.5rem;
    color: #0b1220;
    margin-bottom: 0.8rem;
}

.dev-name {
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
    font-size: 1.25rem;
    color: var(--text-primary);
    margin: 0;
}

.dev-role {
    color: #5eead4;
    font-size: 0.92rem;
    font-weight: 500;
    margin: 0.15rem 0 0.9rem 0;
}

.dev-tag {
    display: inline-block;
    background: rgba(148, 163, 184, 0.1);
    border: 1px solid var(--card-border);
    color: var(--text-secondary);
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 0.78rem;
    margin: 0 6px 6px 0;
}

.dev-link-row {
    margin-top: 1rem;
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.dev-link {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    color: var(--text-primary) !important;
    padding: 8px 16px;
    border-radius: 10px;
    font-size: 0.85rem;
    font-weight: 600;
    text-decoration: none !important;
}

.dev-link:hover {
    border-color: var(--accent-teal);
    color: #5eead4 !important;
}

/* ---------- Footer ---------- */
.app-footer {
    text-align: center;
    margin-top: 2.5rem;
    padding-top: 1.6rem;
    border-top: 1px solid var(--card-border);
    color: var(--text-muted);
    font-size: 0.85rem;
}

.app-footer .footer-strong {
    color: var(--text-secondary);
    font-weight: 600;
}

.disclaimer-box {
    background: rgba(239, 68, 68, 0.07);
    border: 1px solid rgba(239, 68, 68, 0.25);
    border-radius: 12px;
    padding: 0.9rem 1.2rem;
    color: #fca5a5;
    font-size: 0.82rem;
    margin-top: 1rem;
    text-align: left;
}

/* Divider */
hr {
    border-color: var(--card-border) !important;
}

</style>
"""
