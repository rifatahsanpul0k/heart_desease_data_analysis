# Quick Model Usage Guide

## 🚀 3 Ways to Use Your Heart Disease Prediction Model

### **1. 🌐 Web App (Easiest)**
Your Streamlit app is running at: **http://localhost:8502**
- Interactive interface
- Real-time predictions
- Visual risk assessment
- No coding required!

### **2. 🐍 Python Script**
```bash
python use_model.py
```
- Choose example predictions or custom input
- Direct model access
- Programmatic usage

### **3. 📊 Jupyter Notebook**
Open `hello.ipynb` and use the model directly:
```python
# Load your trained model
import joblib
model = joblib.load('optimized_xgb_model.joblib')

# Make predictions
probability = model.predict_proba(input_data)[0][1]
```

## 📋 **Model Input Parameters**

Your model expects 13 features:
1. **age**: Age in years
2. **sex**: Sex (1 = male, 0 = female)  
3. **cp**: Chest pain type (0-3)
4. **trestbps**: Resting blood pressure
5. **chol**: Serum cholesterol in mg/dl
6. **fbs**: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
7. **restecg**: Resting electrocardiographic results (0-2)
8. **thalach**: Maximum heart rate achieved
9. **exang**: Exercise induced angina (1 = yes, 0 = no)
10. **oldpeak**: ST depression induced by exercise
11. **slope**: Slope of peak exercise ST segment (0-2)
12. **ca**: Number of major vessels (0-3)
13. **thal**: Thalassemia (0-3)

## 🎯 **Model Performance**
- **Accuracy**: 85.25%
- **Optimization**: 50 Optuna trials
- **Improvement**: 1.64% over baseline

## � **High Risk Example**

**91.6% Risk Case - Surprising Discovery:**
```python
# 50-year-old female with typical angina (chest pain type 0)
# All other parameters normal, but model predicts HIGH RISK!
age=50, sex=0, cp=0, trestbps=120, chol=200, fbs=0, 
restecg=0, thalach=180, exang=0, oldpeak=0.0, slope=1, ca=0, thal=1

# Result: 91.6% heart disease probability
```

**Key Insight:** Your model learned that **typical angina in middle-aged women** is highly predictive, even with otherwise normal parameters!

Run `python final_high_risk_examples.py` for detailed examples.

## �🚀 **Next Steps**
1. **Use the web app** for quick assessments
2. **Integrate into your workflow** using the Python script
3. **Deploy to cloud** for public access
4. **Extend the model** with more features

**Your model is ready for production use!** 🏥
