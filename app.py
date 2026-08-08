import streamlit as st
import pandas as pd
import joblib

# Set page layout and title
st.set_page_config(page_title="Customer Churn Predictor", layout="wide")

st.title("📊 Customer Churn Prediction Dashboard")
st.markdown("Enter customer details below to calculate the real-time probability of churn.")

# Load model and feature metadata
@st.cache_resource
def load_artifacts():
    model = joblib.load('telco_churn_model_pipeline.pkl')
    config = joblib.load('feature_config.pkl')
    return model, config

model, config = load_artifacts()

# Build Input Form
st.sidebar.header("Customer Profile Settings")

input_data = {}

# Numerical Inputs
st.sidebar.subheader("Numerical Features")
input_data['tenure'] = st.sidebar.slider("Tenure (Months)", 0, 72, 12)
input_data['MonthlyCharges'] = st.sidebar.number_input("Monthly Charges ($)", min_value=18.0, max_value=120.0, value=65.0)
input_data['TotalCharges'] = st.sidebar.number_input("Total Charges ($)", min_value=0.0, max_value=9000.0, value=float(input_data['tenure'] * input_data['MonthlyCharges']))

# Engineered Numerical Features
input_data['Charge_Ratio'] = input_data['TotalCharges'] / (input_data['MonthlyCharges'] + 1e-5)
input_data['SeniorCitizen'] = st.sidebar.selectbox("Senior Citizen", [0, 1])

# Tenure Grouping Logic
tenure_val = input_data['tenure']
if tenure_val <= 12:
    input_data['Tenure_Group'] = '0-1 Yr'
elif tenure_val <= 24:
    input_data['Tenure_Group'] = '1-2 Yrs'
elif tenure_val <= 48:
    input_data['Tenure_Group'] = '2-4 Yrs'
elif tenure_val <= 60:
    input_data['Tenure_Group'] = '4-5 Yrs'
else:
    input_data['Tenure_Group'] = '5+ Yrs'

# Categorical Inputs
st.sidebar.subheader("Service & Demographics")
services_count = 0
service_cols = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

for col in config['cat_cols']:
    if col != 'Tenure_Group':
        options = config['categorical_options'][col]
        val = st.sidebar.selectbox(col, options)
        input_data[col] = val
        if col in service_cols and val == 'Yes':
            services_count += 1

input_data['Total_Services'] = services_count

# Prediction Trigger
if st.button("Predict Churn Probability", type="primary"):
    input_df = pd.DataFrame([input_data])
    
    # Predict Probability
    prob = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Churn Probability", value=f"{prob * 100:.1f}%")
        
    with col2:
        if prob > 0.5:
            st.error("⚠️ High Risk of Churn! Customer requires retention targeting.")
        else:
            st.success("✅ Low Risk of Churn. Customer is stable.")
            
    # Show Raw Feature Payload
    with st.expander("View Input Payload Summary"):
        st.json(input_data)
