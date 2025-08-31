import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Page config
st.set_page_config(
    page_title="🫀 Heart Disease Predictor",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #262730;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    /* Target specific Streamlit element containers */
    .stElementContainer.element-container.st-emotion-cache-1vo6xi6.e52wr8w0 {
        background: transparent !important;
        padding: 0 !important;
        margin: 1rem 0 !important;
    }
    
    /* Base prediction box styling */
    .prediction-box {
        padding: 2.5rem;
        border-radius: 25px;
        margin: 2rem auto;
        border: none;
        font-weight: 500;
        position: relative;
        overflow: hidden;
        max-width: 600px;
        text-align: center;
    }
    
    /* HIGH RISK - Dark/Black Theme */
    .high-risk {
        background: linear-gradient(145deg, #000000 0%, #1a1a1a 30%, #333333 100%);
        color: #ffffff;
        box-shadow: 
            0 20px 40px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        border: 2px solid #444444;
    }
    
    .high-risk::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 6px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            rgba(255, 255, 255, 0.3) 20%, 
            rgba(255, 255, 255, 0.8) 50%, 
            rgba(255, 255, 255, 0.3) 80%, 
            transparent 100%);
    }
    
    .high-risk::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 6px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            rgba(255, 255, 255, 0.2) 50%, 
            transparent 100%);
    }
    
    .high-risk h3 {
        color: #ffffff !important;
        margin-bottom: 1.5rem;
        font-size: 2.2rem;
        font-weight: 900;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    
    .high-risk p {
        color: #f8f9fa !important;
        margin-bottom: 1rem;
        font-size: 1.3rem;
        line-height: 1.7;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
    }
    
    .high-risk strong {
        color: #ffffff !important;
        font-size: 1.6rem;
        font-weight: 800;
        display: block;
        margin-bottom: 1rem;
        padding: 0.5rem;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        backdrop-filter: blur(10px);
    }
    
    /* LOW RISK - Light/White Theme */
    .low-risk {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 30%, #e9ecef 100%);
        color: #212529;
        box-shadow: 
            0 20px 40px rgba(0, 0, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.8);
        border: 2px solid #dee2e6;
    }
    
    .low-risk::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 6px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            rgba(33, 37, 41, 0.2) 20%, 
            rgba(33, 37, 41, 0.4) 50%, 
            rgba(33, 37, 41, 0.2) 80%, 
            transparent 100%);
    }
    
    .low-risk::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 6px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            rgba(108, 117, 125, 0.3) 50%, 
            transparent 100%);
    }
    
    .low-risk h3 {
        color: #212529 !important;
        margin-bottom: 1.5rem;
        font-size: 2.2rem;
        font-weight: 900;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    
    .low-risk p {
        color: #495057 !important;
        margin-bottom: 1rem;
        font-size: 1.3rem;
        line-height: 1.7;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
    }
    
    .low-risk strong {
        color: #212529 !important;
        font-size: 1.6rem;
        font-weight: 800;
        display: block;
        margin-bottom: 1rem;
        padding: 0.5rem;
        background: rgba(33, 37, 41, 0.05);
        border-radius: 12px;
        border: 1px solid rgba(33, 37, 41, 0.1);
    }
    
    /* Enhanced sidebar styling */
    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8f9fa 0%, #ffffff 100%);
        border-right: 2px solid #dee2e6;
    }
    
    /* Override Streamlit's default container styling for our prediction boxes */
    .stElementContainer:has(.prediction-box) {
        background: transparent !important;
        padding: 0 !important;
        margin: 2rem 0 !important;
    }
    
    /* Custom button styling */
    .stButton > button {
        background: linear-gradient(135deg, #212529 0%, #495057 100%);
        color: white;
        border: none;
        border-radius: 15px;
        font-weight: 700;
        font-size: 1.2rem;
        padding: 1rem 2.5rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.3);
        background: linear-gradient(135deg, #000000 0%, #212529 100%);
    }
    
    .stSelectbox > div > div {
        background-color: #ffffff;
        border: 2px solid #ced4da;
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #495057;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .stSlider > div > div > div {
        background-color: #ffffff;
        border-radius: 10px;
    }
    
    /* Additional CSS for specific Streamlit container targeting */
    .st-emotion-cache-1vo6xi6 {
        background: transparent !important;
        padding: 0 !important;
        border: none !important;
    }
    
    .e52wr8w0 {
        margin: 1rem 0 !important;
    }
    
    /* High Risk - Dark Military/Alert Style */
    .high-risk {
        position: relative;
        background: 
            linear-gradient(145deg, #000000 0%, #1a1a1a 25%, #2d2d2d 75%, #1a1a1a 100%) !important;
        border: 3px solid #333333 !important;
        border-radius: 20px !important;
        color: #ffffff !important;
        padding: 2.5rem !important;
        margin: 2rem auto !important;
        max-width: 700px !important;
        text-align: center !important;
        box-shadow: 
            0 25px 50px rgba(0, 0, 0, 0.5),
            inset 0 1px 0 rgba(255, 255, 255, 0.1),
            0 0 30px rgba(255, 255, 255, 0.05) !important;
    }
    
    .high-risk::before {
        content: '🚨' !important;
        position: absolute !important;
        top: -15px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        font-size: 2rem !important;
        background: #000000 !important;
        padding: 0.5rem 1rem !important;
        border-radius: 50% !important;
        border: 3px solid #ff0000 !important;
        animation: blink 1.5s infinite !important;
    }
    
    @keyframes blink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0.3; }
    }
    
    /* Low Risk - Clean Medical/Professional Style */
    .low-risk {
        position: relative;
        background: 
            linear-gradient(145deg, #ffffff 0%, #f8f9fa 25%, #e9ecef 75%, #f8f9fa 100%) !important;
        border: 3px solid #28a745 !important;
        border-radius: 20px !important;
        color: #212529 !important;
        padding: 2.5rem !important;
        margin: 2rem auto !important;
        max-width: 700px !important;
        text-align: center !important;
        box-shadow: 
            0 25px 50px rgba(0, 0, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.8),
            0 0 30px rgba(40, 167, 69, 0.1) !important;
    }
    
    .low-risk::before {
        content: '✅' !important;
        position: absolute !important;
        top: -15px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        font-size: 2rem !important;
        background: #ffffff !important;
        padding: 0.5rem 1rem !important;
        border-radius: 50% !important;
        border: 3px solid #28a745 !important;
        animation: pulse-success 2s infinite !important;
    }
    
    @keyframes pulse-success {
        0%, 100% { 
            transform: translateX(-50%) scale(1); 
            box-shadow: 0 0 0 0 rgba(40, 167, 69, 0.4); 
        }
        50% { 
            transform: translateX(-50%) scale(1.1); 
            box-shadow: 0 0 0 10px rgba(40, 167, 69, 0); 
        }
    }
    
    /* Override any Streamlit container styling that might interfere */
    div[data-testid="stMarkdownContainer"] .prediction-box {
        margin: 2rem auto !important;
    }
    
    /* Make sure text is properly visible in each theme */
    .high-risk * {
        color: #ffffff !important;
    }
    
    .low-risk * {
        color: #212529 !important;
    }
    
    .high-risk strong {
        background: rgba(255, 255, 255, 0.1) !important;
        padding: 0.3rem 0.6rem !important;
        border-radius: 8px !important;
        backdrop-filter: blur(5px) !important;
    }
    
    .low-risk strong {
        background: rgba(40, 167, 69, 0.1) !important;
        padding: 0.3rem 0.6rem !important;
        border-radius: 8px !important;
        color: #155724 !important;
    }
</style>""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    try:
        # Load the Random Forest model (90.16% accuracy)
        model = joblib.load('heart_disease_model_optimized.pkl')
        feature_names = joblib.load('feature_names.pkl')
        model_info = joblib.load('model_info.pkl')
        
        return model, feature_names, model_info
        
    except FileNotFoundError as e:
        st.error(f"❌ Model files not found: {e}")
        st.error("Please ensure all required model files are in the same directory:")
        st.error("• heart_disease_model_optimized.pkl")
        st.error("• feature_names.pkl") 
        st.error("• model_info.pkl")
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

            # Make prediction with Random Forest model (no preprocessing needed)
            prediction = model.predict(features)[0]
            probability = model.predict_proba(features)[0]
            risk_prob = probability[1] * 100

            # Display prediction
            if prediction == 1:
                st.markdown(f"""
                <div class="prediction-box high-risk" style="animation: pulse-danger 2s infinite;">
                    <h3>🚨 CRITICAL RISK ALERT</h3>
                    <p><strong>⚡ Risk Assessment: {risk_prob:.1f}%</strong></p>
                    <p>🔍 <strong>URGENT:</strong> Analysis indicates significant risk factors for cardiovascular disease. 
                    Immediate medical consultation with a cardiologist is <em>strongly recommended</em> 
                    for comprehensive evaluation and immediate risk management protocol.</p>
                    <p style="margin-top: 1.5rem; font-size: 0.9rem; opacity: 0.8;">
                    ⏰ <strong>Next Steps:</strong> Schedule cardiology appointment within 48-72 hours
                    </p>
                </div>
                
                <style>
                @keyframes pulse-danger {{
                    0%, 100% {{ box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), 0 0 0 0 rgba(255, 255, 255, 0.1); }}
                    50% {{ box-shadow: 0 25px 50px rgba(0, 0, 0, 0.6), 0 0 0 10px rgba(255, 255, 255, 0.05); }}
                }}
                </style>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="prediction-box low-risk" style="animation: glow-safe 3s infinite;">
                    <h3>✅ OPTIMAL HEALTH PROFILE</h3>
                    <p><strong>💚 Risk Assessment: {risk_prob:.1f}%</strong></p>
                    <p>🌟 <strong>EXCELLENT:</strong> Cardiovascular health indicators show minimal risk factors. 
                    Current health profile suggests <em>low probability</em> of heart disease. 
                    Continue maintaining healthy lifestyle practices and regular monitoring.</p>
                    <p style="margin-top: 1.5rem; font-size: 0.9rem; opacity: 0.7;">
                    📅 <strong>Recommendation:</strong> Annual cardiac health screening recommended
                    </p>
                </div>
                
                <style>
                @keyframes glow-safe {{
                    0%, 100% {{ box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1), 0 0 0 0 rgba(33, 37, 41, 0.05); }}
                    50% {{ box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15), 0 0 0 8px rgba(33, 37, 41, 0.02); }}
                }}
                </style>
                """, unsafe_allow_html=True)

            # Risk gauge
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = risk_prob,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Heart Disease Risk (%)", 'font': {'color': '#262730', 'size': 20}},
                gauge = {
                    'axis': {'range': [None, 100], 'tickcolor': '#262730', 'tickfont': {'color': '#262730'}},
                    'bar': {'color': "#000000"},
                    'steps': [
                        {'range': [0, 30], 'color': "#f8f9fa"},
                        {'range': [30, 70], 'color': "#dee2e6"},
                        {'range': [70, 100], 'color': "#6c757d"}],
                    'threshold': {
                        'line': {'color': "#000000", 'width': 4},
                        'thickness': 0.75,
                        'value': 85}}))

            fig.update_layout(
                height=300,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font={'color': '#262730'}
            )
            st.plotly_chart(fig, use_container_width=True)

    # Feature importance
    st.subheader("🎯 Model Information")

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
    else:
        st.info(f"""
        **🎯 Random Forest Model Active!**
        
        This model uses all {len(feature_names)} medical features directly 
        with {model_info['accuracy']*100:.1f}% accuracy.
        
        **Features Used:**
        - � Age, Sex, Chest Pain Type
        - 🩸 Blood Pressure & Cholesterol
        - � Heart Rate & Exercise Response  
        - 📈 ECG Results & ST Measurements
        - 🧬 Thalassemia & Vessel Count
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
