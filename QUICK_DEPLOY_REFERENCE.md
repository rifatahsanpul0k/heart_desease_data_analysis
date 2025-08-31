# 🚀 QUICK RENDER DEPLOYMENT REFERENCE

## 📋 Essential Commands (Run These First)

```bash
# 1. Check files are ready
ls -la *.pkl *.py *.txt *.env

# 2. Commit to GitHub  
git add .
git commit -m "Deploy Heart Disease Predictor to Render"
git push origin main

# 3. Go to render.com → New Web Service
```

---

## 🔧 EXACT Render Configuration

### Service Settings:
```
Name: heart-disease-predictor
Environment: Python 3
Branch: main
Build Command: pip install --upgrade pip && pip install -r requirements.txt
Start Command: streamlit run heart_disease_app.py --server.headless true --server.port $PORT --server.address 0.0.0.0
```

### Environment Variables (Copy Each Line):
```
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=$PORT
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
PYTHON_VERSION=3.11.4
```

---

## ✅ Quick Test Commands

```bash
# Test model files
python3 -c "import joblib; print('✅ Model:', joblib.load('heart_disease_model_optimized.pkl'))"

# Test local app (optional)
streamlit run heart_disease_app.py --server.port 8501
```

---

## 🎯 Expected Result

**Your app will be live at:**
`https://heart-disease-predictor-[random].onrender.com`

**Features:**
- 90.16% accuracy Random Forest model
- Interactive medical parameter input
- Real-time heart disease risk prediction
- Mobile-responsive design

---

## 🆘 If Something Fails

1. **Build Error:** Check requirements.txt format
2. **Start Error:** Verify start command exactly as shown
3. **Access Error:** Check environment variables
4. **Model Error:** Ensure all .pkl files are in repository

**Deploy Time:** 3-5 minutes | **Free Tier:** ✅ Supported
