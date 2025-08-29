#!/usr/bin/env python3
"""
Multiple High Risk Examples
Testing different combinations to find high-risk predictions
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
        print("Model files not found.")
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

def test_high_risk_scenarios():
    """Test multiple high-risk scenarios"""
    
    print("🔬 TESTING HIGH-RISK SCENARIOS")
    print("=" * 60)
    
    scenarios = [
        {
            "name": "Elderly Male with Multiple Comorbidities",
            "params": [70, 1, 3, 200, 400, 1, 2, 90, 1, 4.0, 2, 3, 2],
            "description": "70-year-old male, very high BP & cholesterol, very low heart rate"
        },
        {
            "name": "Middle-aged with Severe Coronary Disease", 
            "params": [55, 1, 3, 160, 300, 1, 1, 100, 1, 3.0, 2, 3, 2],
            "description": "55-year-old male, 3 blocked vessels, severe symptoms"
        },
        {
            "name": "Young but Critical Case",
            "params": [45, 1, 3, 180, 350, 1, 2, 95, 1, 3.5, 2, 2, 2], 
            "description": "45-year-old with premature severe disease"
        },
        {
            "name": "Classic High-Risk Profile",
            "params": [65, 1, 2, 170, 320, 1, 1, 105, 1, 2.8, 1, 2, 1],
            "description": "Typical high-risk cardiac patient"
        },
        {
            "name": "Extreme Risk Factors",
            "params": [75, 1, 3, 220, 450, 1, 2, 80, 1, 5.0, 2, 3, 2],
            "description": "Maximum risk factors across all parameters"
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n🏥 SCENARIO {i}: {scenario['name']}")
        print("-" * 50)
        print(f"📝 {scenario['description']}")
        
        prob, pred = predict_heart_disease(*scenario['params'])
        
        if prob is not None:
            risk_level = "🔴 HIGH" if prob > 0.7 else "🟡 MEDIUM" if prob > 0.3 else "🟢 LOW"
            print(f"💥 Heart Disease Probability: {prob:.1%}")
            print(f"🚨 Risk Level: {risk_level}")
            print(f"⚕️ Prediction: {'⚠️ Heart Disease' if pred == 1 else '❤️ Healthy'}")
            
            # Show parameters
            params = scenario['params']
            print(f"📊 Parameters: Age={params[0]}, Sex={params[1]}, CP={params[2]}, BP={params[3]}")
            print(f"   Chol={params[4]}, FBS={params[5]}, ECG={params[6]}, HR={params[7]}")
            print(f"   Angina={params[8]}, ST={params[9]}, Slope={params[10]}, Vessels={params[11]}, Thal={params[12]}")
        
        if i < len(scenarios):
            print()
    
    print("\n" + "=" * 60)

def find_highest_risk():
    """Find combinations that give highest risk predictions"""
    
    print("\n🔍 SEARCHING FOR HIGHEST RISK COMBINATIONS...")
    print("=" * 60)
    
    highest_prob = 0
    best_scenario = None
    
    # Test various combinations
    test_cases = [
        # Try different age/sex combinations with worst other factors
        [60, 0, 3, 200, 400, 1, 2, 90, 1, 4.0, 2, 3, 2],  # Female
        [60, 1, 1, 200, 400, 1, 2, 90, 1, 4.0, 2, 3, 2],  # Different CP
        [60, 1, 0, 200, 400, 1, 2, 90, 1, 4.0, 2, 3, 2],  # Different CP
        [40, 1, 3, 200, 400, 1, 2, 90, 1, 4.0, 2, 3, 2],  # Younger
        [80, 1, 3, 200, 400, 1, 2, 90, 1, 4.0, 2, 3, 2],  # Older
        [60, 1, 3, 140, 250, 0, 0, 150, 0, 1.0, 1, 1, 1], # Lower risk factors
        [50, 0, 0, 120, 200, 0, 0, 180, 0, 0.0, 1, 0, 1], # Low risk baseline
    ]
    
    for i, params in enumerate(test_cases):
        prob, pred = predict_heart_disease(*params)
        if prob is not None and prob > highest_prob:
            highest_prob = prob
            best_scenario = params.copy()
        
        risk_level = "🔴 HIGH" if prob > 0.7 else "🟡 MEDIUM" if prob > 0.3 else "🟢 LOW"
        print(f"Test {i+1}: {prob:.1%} - {risk_level}")
    
    if best_scenario:
        print(f"\n🏆 HIGHEST RISK FOUND: {highest_prob:.1%}")
        print(f"📋 Best parameters: {best_scenario}")
        
        # Describe this scenario
        params = best_scenario
        print(f"\n👤 HIGHEST RISK PATIENT PROFILE:")
        print(f"   Age: {params[0]} years")
        print(f"   Sex: {'Male' if params[1] == 1 else 'Female'}")
        print(f"   Chest Pain Type: {params[2]}")
        print(f"   Blood Pressure: {params[3]} mmHg")
        print(f"   Cholesterol: {params[4]} mg/dl")
        print(f"   And other risk factors...")

if __name__ == "__main__":
    test_high_risk_scenarios()
    find_highest_risk()
