# 🚀 Heart Disease Predictor - Complete Deployment Guide

## 📋 Pre-Deployment Checklist

✅ All files ready:
- `heart_disease_app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies (fixed versions)
- `heart_disease_model_optimized.pkl` - Trained model (90.16% accuracy)
- `feature_names.pkl` - Feature names
- `model_info.pkl` - Model metadata
- `.env.production` - Environment variables
- `README.md` - Documentation

## 🔧 Essential Commands for Deployment

### 1. 📦 Final Environment Setup
```bash
# Navigate to project directory
cd /Users/rifatahasan/Documents/heart_desease

# Activate virtual environment
source .venv/bin/activate

# Install/verify all dependencies
pip install -r requirements.txt

# Test app locally one final time
streamlit run heart_disease_app.py
```

### 2. 📤 Git Repository Commands
```bash
# Add all files to git
git add .

# Commit with deployment message
git commit -m "Ready for production deployment - v1.0"

# Push to GitHub
git push origin main

# Verify repository status
git status
git log --oneline -5
```

### 3. 🌐 Platform-Specific Deployment Commands

#### Option A: Streamlit Community Cloud (FREE)
```bash
# Repository URL needed: https://github.com/rifatahsanpul0k/heart_desease_data_analysis
# 1. Go to: https://share.streamlit.io
# 2. Connect GitHub account
# 3. Select repository: rifatahsanpul0k/heart_desease_data_analysis
# 4. Main file: heart_disease_app.py
# 5. Python version: 3.11
# 6. Deploy!
```

#### Option B: Render Deployment
```bash
# Build Command (for Render):
pip install -r requirements.txt

# Start Command (for Render):
streamlit run heart_disease_app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true

# Render will auto-detect Python and use requirements.txt
```

#### Option C: Railway Deployment
```bash
# Railway auto-deploys from GitHub
# Connect repository at: https://railway.app
# Environment variables will be loaded from .env.production
```

### 4. 📱 Local Testing Commands
```bash
# Test with production-like settings
streamlit run heart_disease_app.py --server.headless=true --server.port=8501

# Test model loading specifically
python -c "
import joblib
model = joblib.load('heart_disease_model_optimized.pkl')
print(f'Model loaded: {type(model)}')
print(f'Model score: {joblib.load(\"model_info.pkl\")[\"accuracy\"]:.2%}')
"

# Test app import
python -c "
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
print('All imports successful!')
"
```

## 🔑 Environment Variables for Each Platform

### Streamlit Cloud Environment Variables:
```
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

### Render Environment Variables:
```
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=$PORT
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_ENABLE_CORS=false
PYTHON_VERSION=3.11.8
```

### Railway Environment Variables:
```
STREAMLIT_SERVER_HEADLESS=true
PORT=8080
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_ENABLE_CORS=false
```

## 🎯 Quick Deploy Commands (Copy & Paste)

### For Streamlit Cloud:
```bash
# 1. Ensure everything is committed
git add . && git commit -m "Production ready" && git push origin main

# 2. Open deployment page
open https://share.streamlit.io/new
```

### For Render:
```bash
# 1. Commit and push
git add . && git commit -m "Deploy to Render" && git push origin main

# 2. Create new web service at render.com with:
# Build Command: pip install -r requirements.txt
# Start Command: streamlit run heart_disease_app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
```

### For Railway:
```bash
# 1. Push to GitHub
git add . && git commit -m "Deploy to Railway" && git push origin main

# 2. Connect repository at railway.app
# 3. Auto-deployment will start
```

## 🔍 Troubleshooting Commands

### Check Dependencies:
```bash
pip list | grep -E "(streamlit|numpy|pandas|sklearn|matplotlib|seaborn|plotly|joblib)"
```

### Verify Model Files:
```bash
ls -la *.pkl
python -c "import joblib; print([f for f in ['heart_disease_model_optimized.pkl', 'feature_names.pkl', 'model_info.pkl'] if joblib.load(f) is not None])"
```

### Test App Locally:
```bash
streamlit run heart_disease_app.py --server.port=8502
```

## 📊 Expected Deployment Results

### Success Indicators:
- ✅ App loads without errors
- ✅ Model prediction works with test data
- ✅ All 13 input fields function correctly
- ✅ Visualization displays properly
- ✅ 90.16% accuracy model responds correctly

### URLs After Deployment:
- **Streamlit Cloud**: `https://heart-disease-predictor-rifatahasan.streamlit.app`
- **Render**: `https://heart-disease-predictor.onrender.com`
- **Railway**: `https://heart-disease-predictor.railway.app`

## 🎉 Post-Deployment Testing

Test your deployed app with these sample inputs:
```
Age: 54, Sex: Male, Chest Pain: Typical Angina
Blood Pressure: 140, Cholesterol: 240
Expected: High Risk (~80% probability)
```

## 📞 Support Commands

If deployment fails, run these diagnostic commands:
```bash
# Check Python version
python --version

# Verify all files exist
ls -la heart_disease_app.py requirements.txt *.pkl

# Test imports individually
python -c "import streamlit; print('Streamlit OK')"
python -c "import sklearn; print('Sklearn OK')"
python -c "import joblib; print('Joblib OK')"
```

---
🚀 **Your Heart Disease Prediction App is Ready for Production!**
