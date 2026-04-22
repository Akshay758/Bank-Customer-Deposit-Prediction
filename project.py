import streamlit as st
import joblib
import numpy as np
import base64

def set_bg_image(image_file): 
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    st.markdown(    #st.markdown use cheyunnath html and css apply cheyan anne.
        f"""
        <style>

        /* Background image */
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}

        /* Title */
        h1 {{
            color: #ffffff;
        }}

        /* Paragraph text (subheading fix) */
        p {{
            color: #ffffff !important;
            font-size: 18px;
            font-weight: 500;
        }}

        /* Labels */
        label {{
            color: #ffffff !important;
            font-size: 16px;
            font-weight: 500;
        }}

        /* INPUT BOX STYLE */
        input {{
            color: #000000 !important;
            background-color: #f0f0f0 !important;
            border-radius: 10px !important;
        }}

        /* NUMBER INPUT */
        div[data-baseweb="input"] {{
            border-radius: 10px !important;
        }}

        /* SELECTBOX */
        div[data-baseweb="select"] > div {{
            background-color: #f0f0f0 !important;
            border-radius: 10px !important;
        }}

        /* Button */
        div.stButton > button {{
            color: white;
            background-color: #1f2937;
            font-size: 16px;
            font-weight: 600;
            border-radius: 10px;
            border: none;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

# --- Set background image ---
set_bg_image("3451499.jpg")

# --- Load model ---
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

job_le = joblib.load("job_le.pkl")
marital_le = joblib.load("marital_le.pkl")
education_le = joblib.load("education_le.pkl")
contact_le = joblib.load("contact_le.pkl")
month_le = joblib.load("month_le.pkl")
poutcome_le = joblib.load("poutcome_le.pkl")

# --- Title ---
st.markdown(
"""
<h1 style='font-size:42px; font-weight:700; white-space:nowrap;'>
🏦 Bank Customer Deposit Prediction
</h1>
""",
unsafe_allow_html=True
)

st.markdown( 
"Enter customer details to predict whether they will subscribe to a bank deposit."
)


age = st.number_input("Age")
job = st.selectbox("Job", [
"management","blue-collar","technician","admin.","services","retired",
"self-employed","student","unemployed","entrepreneur","housemaid","unknown"
])
marital = st.selectbox("Marital", [
"married","single","divorced"
])
education = st.selectbox("Education", [
"secondary","tertiary","primary","unknown"
])
default = st.selectbox("Default (0 = No, 1 = Yes)", [0,1])
balance = st.number_input("Balance")
housing = st.selectbox("Housing Loan (0 = No, 1 = Yes)", [0,1])
loan = st.selectbox("Personal Loan (0 = No, 1 = Yes)", [0,1])
contact = st.selectbox("Contact", [
"cellular","telephone","unknown"
])

day = st.number_input("Day")

month = st.selectbox("Month", [
"jan","feb","mar","apr","may","jun",
"jul","aug","sep","oct","nov","dec"
])

campaign = st.number_input("Campaign")
pdays = st.number_input("Pdays")
previous = st.number_input("Previous")
poutcome = st.selectbox("Poutcome", [
"unknown","failure","success","other"
])

# --- Prediction ---
if st.button("Predict"):

    job = job_le.transform([job])[0]
    marital = marital_le.transform([marital])[0]
    education = education_le.transform([education])[0]
    contact = contact_le.transform([contact])[0]
    month = month_le.transform([month])[0]
    poutcome = poutcome_le.transform([poutcome])[0]

    features = np.array([[age, job, marital, education, default, balance,
                          housing, loan, contact, day, month, campaign,
                          pdays, previous, poutcome]])

    features_scaled = scaler.transform(features)    #scaler cheyunnu

    prediction = model.predict(features_scaled)[0]
    prob = model.predict_proba(features_scaled)[0]

    if prediction == 1:
        st.success("Customer WILL subscribe to the deposit")
        st.write(f"Probability: {prob[1]*100:.2f}%")
    else:
        st.error("Customer will NOT subscribe")
        st.write(f"Probability: {prob[0]*100:.2f}%")