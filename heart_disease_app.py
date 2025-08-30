
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
    import joblib
    try:
        # Load the optimized SVM model (85.25% accuracy)
        model = joblib.load('heart_disease_model_optimized.pkl')
        feature_selector = joblib.load('feature_selector.pkl')
        scaler = joblib.load('feature_scaler.pkl')
        
        # Create feature names for the selected features
        feature_names = [
            'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
            'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
        ]
        
        model_info = {
            'model_type': 'Optimized SVM with Feature Selection',
            'accuracy': '85.25%',
            'features_used': 15,
            'total_features': 24
        }
        
        return model, feature_names, model_info, feature_selector, scaler
        
    except FileNotFoundError as e:
        st.error(f"❌ Model files not found: {e}")
        st.error("Please ensure all required model files are in the same directory:")
        st.error("• heart_disease_model_optimized.pkl")
        st.error("• feature_selector.pkl") 
        st.error("• feature_scaler.pkl")
        return None, None, None, None, None

def main():
    st.markdown('<h1 class="main-header">🫀 Heart Disease Risk Predictor</h1>', unsafe_allow_html=True)

    # Load model
    model, feature_names, model_info, feature_selector, scaler = load_model()
    if model is None:
        st.stop()

    # Sidebar with model info
    st.sidebar.header("🤖 Model Information")
    st.sidebar.info(f"""
    **Model Type:** {model_info['model_type']}
    **Accuracy:** {model_info['accuracy']}
    **Features Used:** {model_info.get('features_used', 'N/A')}
    **Total Features:** {model_info.get('total_features', 'N/A')}
    """)

    # Sidebar input fields
    st.sidebar.header("📋 Patient Information")
    st.sidebar.markdown("Enter the patient's medical information below:")

    with st.sidebar:
        age = st.slider("Age (years)", 20, 100, 50, help="Patient age in years")
        
        sex = st.selectbox("Sex", [0, 1], 
                          format_func=lambda x: "Female" if x == 0 else "Male",
                          help="1 = male; 0 = female")
        
        cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3], 
                         format_func=lambda x: {
                             0: "Typical angina", 
                             1: "Atypical angina", 
                             2: "Non-anginal pain", 
                             3: "Asymptomatic"
                         }[x],
                         help="0: Typical angina (chest pain), 1: Atypical angina (chest pain not related to heart), 2: Non-anginal pain (typically esophageal spasms), 3: Asymptomatic (chest pain not showing signs of disease)")
        
        trestbps = st.slider("Resting Blood Pressure (mmHg)", 80, 200, 120,
                            help="Resting blood pressure in mm Hg on admission to the hospital")
        
        chol = st.slider("Serum Cholesterol (mg/dl)", 100, 400, 200,
                        help="Serum cholesterol in mg/dl")
        
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1], 
                          format_func=lambda x: "No" if x == 0 else "Yes",
                          help="1 = true (>120 mg/dl); 0 = false (≤120 mg/dl)")
        
        restecg = st.selectbox("Resting ECG Results", [0, 1, 2],
                              format_func=lambda x: {
                                  0: "Nothing to note", 
                                  1: "ST-T Wave abnormality", 
                                  2: "Left ventricular hypertrophy"
                              }[x],
                              help="0: Nothing to note, 1: ST-T Wave abnormality, 2: Left ventricular hypertrophy")
        
        thalach = st.slider("Maximum Heart Rate Achieved", 60, 220, 150,
                           help="Maximum heart rate achieved during exercise")
        
        exang = st.selectbox("Exercise Induced Angina", [0, 1],
                            format_func=lambda x: "No" if x == 0 else "Yes",
                            help="1 = yes; 0 = no")
        
        oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0, 0.1,
                           help="ST depression (heart potentially not getting enough oxygen) induced by exercise relative to rest")
        
        slope = st.selectbox("Peak Exercise ST Segment Slope", [0, 1, 2],
                            format_func=lambda x: {
                                0: "Upsloping", 
                                1: "Flat", 
                                2: "Downsloping"
                            }[x],
                            help="The slope of the peak exercise ST segment: 0: Upsloping, 1: Flat, 2: Downsloping")
        
        ca = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3],
                         help="Number of major vessels (0-3) colored by fluoroscopy")
        
        thal = st.selectbox("Thalium Stress Result", [1, 3, 6, 7],
                           format_func=lambda x: {
                               1: "Normal", 
                               3: "Fixed defect", 
                               6: "Fixed defect", 
                               7: "Reversible defect"
                           }[x],
                           help="Thalium stress test result: 1,3: Normal, 6: Fixed defect, 7: Reversible defect")

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

            # Process features for optimized model
            if feature_selector is not None and scaler is not None:
                # Create DataFrame with feature names for advanced processing
                feature_df = pd.DataFrame(features, columns=feature_names)
                
                # Apply advanced feature engineering (same as in notebook)
                poly_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
                for feature in poly_features:
                    if feature in feature_df.columns:
                        feature_df[f'{feature}_squared'] = feature_df[feature] ** 2

                # Add interaction terms
                interaction_pairs = [
                    ('age', 'thalach'), ('trestbps', 'chol'), ('age', 'oldpeak'), ('cp', 'thalach')
                ]
                for feat1, feat2 in interaction_pairs:
                    if feat1 in feature_df.columns and feat2 in feature_df.columns:
                        feature_df[f'{feat1}_{feat2}_interaction'] = feature_df[feat1] * feature_df[feat2]

                # Add ratios
                if 'thalach' in feature_df.columns and 'age' in feature_df.columns:
                    feature_df['heart_rate_age_ratio'] = feature_df['thalach'] / (feature_df['age'] + 1)
                if 'chol' in feature_df.columns and 'trestbps' in feature_df.columns:
                    feature_df['chol_bp_ratio'] = feature_df['chol'] / (feature_df['trestbps'] + 1)

                # Scale the features
                features_scaled = scaler.transform(feature_df)
                
                # Apply feature selection
                features_selected = feature_selector.transform(features_scaled)
                
                # Make prediction with optimized model
                prediction = model.predict(features_selected)[0]
                # Note: SVM might not have predict_proba, handle gracefully
                try:
                    probability = model.predict_proba(features_selected)[0]
                    risk_prob = probability[1] * 100
                except:
                    # For SVM without probability, use decision function
                    decision = model.decision_function(features_selected)[0]
                    # Convert decision function to pseudo-probability
                    risk_prob = max(0, min(100, (decision + 1) * 50))
            else:
                # Fallback to original model prediction
                prediction = model.predict(features)[0]
                probability = model.predict_proba(features)[0]
                risk_prob = probability[1] * 100

            # Display prediction
            if prediction == 1:
                st.markdown(f"""
                <div class="prediction-box high-risk">
                    <h3>⚠️ HIGH RISK</h3>
                    <p><strong>Risk Score: {risk_prob:.1f}%</strong></p>
                    <p>This patient shows indicators of potential heart disease. 
                    Please consult with a cardiologist for further evaluation.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="prediction-box low-risk">
                    <h3>✅ LOW RISK</h3>
                    <p><strong>Risk Score: {risk_prob:.1f}%</strong></p>
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
    st.subheader("🎯 Model Information")

    if hasattr(model, 'feature_importances_') and feature_selector is None:
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
    elif feature_selector is not None:
        st.info(f"""
        **🎯 Optimized Model Active!**
        
        This model uses advanced feature engineering with {model_info.get('features_used', 15)} 
        selected features out of {model_info.get('total_features', 24)} total engineered features.
        
        **Advanced Features Include:**
        - 🔢 Polynomial features (age², cholesterol², etc.)
        - 🔗 Interaction terms (age×heart_rate, bp×cholesterol)
        - 📊 Ratio features (heart_rate/age, cholesterol/bp)
        - 🎯 Statistical feature selection for optimal performance
        """)

    # About section
    with st.expander("ℹ️ About This App"):
        st.markdown(f"""
        This Heart Disease Risk Predictor uses an **advanced {model_info['model_type']}** 
        trained on clinical data with sophisticated feature engineering.

        **Model Performance:**
        - 🎯 Accuracy: {model_info['accuracy']}
        - 🔧 Advanced feature engineering with {model_info.get('total_features', 'multiple')} features
        - ⚡ Hyperparameter optimization and feature selection
        - 📊 Cross-validated for reliability

        **Key Improvements:**
        - Advanced polynomial and interaction features
        - Intelligent statistical feature selection
        - Optimized hyperparameters for maximum accuracy
        - Robust cross-validation testing

        **Important Note:**
        This tool is for educational purposes only and should not replace professional medical advice.
        Always consult with healthcare professionals for medical decisions.
        """)

if __name__ == "__main__":
    main()
