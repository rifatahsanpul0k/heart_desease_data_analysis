#!/usr/bin/env python3
"""
High Risk Heart Disease Example
This script demonstrates a patient profile with high risk factors
"""

import pandas as pd
import joblib
import numpy as np

def load_model():
    """Load the trained model and feature names"""
    try:
        model = joblib.load('optimized_xgb_model.joblib')
        with open('feature_names.pkl', 'rb') as f:
            import pickle
            feature_names = pickle.load(f)
        return model, feature_names
    except FileNotFoundError:
        print("Model files not found. Make sure you're in the correct directory.")
        return None, None

def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, 
                         thalach, exang, oldpeak, slope, ca, thal):
    """Predict heart disease probability"""
    model, feature_names = load_model()
    if model is None:
        return None, None
    
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, 
                           thalach, exang, oldpeak, slope, ca, thal]])
    input_df = pd.DataFrame(input_data, columns=feature_names)
    
    probability = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]
    
    return probability, prediction

def high_risk_example():
    """Show a high-risk patient example"""
    
    print("🚨 HIGH RISK HEART DISEASE EXAMPLE")
    print("=" * 50)
    
    # High-risk patient profile
    print("\n👨‍⚕️ Patient Profile:")
    print("-" * 30)
    age = 67          # Older age (high risk)
    sex = 1           # Male (higher risk than female)
    cp = 3            # Asymptomatic chest pain (highest risk type)
    trestbps = 180    # High blood pressure
    chol = 350        # Very high cholesterol
    fbs = 1           # High fasting blood sugar (diabetic)
    restecg = 2       # Abnormal ECG
    thalach = 110     # Low maximum heart rate (concerning)
    exang = 1         # Exercise-induced chest pain
    oldpeak = 3.5     # Significant ST depression
    slope = 2         # Downsloping ST segment (worst type)
    ca = 3            # 3 major vessels blocked (maximum)
    thal = 2          # Reversible defect (concerning)
    
    print(f"🧑 Age: {age} years old")
    print(f"👨 Sex: {'Male' if sex == 1 else 'Female'}")
    print(f"💔 Chest Pain: Type {cp} (Asymptomatic - most concerning)")
    print(f"🩸 Blood Pressure: {trestbps} mmHg (HIGH)")
    print(f"🧪 Cholesterol: {chol} mg/dl (VERY HIGH)")
    print(f"🍬 Fasting Blood Sugar: {'HIGH (Diabetic)' if fbs == 1 else 'Normal'}")
    print(f"📊 ECG: Abnormal (showing hypertrophy)")
    print(f"❤️ Max Heart Rate: {thalach} bpm (LOW for age)")
    print(f"🏃 Exercise Angina: {'YES' if exang == 1 else 'NO'}")
    print(f"📈 ST Depression: {oldpeak} (SIGNIFICANT)")
    print(f"📉 ST Slope: Downsloping (WORST type)")
    print(f"🚫 Blocked Vessels: {ca}/4 major vessels (SEVERE)")
    print(f"🔬 Thalassemia: Reversible defect")
    
    # Get prediction
    probability, prediction = predict_heart_disease(
        age, sex, cp, trestbps, chol, fbs, restecg, 
        thalach, exang, oldpeak, slope, ca, thal
    )
    
    if probability is not None:
        print(f"\n🎯 MODEL PREDICTION:")
        print("-" * 30)
        print(f"💥 Heart Disease Probability: {probability:.1%}")
        print(f"🚨 Risk Level: {'🟢 LOW' if probability < 0.3 else '🟡 MEDIUM' if probability < 0.7 else '🔴 HIGH'}")
        print(f"⚕️ Clinical Prediction: {'❤️ Healthy' if prediction == 0 else '⚠️ Heart Disease'}")
        
        print(f"\n📋 RISK FACTOR ANALYSIS:")
        print("-" * 30)
        risk_factors = []
        if age > 55: risk_factors.append(f"Advanced age ({age})")
        if sex == 1: risk_factors.append("Male gender")
        if cp == 3: risk_factors.append("Asymptomatic chest pain")
        if trestbps > 140: risk_factors.append(f"High blood pressure ({trestbps})")
        if chol > 240: risk_factors.append(f"High cholesterol ({chol})")
        if fbs == 1: risk_factors.append("Diabetes")
        if thalach < 120: risk_factors.append(f"Low max heart rate ({thalach})")
        if exang == 1: risk_factors.append("Exercise-induced angina")
        if oldpeak > 2: risk_factors.append(f"Significant ST depression ({oldpeak})")
        if ca > 0: risk_factors.append(f"{ca} blocked major vessels")
        
        for i, factor in enumerate(risk_factors, 1):
            print(f"{i:2d}. 🔴 {factor}")
        
        print(f"\n💡 TOTAL RISK FACTORS: {len(risk_factors)}/10")
        
        if probability > 0.8:
            print(f"\n🚨 CRITICAL RISK ASSESSMENT:")
            print("   This patient has EXTREMELY HIGH risk factors")
            print("   Immediate medical evaluation recommended")
            print("   Multiple cardiovascular interventions likely needed")
    
    print("\n" + "=" * 50)
    print("⚠️  This is for educational purposes only")
    print("⚕️  Always consult healthcare professionals")

if __name__ == "__main__":
    high_risk_example()
