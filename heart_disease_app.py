
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import classification_report
import warnings
warnings.filterwarnings('ignore')

# Page config
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 2rem;
    }
    .prediction-box {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .high-risk {
        background-color: #FFE5E5;
        border-left: 5px solid #FF6B6B;
    }
    .low-risk {
        background-color: #E5F5E5;
        border-left: 5px solid #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    try:
        with open('optimized_xgb_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('feature_names.pkl', 'rb') as f:
            feature_names = pickle.load(f)
        with open('model_info.pkl', 'rb') as f:
            model_info = pickle.load(f)
        return model, feature_names, model_info
    except FileNotFoundError:
        st.error("Model files not found. Please ensure all model files are in the same directory.")
        return None, None, None

def main():
    st.markdown('<h1 class="main-header">🫀 Heart Disease Risk Predictor</h1>', unsafe_allow_html=True)

    # Load model
    model, feature_names, model_info = load_model()
    if model is None:
        st.stop()

    # Sidebar with model info
    st.sidebar.header("🤖 Model Information")
    st.sidebar.info(f"""
    **Model Type:** {model_info['model_type']}
    **Accuracy:** {model_info['accuracy']*100:.2f}%
    **Features:** {model_info['feature_count']}
    **Optimization Trials:** {model_info['optimization_trials']}
    **Training Date:** {model_info['training_date']}
    """)

    # Sidebar input fields
    st.sidebar.header("📋 Patient Information")
    st.sidebar.markdown("Enter the patient's medical information below:")

    with st.sidebar:
        age = st.slider("Age (years)", 20, 100, 50)
        sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
        cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3], 
                         help="0: Typical angina, 1: Atypical angina, 2: Non-anginal pain, 3: Asymptomatic")
        trestbps = st.slider("Resting Blood Pressure (mmHg)", 80, 200, 120)
        chol = st.slider("Cholesterol (mg/dl)", 100, 400, 200)
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1], 
                          format_func=lambda x: "No" if x == 0 else "Yes")
        restecg = st.selectbox("Resting ECG", [0, 1, 2],
                              help="0: Normal, 1: ST-T abnormality, 2: Left ventricular hypertrophy")
        thalach = st.slider("Maximum Heart Rate Achieved", 60, 220, 150)
        exang = st.selectbox("Exercise Induced Angina", [0, 1],
                            format_func=lambda x: "No" if x == 0 else "Yes")
        oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0, 0.1)
        slope = st.selectbox("ST Slope", [0, 1, 2],
                            help="0: Upsloping, 1: Flat, 2: Downsloping")
        ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3])
        thal = st.selectbox("Thalassemia", [0, 1, 2, 3],
                           help="0: Normal, 1: Fixed defect, 2: Reversible defect, 3: Unknown")

    # Main content
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📊 Patient Profile Summary")

        # Create patient summary
        summary_data = {
            "Attribute": ["Age", "Sex", "Resting BP", "Cholesterol", "Max Heart Rate"],
            "Value": [f"{age} years", "Male" if sex == 1 else "Female", 
                     f"{trestbps} mmHg", f"{chol} mg/dl", f"{thalach} bpm"],
            "Status": ["Normal" if 20 <= age <= 65 else "High Risk",
                      "N/A",
                      "Normal" if 90 <= trestbps <= 140 else "Abnormal",
                      "Normal" if chol <= 200 else "High",
                      "Normal" if thalach >= 150 else "Low"]
        }

        summary_df = pd.DataFrame(summary_data)
        st.table(summary_df)

    with col2:
        if st.button("🔍 Predict Risk", type="primary"):
            # Create feature array in the correct order
            features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                                thalach, exang, oldpeak, slope, ca, thal]])

            # Make prediction
            prediction = model.predict(features)[0]
            probability = model.predict_proba(features)[0]

            # Display prediction
            risk_prob = probability[1] * 100

            if prediction == 1:
                st.markdown(f"""
                <div class="prediction-box high-risk">
                    <h3>⚠️ HIGH RISK</h3>
                    <p><strong>Risk Probability: {risk_prob:.1f}%</strong></p>
                    <p>This patient shows indicators of potential heart disease. 
                    Please consult with a cardiologist for further evaluation.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="prediction-box low-risk">
                    <h3>✅ LOW RISK</h3>
                    <p><strong>Risk Probability: {risk_prob:.1f}%</strong></p>
                    <p>This patient shows low indicators of heart disease risk. 
                    Continue regular health monitoring.</p>
                </div>
                """, unsafe_allow_html=True)

            # Risk gauge
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = risk_prob,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Heart Disease Risk (%)"},
                gauge = {
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 30], 'color': "lightgreen"},
                        {'range': [30, 70], 'color': "yellow"},
                        {'range': [70, 100], 'color': "red"}],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 90}}))

            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)

    # Feature importance
    st.subheader("🎯 Feature Importance")

    if hasattr(model, 'feature_importances_'):
        feature_importance_df = pd.DataFrame({
            'Feature': ['Age', 'Sex', 'Chest Pain', 'Resting BP', 'Cholesterol',
                       'Fasting Blood Sugar', 'Resting ECG', 'Max Heart Rate',
                       'Exercise Angina', 'ST Depression', 'ST Slope',
                       'Major Vessels', 'Thalassemia'],
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=True)

        fig = px.bar(feature_importance_df, x='Importance', y='Feature', orientation='h',
                    title="Feature Importance in Heart Disease Prediction")
        st.plotly_chart(fig, use_container_width=True)

    # About section
    with st.expander("ℹ️ About This App"):
        st.markdown(f"""
        This Heart Disease Risk Predictor uses an **XGBoost machine learning model** 
        trained on clinical data to assess the probability of heart disease.

        **Model Performance:**
        - Accuracy: {model_info['accuracy']*100:.2f}%
        - Optimized using Optuna hyperparameter tuning ({model_info['optimization_trials']} trials)
        - Cross-validated for reliability

        **Important Note:**
        This tool is for educational purposes only and should not replace professional medical advice.
        Always consult with healthcare professionals for medical decisions.

        **Model Details:**
        - Training Date: {model_info['training_date']}
        - Features Used: {model_info['feature_count']}
        - Best Parameters: Optimized via Bayesian optimization
        """)

if __name__ == "__main__":
    main()
