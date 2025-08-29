#!/usr/bin/env python3
"""
Heart Disease Prediction Model - Direct Usage Example
This script shows how to use your trained XGBoost model directly for predictions.
"""

import pandas as pd
import joblib
import numpy as np

def load_model():
    """Load the trained model and feature names"""
    try:
        # Load the optimized model
        model = joblib.load('optimized_xgb_model.joblib')
        
        # Load feature names
        with open('feature_names.pkl', 'rb') as f:
            import pickle
            feature_names = pickle.load(f)
        
        return model, feature_names
    except FileNotFoundError:
        print("Model files not found. Make sure you're in the correct directory.")
        return None, None

def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, 
                         thalach, exang, oldpeak, slope, ca, thal):
    """
    Predict heart disease probability for a patient
    
    Parameters:
    - age: Age in years
    - sex: Sex (1 = male, 0 = female)
    - cp: Chest pain type (0-3)
    - trestbps: Resting blood pressure
    - chol: Serum cholesterol in mg/dl
    - fbs: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
    - restecg: Resting electrocardiographic results (0-2)
    - thalach: Maximum heart rate achieved
    - exang: Exercise induced angina (1 = yes, 0 = no)
    - oldpeak: ST depression induced by exercise
    - slope: Slope of peak exercise ST segment (0-2)
    - ca: Number of major vessels colored by fluoroscopy (0-3)
    - thal: Thalassemia (0-3)
    
    Returns:
    - probability: Heart disease probability (0-1)
    - prediction: Binary prediction (0 = no disease, 1 = disease)
    """
    
    # Load model
    model, feature_names = load_model()
    if model is None:
        return None, None
    
    # Create input array
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, 
                           thalach, exang, oldpeak, slope, ca, thal]])
    
    # Create DataFrame with proper feature names
    input_df = pd.DataFrame(input_data, columns=feature_names)
    
    # Make prediction
    probability = model.predict_proba(input_df)[0][1]  # Probability of class 1 (disease)
    prediction = model.predict(input_df)[0]
    
    return probability, prediction

def example_predictions():
    """Show example predictions for different patient profiles"""
    
    print("🔬 Heart Disease Prediction Model - Examples\n")
    print("=" * 60)
    
    # Example 1: Low risk patient
    print("\n📊 Example 1: Low Risk Patient")
    print("-" * 40)
    prob1, pred1 = predict_heart_disease(
        age=35, sex=0, cp=0, trestbps=120, chol=200, fbs=0, 
        restecg=0, thalach=180, exang=0, oldpeak=0, slope=1, ca=0, thal=1
    )
    if prob1 is not None:
        print(f"Patient Profile: 35-year-old female, normal vitals")
        print(f"Heart Disease Probability: {prob1:.2%}")
        print(f"Prediction: {'❤️ Healthy' if pred1 == 0 else '⚠️ At Risk'}")
    
    # Example 2: High risk patient
    print("\n📊 Example 2: High Risk Patient")
    print("-" * 40)
    prob2, pred2 = predict_heart_disease(
        age=65, sex=1, cp=3, trestbps=160, chol=300, fbs=1, 
        restecg=1, thalach=120, exang=1, oldpeak=2.5, slope=2, ca=2, thal=2
    )
    if prob2 is not None:
        print(f"Patient Profile: 65-year-old male, multiple risk factors")
        print(f"Heart Disease Probability: {prob2:.2%}")
        print(f"Prediction: {'❤️ Healthy' if pred2 == 0 else '⚠️ At Risk'}")
    
    # Example 3: Medium risk patient
    print("\n📊 Example 3: Medium Risk Patient")
    print("-" * 40)
    prob3, pred3 = predict_heart_disease(
        age=50, sex=1, cp=1, trestbps=140, chol=250, fbs=0, 
        restecg=0, thalach=150, exang=0, oldpeak=1.0, slope=1, ca=1, thal=1
    )
    if prob3 is not None:
        print(f"Patient Profile: 50-year-old male, moderate risk factors")
        print(f"Heart Disease Probability: {prob3:.2%}")
        print(f"Prediction: {'❤️ Healthy' if pred3 == 0 else '⚠️ At Risk'}")
    
    print("\n" + "=" * 60)
    print("💡 Model Performance: 85.25% accuracy (optimized with Optuna)")
    print("🔬 Based on 13 medical parameters")
    print("⚕️ For educational purposes only - consult medical professionals")

def custom_prediction():
    """Interactive function for custom predictions"""
    print("\n🩺 Custom Patient Assessment")
    print("-" * 40)
    print("Enter patient information:")
    
    try:
        age = int(input("Age: "))
        sex = int(input("Sex (0=female, 1=male): "))
        cp = int(input("Chest pain type (0-3): "))
        trestbps = int(input("Resting blood pressure: "))
        chol = int(input("Cholesterol (mg/dl): "))
        fbs = int(input("Fasting blood sugar > 120 (0=no, 1=yes): "))
        restecg = int(input("Resting ECG (0-2): "))
        thalach = int(input("Max heart rate: "))
        exang = int(input("Exercise angina (0=no, 1=yes): "))
        oldpeak = float(input("ST depression: "))
        slope = int(input("ST slope (0-2): "))
        ca = int(input("Major vessels (0-3): "))
        thal = int(input("Thalassemia (0-3): "))
        
        prob, pred = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, 
                                         restecg, thalach, exang, oldpeak, slope, ca, thal)
        
        if prob is not None:
            print(f"\n🎯 Results:")
            print(f"Heart Disease Probability: {prob:.2%}")
            print(f"Risk Level: {'❤️ Low Risk' if prob < 0.3 else '⚠️ Medium Risk' if prob < 0.7 else '🚨 High Risk'}")
            print(f"Prediction: {'❤️ Healthy' if pred == 0 else '⚠️ At Risk'}")
        
    except ValueError:
        print("Please enter valid numbers.")
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    print("🏥 Heart Disease Prediction Model")
    print("Choose an option:")
    print("1. View example predictions")
    print("2. Make custom prediction")
    
    choice = input("\nEnter choice (1 or 2): ")
    
    if choice == "1":
        example_predictions()
    elif choice == "2":
        custom_prediction()
    else:
        print("Invalid choice. Running examples...")
        example_predictions()
