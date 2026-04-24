import streamlit as st
from prediction_helper import predict

# ------------------ PAGE CONFIG ------------------ #
st.set_page_config(
    page_title="Insurance Cost Predictor",
    layout="wide"
)

# ------------------ FORM KEY (RESET ENGINE) ------------------ #
if "form_key" not in st.session_state:
    st.session_state.form_key = 0

# ------------------ PROFESSIONAL CSS ------------------ #
st.markdown("""
<style>

/* ===== GLOBAL BACKGROUND (PREMIUM BLUE GRADIENT) ===== */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at 10% 20%, rgba(59,130,246,0.15), transparent 40%),
                radial-gradient(circle at 90% 10%, rgba(96,165,250,0.12), transparent 40%),
                linear-gradient(135deg, #f8fbff, #eef5ff);
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

/* Remove header white bar */
[data-testid="stHeader"] {
    background: transparent;
}

/* Layout padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* ===== TITLE ===== */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #0f172a;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #475569;
    margin-bottom: 35px;
}

/* ===== CARD ===== */
.card {
    background: white;
    padding: 24px;
    border-radius: 16px;
    border: 1px solid #e2e8f0;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

/* Section title */
.section-title {
    font-size: 18px;
    font-weight: 600;
    color: #1e3a8a;
    margin-bottom: 12px;
}

/* ===== INPUT LABEL FIX (VERY IMPORTANT) ===== */
label {
    color: #1e293b !important;
    font-size: 14px !important;
    font-weight: 600 !important;
}

/* Input text */
input {
    color: #111827 !important;
}

/* Selectbox text */
div[data-baseweb="select"] {
    color: #111827 !important;
}

/* ===== BUTTON ===== */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #2563eb, #1d4ed8);
    color: white;
    font-size: 18px;
    font-weight: 600;
    border-radius: 10px;
    padding: 12px;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #1d4ed8, #1e40af);
    transform: translateY(-1px);
}

/* ===== RESULT ===== */
.result {
    background: linear-gradient(135deg, #1e40af, #2563eb);
    color: white;
    padding: 25px;
    border-radius: 14px;
    text-align: center;
    font-size: 26px;
    font-weight: 600;
    margin-top: 25px;
}

/* ===== INPUT FIELD FIX (CRITICAL) ===== */

/* Number input + text input */
input[type="number"], input[type="text"] {
    background-color: #ffffff !important;
    color: #111827 !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 8px !important;
    padding: 8px !important;
    font-size: 14px !important;
}

/* On focus (when user clicks input) */
input[type="number"]:focus, input[type="text"]:focus {
    border: 1px solid #2563eb !important;
    box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2) !important;
    outline: none !important;
}

/* Selectbox (dropdown) */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #111827 !important;
    border-radius: 8px !important;
    border: 1px solid #cbd5e1 !important;
}

/* Dropdown menu items */
ul[role="listbox"] {
    background-color: #ffffff !important;
    color: #111827 !important;
}

/* Placeholder */
input::placeholder {
    color: #6b7280 !important;
}
/* ===== SECTION HEADER (FIXED + PREMIUM) ===== */
.section-header {
    font-size: 16px;
    font-weight: 600;
    color: #1e293b;
    background: rgba(37, 99, 235, 0.08);
    padding: 8px 14px;
    border-radius: 999px;
    display: inline-block;
    margin-bottom: 12px;
    border: 1px solid rgba(37, 99, 235, 0.15);
}

/* Add spacing between sections */
.section-block {
    margin-bottom: 25px;
}


</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------ #
st.markdown('<div class="title">🏥 Health Insurance Cost Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart premium estimation based on your profile</div>', unsafe_allow_html=True)

# ------------------ OPTIONS ------------------ #
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure',
        'Diabetes & High blood pressure', 'Thyroid',
        'Heart disease', 'High blood pressure & Heart disease',
        'Diabetes & Thyroid', 'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# ------------------ LAYOUT ------------------ #
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="section-header">👤 Personal Details</div>', unsafe_allow_html=True)
    age = st.number_input('Age', 18, 100, key=f"age_{st.session_state.form_key}")
    dependants = st.number_input('Number of Dependants', 0, 20, key=f"dep_{st.session_state.form_key}")
    income = st.number_input('Income (Lakhs)', 0, 200, key=f"inc_{st.session_state.form_key}")

with col2:
    st.markdown('<div class="section-header">🧬 Health Information</div>', unsafe_allow_html=True)
    genetical_risk = st.number_input('Genetic Risk Score (0–5)', 0, 5, key=f"risk_{st.session_state.form_key}")
    bmi = st.selectbox('BMI Category', categorical_options['BMI Category'], key=f"bmi_{st.session_state.form_key}")
    smoking = st.selectbox('Smoking Status', categorical_options['Smoking Status'], key=f"smoking_{st.session_state.form_key}")

with col3:
    st.markdown('<div class="section-header">📋 Policy Details</div>', unsafe_allow_html=True)
    plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'], key=f"plan_{st.session_state.form_key}")
    employment = st.selectbox('Employment Status', categorical_options['Employment Status'], key=f"emp_{st.session_state.form_key}")
    medical = st.selectbox('Medical History', categorical_options['Medical History'], key=f"med_{st.session_state.form_key}")
    gender = st.selectbox('Gender', categorical_options['Gender'], key=f"gender_{st.session_state.form_key}")
    marital = st.selectbox('Marital Status', categorical_options['Marital Status'], key=f"marital_{st.session_state.form_key}")
    region = st.selectbox('Region', categorical_options['Region'], key=f"region_{st.session_state.form_key}")

# ------------------ INPUT DICT ------------------ #
input_dict = {
    'Age': age,
    'Number of Dependants': dependants,
    'Income in Lakhs': income,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': plan,
    'Employment Status': employment,
    'Gender': gender,
    'Marital Status': marital,
    'BMI Category': bmi,
    'Smoking Status': smoking,
    'Region': region,
    'Medical History': medical
}

# ------------------ BUTTONS ------------------ #
st.markdown("<br>", unsafe_allow_html=True)

center_col = st.columns([1,2,1])[1]

with center_col:
    col_btn1, col_btn2 = st.columns(2)

    with col_btn1:
        calculate = st.button("Calculate Premium")

    with col_btn2:
        reset = st.button("Reset")

# ------------------ RESET LOGIC ------------------ #
if reset:
    st.session_state.form_key += 1
    st.rerun()

# ------------------ RESULT ------------------ #
if calculate:
    with st.spinner("Calculating..."):
        prediction = predict(input_dict)

    st.markdown(
        f'<div class="result">Estimated Premium: ₹ {prediction}</div>',
        unsafe_allow_html=True
    )