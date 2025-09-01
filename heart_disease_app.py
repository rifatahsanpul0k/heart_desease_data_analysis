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
    page_title="Heart Disease Risk Predictor",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.who.int/health-topics/cardiovascular-diseases',
        'Report a bug': None,
        'About': "AI-powered heart disease risk prediction tool for educational purposes."
    }
)

# Static Dark Theme CSS
st.markdown("""
<style>
    /* Global Theme Variables - Dark Theme */
    :root {
        --bg-primary: #0D0D0D;
        --bg-secondary: #1A1A1A;
        --text-primary: #FFFFFF;
        --text-secondary: #B3B3B3;
        --border-color: #333333;
        --button-bg: #FFFFFF;
        --button-text: #0D0D0D;
        --button-hover-bg: #0D0D0D;
        --button-hover-text: #FFFFFF;
        --shadow-color: rgba(255, 255, 255, 0.05);
        --slider-track: #333333;
        --slider-thumb: #FFFFFF;
        --accent-color: #FFFFFF;
        --success-color: #28A745;
        --warning-color: #FFC107;
        --danger-color: #DC3545;
        --neutral-bg: #2A2A2A;
    }
    
    /* Global Theme */
    .main .block-container {
        background-color: var(--bg-primary) !important;
        color: var(--text-primary) !important;
        padding: 2rem 1rem !important;
        max-width: 1200px !important;
    }
    
    /* Hide Streamlit Default Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main Background */
    .stApp {
        background-color: var(--bg-primary) !important;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background-color: var(--bg-secondary) !important;
    }
    
    div[data-testid="stSidebar"] {
        background-color: var(--bg-secondary) !important;
        border-right: 1px solid var(--border-color) !important;
    }
    
    div[data-testid="stSidebar"] .stMarkdown {
        color: var(--text-primary) !important;
    }
    
    /* Header Styling */
    .header-container {
        text-align: center;
        margin-bottom: 3rem;
        padding: 2rem 0;
    }
    
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: var(--text-primary);
        margin: 0;
        letter-spacing: -0.5px;
    }
    
    .subtitle {
        font-size: 1.1rem;
        color: var(--text-secondary);
        margin-top: 0.5rem;
        font-weight: 400;
    }
    
    /* Card Styling */
    .dark-card {
        background-color: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 30px;
        box-shadow: 0 4px 20px var(--shadow-color);
    }
    
    .section-header {
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 1rem;
    }
    
    /* Custom Input Styling */
    .stSelectbox > div > div {
        background-color: var(--bg-secondary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
    }
    
    .stSelectbox > div > div:hover {
        border-color: var(--accent-color) !important;
        box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.1) !important;
    }
    
    .stSelectbox > div > div > div {
        color: var(--text-primary) !important;
    }
    
    .stSlider > div > div > div > div {
        background-color: var(--slider-track) !important;
    }
    
    .stSlider > div > div > div > div > div {
        background-color: var(--slider-thumb) !important;
    }
    
    .stSlider:hover > div > div > div > div > div {
        box-shadow: 0 0 0 4px rgba(255, 255, 255, 0.2) !important;
    }
    
    /* Input Labels */
    .stSelectbox > label,
    .stSlider > label {
        color: var(--text-secondary) !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
    }
    
    /* Primary Button */
    .predict-button {
        display: flex;
        justify-content: center;
        margin: 2rem 0;
    }
    
    .stButton > button {
        background-color: var(--button-bg) !important;
        color: var(--button-text) !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        padding: 0.75rem 3rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px var(--shadow-color) !important;
    }
    
    .stButton > button:hover {
        background-color: var(--button-hover-bg) !important;
        color: var(--button-hover-text) !important;
        border: none !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 25px var(--shadow-color) !important;
    }
    
    /* Prediction Result Cards */
    .prediction-result {
        background-color: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 30px;
        text-align: center;
        margin: 30px 0;
        box-shadow: 0 4px 20px var(--shadow-color);
    }
    
    .risk-percentage {
        font-size: 3rem;
        font-weight: 800;
        color: var(--text-primary);
        margin: 1rem 0;
    }
    
    .risk-message {
        font-size: 1.1rem;
        color: var(--text-secondary);
        line-height: 1.6;
    }
    
    .risk-low {
        border-left: 4px solid var(--success-color) !important;
        background: linear-gradient(135deg, var(--bg-secondary) 0%, rgba(40, 167, 69, 0.05) 100%);
    }
    
    .risk-high {
        border-left: 4px solid var(--danger-color) !important;
        background: linear-gradient(135deg, var(--bg-secondary) 0%, rgba(220, 53, 69, 0.05) 100%);
    }
    
    .risk-medium {
        border-left: 4px solid var(--warning-color) !important;
        background: linear-gradient(135deg, var(--bg-secondary) 0%, rgba(255, 193, 7, 0.05) 100%);
    }
    
    /* Patient Summary Table */
    .stDataFrame {
        background-color: var(--bg-secondary) !important;
    }
    
    .stDataFrame > div {
        background-color: var(--bg-secondary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
    }
    
    /* Metrics Styling */
    div[data-testid="metric-container"] {
        background-color: var(--bg-secondary);
        border: 1px solid var(--border-color);
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px var(--shadow-color);
    }
    
    div[data-testid="metric-container"] > div {
        color: var(--text-primary) !important;
    }
    
    /* Expandable Sections */
    .streamlit-expanderHeader {
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
    }
    
    .streamlit-expanderContent {
        background-color: var(--bg-secondary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 0 0 8px 8px !important;
        color: var(--text-primary) !important;
    }
    
    /* Feature Description Cards */
    .feature-card {
        background-color: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
    }
    
    .feature-title {
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 8px;
    }
    
    .feature-description {
        color: var(--text-secondary);
        font-size: 0.9rem;
        line-height: 1.5;
    }
    
    /* Toggle Button Styling */
    .stCheckbox > label {
        color: var(--text-primary) !important;
    }
    
    /* Additional Text Visibility Fixes */
    .stSelectbox > label > div {
        color: var(--text-secondary) !important;
    }
    
    .stSelectbox [data-baseweb="select"] > div {
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
    }
    
    .stSelectbox [data-baseweb="select"] > div > div {
        color: var(--text-primary) !important;
    }
    
    /* Number Input Styling */
    .stNumberInput > div > div > input {
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-color) !important;
    }
    
    /* Text Input Styling */
    .stTextInput > div > div > input {
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-color) !important;
    }
    
    /* Slider Value Display */
    .stSlider > div > div > div > div > div > div {
        color: var(--text-primary) !important;
    }
    
    /* All text elements */
    div[data-testid="stMarkdownContainer"] p {
        color: var(--text-primary) !important;
    }
    
    /* Sidebar text */
    .css-1d391kg .stMarkdown {
        color: var(--text-primary) !important;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        
        .risk-percentage {
            font-size: 2.5rem;
        }
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-primary);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--border-color);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--text-secondary);
    }
</style>""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    import os
    import joblib
    
    # Multiple possible paths for model files
    possible_dirs = [
        os.path.dirname(os.path.abspath(__file__)),  # Same directory as script
        os.getcwd(),  # Current working directory
        '/opt/render/project/src',  # Render deployment path
        '.',  # Current directory
    ]
    
    model_files = {
        'model': 'heart_disease_model_optimized.pkl',
        'features': 'feature_names.pkl',
        'info': 'model_info.pkl'
    }
    
    # Try each directory until we find the files
    for directory in possible_dirs:
        try:
            file_paths = {}
            all_exist = True
            
            # Check if all files exist in this directory
            for key, filename in model_files.items():
                file_path = os.path.join(directory, filename)
                if os.path.exists(file_path):
                    file_paths[key] = file_path
                else:
                    all_exist = False
                    break
            
            if all_exist:
                # Load all model files
                model = joblib.load(file_paths['model'])
                feature_names = joblib.load(file_paths['features'])
                model_info = joblib.load(file_paths['info'])
                
                st.success(f"✅ Model loaded successfully from: {directory}")
                return model, feature_names, model_info
                
        except Exception as e:
            continue  # Try next directory
    
    # If we get here, no directory worked
    st.error("❌ Model files not found in any expected location!")
    st.error("Searched directories:")
    for i, directory in enumerate(possible_dirs, 1):
        st.error(f"{i}. {directory}")
    st.error("Required files:")
    for filename in model_files.values():
        st.error(f"• {filename}")
    
    # Show current directory contents for debugging
    try:
        current_files = os.listdir(os.getcwd())
        st.error(f"Files in current directory: {current_files}")
    except:
        pass
        
    return None, None, None

def main():
    # Header Section
    st.markdown("""
    <div class="header-container">
        <h1 class="main-title">Heart Disease Risk Predictor</h1>
        <p class="subtitle">AI-powered prediction based on patient health data</p>
    </div>
    """, unsafe_allow_html=True)

    # Load model
    model, feature_names, model_info = load_model()
    if model is None:
        st.error("⚠️ Unable to load the prediction model. Please check the model files.")
        st.stop()

    # Input Section Card
    st.markdown('<div class="dark-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Patient Information</h2>', unsafe_allow_html=True)
    
    # Create two columns for input grid
    col1, col2 = st.columns(2)
    
    with col1:
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
                         help="Type of chest pain experienced")
        
        trestbps = st.slider("Resting Blood Pressure (mmHg)", 80, 200, 120,
                            help="Resting blood pressure in mm Hg")
        
        chol = st.slider("Serum Cholesterol (mg/dl)", 100, 400, 200,
                        help="Serum cholesterol in mg/dl")
        
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1], 
                          format_func=lambda x: "No" if x == 0 else "Yes",
                          help="1 = true (>120 mg/dl); 0 = false (≤120 mg/dl)")
        
        restecg = st.selectbox("Resting ECG Results", [0, 1, 2],
                              format_func=lambda x: {
                                  0: "Normal", 
                                  1: "ST-T Wave abnormality", 
                                  2: "Left ventricular hypertrophy"
                              }[x],
                              help="Resting electrocardiographic results")
    
    with col2:
        thalach = st.slider("Maximum Heart Rate Achieved", 60, 220, 150,
                           help="Maximum heart rate achieved during exercise")
        
        exang = st.selectbox("Exercise Induced Angina", [0, 1],
                            format_func=lambda x: "No" if x == 0 else "Yes",
                            help="1 = yes; 0 = no")
        
        oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0, 0.1,
                           help="ST depression induced by exercise relative to rest")
        
        slope = st.selectbox("Peak Exercise ST Segment Slope", [0, 1, 2],
                            format_func=lambda x: {
                                0: "Upsloping", 
                                1: "Flat", 
                                2: "Downsloping"
                            }[x],
                            help="The slope of the peak exercise ST segment")
        
        ca = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3],
                         help="Number of major vessels colored by fluoroscopy")
        
        thal = st.selectbox("Thalium Stress Result", [1, 3, 6, 7],
                           format_func=lambda x: {
                               1: "Normal", 
                               3: "Fixed defect", 
                               6: "Fixed defect", 
                               7: "Reversible defect"
                           }[x],
                           help="Thalium stress test result")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Patient Profile Summary (Collapsible)
    with st.expander("📊 Patient Profile Summary", expanded=False):
        summary_data = {
            "Attribute": ["Age", "Sex", "Chest Pain Type", "Resting BP", "Cholesterol", "Max Heart Rate"],
            "Value": [
                f"{age} years", 
                "Male" if sex == 1 else "Female",
                {0: "Typical angina", 1: "Atypical angina", 2: "Non-anginal pain", 3: "Asymptomatic"}[cp],
                f"{trestbps} mmHg", 
                f"{chol} mg/dl", 
                f"{thalach} bpm"
            ],
            "Status": [
                "Normal" if 20 <= age <= 65 else "Attention needed",
                "N/A",
                "N/A",
                "Normal" if 90 <= trestbps <= 140 else "Abnormal",
                "Normal" if chol <= 200 else "High",
                "Normal" if thalach >= 150 else "Low"
            ]
        }
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df, use_container_width=True)

    # Prediction Button
    st.markdown('<div class="predict-button">', unsafe_allow_html=True)
    if st.button("🔍 Predict Risk", type="primary"):
        # Create feature array
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])

        # Make prediction
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0]
        risk_prob = probability[1] * 100

        # Display prediction result
        risk_percentage_text = f"Risk: {risk_prob:.1f}%"
        
        # Determine risk level and styling
        if risk_prob < 30:
            risk_level = "low"
            risk_message_text = '✅ Low risk detected – maintain healthy lifestyle practices'
        elif risk_prob < 70:
            risk_level = "medium"
            risk_message_text = '⚠️ Medium risk detected – consider lifestyle changes and medical consultation'
        else:
            risk_level = "high"
            risk_message_text = '🚨 High risk detected – seek immediate medical consultation'
        
        st.markdown(f"""
        <div class="prediction-result risk-{risk_level}">
            <div class="risk-percentage">{risk_percentage_text}</div>
            <div class="risk-message">{risk_message_text}</div>
        </div>
        """, unsafe_allow_html=True)

        # Risk Gauge Chart
        chart_colors = {
            'title_color': '#FFFFFF',
            'axis_color': '#B3B3B3',
            'bar_color': '#FFFFFF',
            'paper_bg': '#1A1A1A',
            'plot_bg': '#1A1A1A',
            'font_color': '#FFFFFF',
            'steps': [
                {'range': [0, 30], 'color': '#333333'},
                {'range': [30, 70], 'color': '#1A1A1A'},
                {'range': [70, 100], 'color': '#0D0D0D'}
            ]
        }
        
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_prob,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Heart Disease Risk (%)", 'font': {'color': chart_colors['title_color'], 'size': 18}},
            gauge={
                'axis': {'range': [None, 100], 'tickcolor': chart_colors['axis_color'], 'tickfont': {'color': chart_colors['axis_color']}},
                'bar': {'color': chart_colors['bar_color']},
                'steps': chart_colors['steps'],
                'threshold': {
                    'line': {'color': chart_colors['bar_color'], 'width': 4},
                    'thickness': 0.75,
                    'value': 50
                }
            }
        ))

        fig.update_layout(
            height=300,
            paper_bgcolor=chart_colors['paper_bg'],
            plot_bgcolor=chart_colors['plot_bg'],
            font={'color': chart_colors['font_color']}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Model Information Card
    st.markdown('<div class="dark-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">🤖 Model Information</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Model Type", model_info['model_type'])
    with col2:
        st.metric("Accuracy", f"{model_info['accuracy']}")
    with col3:
        st.metric("Total Features", f"{model_info.get('total_features', len(feature_names))}")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Feature Importance Chart
    if hasattr(model, 'feature_importances_'):
        st.markdown('<div class="dark-card">', unsafe_allow_html=True)
        st.markdown('<h2 class="section-header">📊 Feature Importance</h2>', unsafe_allow_html=True)
        
        feature_importance_df = pd.DataFrame({
            'Feature': ['Age', 'Sex', 'Chest Pain', 'Resting BP', 'Cholesterol',
                       'Fasting Blood Sugar', 'Resting ECG', 'Max Heart Rate',
                       'Exercise Angina', 'ST Depression', 'ST Slope',
                       'Major Vessels', 'Thalassemia'],
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=True)

        fig = px.bar(
            feature_importance_df, 
            x='Importance', 
            y='Feature', 
            orientation='h',
            title="Feature Importance in Heart Disease Prediction"
        )
        
        # Apply theme colors to chart
        chart_colors = {
            'paper_bg': '#1A1A1A',
            'plot_bg': '#1A1A1A',
            'font_color': '#FFFFFF',
            'grid_color': '#333333',
            'axis_color': '#B3B3B3',
            'bar_color': '#FFFFFF'
        }
        
        fig.update_layout(
            paper_bgcolor=chart_colors['paper_bg'],
            plot_bgcolor=chart_colors['plot_bg'],
            font={'color': chart_colors['font_color']},
            title={'font': {'color': chart_colors['font_color']}},
            xaxis={'gridcolor': chart_colors['grid_color'], 'color': chart_colors['axis_color']},
            yaxis={'gridcolor': chart_colors['grid_color'], 'color': chart_colors['axis_color']}
        )
        
        fig.update_traces(marker_color=chart_colors['bar_color'])
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Feature Descriptions (Accordion)
    with st.expander("📖 Feature Descriptions", expanded=False):
        feature_descriptions = {
            "Age": "Patient age in years. Higher age generally increases cardiovascular risk.",
            "Sex": "Biological sex (Male/Female). Males typically have higher risk at younger ages.",
            "Chest Pain Type": "Type of chest pain: Typical angina, Atypical angina, Non-anginal pain, or Asymptomatic.",
            "Resting Blood Pressure": "Blood pressure when at rest, measured in mmHg. Normal range: 90-140 mmHg.",
            "Cholesterol": "Serum cholesterol level in mg/dl. Normal: <200 mg/dl, High: >240 mg/dl.",
            "Fasting Blood Sugar": "Blood sugar level after fasting. >120 mg/dl indicates potential diabetes.",
            "Resting ECG": "Electrocardiogram results at rest showing heart's electrical activity.",
            "Maximum Heart Rate": "Highest heart rate achieved during exercise testing.",
            "Exercise Induced Angina": "Whether chest pain occurs during physical exercise.",
            "ST Depression": "Depression in ST segment during exercise, indicating potential ischemia.",
            "ST Slope": "Slope of peak exercise ST segment (Upsloping/Flat/Downsloping).",
            "Major Vessels": "Number of major blood vessels (0-3) visible in fluoroscopy.",
            "Thalassemia": "Blood disorder affecting hemoglobin production and heart function."
        }
        
        for feature, description in feature_descriptions.items():
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-title">{feature}</div>
                <div class="feature-description">{description}</div>
            </div>
            """, unsafe_allow_html=True)

    # About Section
    with st.expander("ℹ️ About This Application", expanded=False):
        model_type = model_info['model_type']
        accuracy = model_info['accuracy']
        total_features = model_info.get('total_features', len(feature_names))
        
        about_content = f"""
        **Heart Disease Risk Predictor** uses an advanced **{model_type}** 
        trained on clinical cardiovascular data to assess heart disease risk.

        **Model Performance:**
        - **Accuracy:** {accuracy}
        - **Features:** {total_features} medical parameters
        - **Technology:** Optimized machine learning with cross-validation
        - **Data:** Trained on clinical cardiovascular datasets

        **Important Medical Disclaimer:**
        This tool is designed for educational and informational purposes only. 
        It should **never replace professional medical advice, diagnosis, or treatment**. 
        Always consult qualified healthcare professionals for medical decisions and 
        comprehensive cardiovascular risk assessment.

        **Usage Guidelines:**
        - Enter accurate patient information for reliable predictions
        - Use results as supplementary information only
        - Seek immediate medical attention for concerning symptoms
        - Schedule regular cardiovascular screenings as recommended by healthcare providers
        """
        st.markdown(about_content, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
