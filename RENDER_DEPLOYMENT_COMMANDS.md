# 🚀 Complete Render Deployment Commands & Setup

## 📋 Pre-Deployment Checklist Commands

### 1. Verify All Files Exist
```bash
ls -la *.pkl *.py *.txt *.yaml *.env *.csv
```

### 2. Check Git Status
```bash
git status
git add .
git commit -m "Prepare for Render deployment - Heart Disease Predictor v2.0"
git push origin main
```

### 3. Test Local Environment (Optional)
```bash
# Activate virtual environment
source .venv/bin/activate

# Test core functionality
python3 -c "
import joblib
import pandas as pd
model = joblib.load('heart_disease_model_optimized.pkl')
print('✅ Model loads successfully')
print(f'Model type: {type(model).__name__}')
"
```

---

## 🌐 Render Service Configuration

### Service Settings (Copy these exactly):

```yaml
Service Name: heart-disease-predictor
Environment: Python 3
Region: Oregon (or your preferred region)
Branch: main
Runtime: python3

Build Command: 
pip install --upgrade pip && pip install -r requirements.txt

Start Command:
streamlit run heart_disease_app.py --server.headless true --server.port $PORT --server.address 0.0.0.0
```

---

## 🔧 Environment Variables Commands

### Copy these EXACT environment variables to Render:

```bash
# Core Streamlit (REQUIRED)
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=$PORT
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Python & Performance
PYTHON_VERSION=3.11.4
ENABLE_MODEL_CACHING=true
CACHE_TTL_SECONDS=3600

# Application Info
APP_TITLE=Heart Disease Risk Predictor
MODEL_NAME=heart_disease_model_optimized.pkl
```

---

## 📝 Step-by-Step Render Commands

### Step 1: Login to Render
```
1. Go to: https://render.com
2. Click "Sign in with GitHub"
3. Authorize Render access to your repositories
```

### Step 2: Create Web Service
```
1. Click "New +"
2. Select "Web Service" 
3. Choose "Build and deploy from a Git repository"
4. Click "Connect" next to GitHub
5. Find repository: heart_desease_data_analysis
6. Click "Connect"
```

### Step 3: Configure Service
```
Name: heart-disease-predictor
Environment: Python 3
Region: Oregon
Branch: main
Build Command: pip install --upgrade pip && pip install -r requirements.txt
Start Command: streamlit run heart_disease_app.py --server.headless true --server.port $PORT --server.address 0.0.0.0
```

### Step 4: Add Environment Variables
```
Key: STREAMLIT_SERVER_HEADLESS        Value: true
Key: STREAMLIT_SERVER_PORT           Value: $PORT
Key: STREAMLIT_SERVER_ADDRESS        Value: 0.0.0.0
Key: STREAMLIT_BROWSER_GATHER_USAGE_STATS  Value: false
Key: PYTHON_VERSION                  Value: 3.11.4
```

### Step 5: Deploy
```
1. Click "Create Web Service"
2. Wait 3-5 minutes for build
3. Check logs for any errors
4. Test the deployed URL
```

---

## 🔍 Deployment Verification Commands

### Check Deployment Status
```bash
# Your app will be available at:
https://heart-disease-predictor-[random].onrender.com

# Test endpoints:
curl https://your-app-url.onrender.com
curl https://your-app-url.onrender.com/_stcore/health
```

### Local Testing Commands (Before Deployment)
```bash
# Activate environment
source .venv/bin/activate

# Test Streamlit locally
streamlit run heart_disease_app.py --server.port 8501

# Test with deployment settings
streamlit run heart_disease_app.py --server.headless true --server.port 8501 --server.address 0.0.0.0
```

---

## 🛠️ Troubleshooting Commands

### If Build Fails:
```bash
# Check requirements.txt
cat requirements.txt

# Test requirements locally
pip install -r requirements.txt

# Check Python version
python3 --version
```

### If App Won't Start:
```bash
# Check model files exist
ls -la *.pkl

# Test model loading
python3 -c "
import joblib
model = joblib.load('heart_disease_model_optimized.pkl')
feature_names = joblib.load('feature_names.pkl')
model_info = joblib.load('model_info.pkl')
print('All model files load successfully!')
"
```

### If Port Issues:
```bash
# Verify start command uses $PORT
echo "streamlit run heart_disease_app.py --server.headless true --server.port \$PORT --server.address 0.0.0.0"
```

---

## 📊 Post-Deployment Testing Commands

### Test App Functionality:
```bash
# Test homepage
curl -I https://your-app-url.onrender.com

# Test health check (if implemented)
curl https://your-app-url.onrender.com/_stcore/health

# Monitor performance
curl -w "@curl-format.txt" -o /dev/null -s https://your-app-url.onrender.com
```

### Performance Monitoring:
```bash
# Create curl timing format file
cat > curl-format.txt << 'EOF'
     time_namelookup:  %{time_namelookup}\n
        time_connect:  %{time_connect}\n
     time_appconnect:  %{time_appconnect}\n
    time_pretransfer:  %{time_pretransfer}\n
       time_redirect:  %{time_redirect}\n
  time_starttransfer:  %{time_starttransfer}\n
                     ----------\n
          time_total:  %{time_total}\n
EOF
```

---

## 🔄 Update & Redeploy Commands

### Update Your App:
```bash
# Make changes to your code
# Commit and push changes
git add .
git commit -m "Update heart disease predictor"
git push origin main

# Render will automatically redeploy
```

### Manual Redeploy (if needed):
```bash
# Go to Render dashboard
# Select your service
# Click "Deploy latest commit"
```

---

## 📱 App Features Test Commands

### Test Data for Manual Validation:

#### High Risk Patient:
```
Age: 65
Sex: Male  
Chest Pain: Typical Angina
Blood Pressure: 160
Cholesterol: 280
Expected Result: High Risk (>70%)
```

#### Low Risk Patient:
```
Age: 35
Sex: Female
Chest Pain: Asymptomatic  
Blood Pressure: 110
Cholesterol: 180
Expected Result: Low Risk (<30%)
```

---

## 🎯 Final Verification Checklist

### ✅ Deployment Success Indicators:
- [ ] Build completes without errors
- [ ] App starts successfully  
- [ ] External URL is accessible
- [ ] All input fields work
- [ ] Predictions generate correctly
- [ ] Charts and visualizations display
- [ ] Mobile responsiveness works

### 📞 Emergency Commands:
```bash
# If app crashes, check logs in Render dashboard
# If build fails, verify requirements.txt
# If can't access, check environment variables
# If slow performance, check model file sizes
```

---

## 🎉 Success! Your Commands Summary

### Quick Deploy Commands:
```bash
# 1. Prepare
git add .
git commit -m "Deploy to Render"
git push origin main

# 2. Go to render.com and create service with these settings:
# Build: pip install --upgrade pip && pip install -r requirements.txt  
# Start: streamlit run heart_disease_app.py --server.headless true --server.port $PORT --server.address 0.0.0.0

# 3. Add environment variables from .env file

# 4. Deploy and test!
```

**🚀 Your heart disease predictor will be live in 3-5 minutes!**
