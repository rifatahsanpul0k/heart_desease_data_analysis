# Heart Disease Prediction App

A machine learning web application that predicts heart disease risk using XGBoost.

## Features
- **85.25% Accuracy** XGBoost model optimized with Optuna
- Interactive web interface built with Streamlit
- Real-time risk assessment with probability scoring
- Feature importance visualization
- Professional medical-grade UI

## Quick Start

### Local Deployment
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run heart_disease_app.py
```

### Cloud Deployment (Streamlit Cloud)
1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy with one click!

## Model Information
- **Model Type:** XGBoost Classifier
- **Accuracy:** 85.25%
- **Optimization:** Optuna (50 trials)
- **Features:** 13 clinical features
- **Training Date:** 2025-08-30

## Input Features
1. **Age** - Patient age in years
2. **Sex** - Male (1) or Female (0)
3. **Chest Pain Type** - 4 categories (0-3)
4. **Resting Blood Pressure** - In mmHg
5. **Cholesterol** - In mg/dl
6. **Fasting Blood Sugar** - >120 mg/dl (1) or ≤120 mg/dl (0)
7. **Resting ECG** - 3 categories (0-2)
8. **Maximum Heart Rate** - During exercise
9. **Exercise Induced Angina** - Yes (1) or No (0)
10. **ST Depression** - Induced by exercise
11. **ST Slope** - 3 categories (0-2)
12. **Number of Major Vessels** - 0-3
13. **Thalassemia** - 4 categories (0-3)

## Disclaimer
This application is for educational and research purposes only. 
It should not be used as a substitute for professional medical advice, 
diagnosis, or treatment.

## License
MIT License - Feel free to use and modify for educational purposes.
