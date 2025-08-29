# Heart Disease Prediction Model - Deployment Guide

## 🚀 Live Deployment Steps

### **Option 1: Streamlit Community Cloud (FREE & Recommended)**

1. **Go to [share.streamlit.io](https://share.streamlit.io)**
2. **Sign in with your GitHub account**
3. **Click "New app"**
4. **Enter repository details:**
   - Repository: `rifatahsanpul0k/heart_desease_data_analysis`
   - Branch: `main`
   - Main file path: `heart_disease_app.py`
5. **Click "Deploy!"**

Your app will be live at: `https://your-app-name.streamlit.app`

### **Option 2: Heroku (Alternative)**

1. **Install Heroku CLI**
2. **Create a Procfile:**
   ```
   web: streamlit run heart_disease_app.py --server.port=$PORT --server.address=0.0.0.0
   ```
3. **Deploy:**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### **Option 3: Railway (Modern Alternative)**

1. **Go to [railway.app](https://railway.app)**
2. **Connect your GitHub repository**
3. **Auto-deploy from `heart_disease_app.py`**

## 📱 **Your App Features**

- **Interactive Heart Disease Risk Assessment**
- **Real-time Predictions with 85.25% Accuracy**
- **Visual Risk Gauge & Feature Importance**
- **Professional Medical Parameter Input**

## 🔧 **Technical Specs**

- **Model**: XGBoost Optimized with Optuna
- **Framework**: Streamlit
- **Dependencies**: All specified in `requirements.txt`
- **Model Files**: Included and ready to deploy

## 🌐 **Repository**
GitHub: https://github.com/rifatahsanpul0k/heart_desease_data_analysis

## 📊 **Model Performance**
- Accuracy: 85.25%
- Optimized with 50 Optuna trials
- Ready for production use

---
**Ready to deploy in 1 click!** 🚀
