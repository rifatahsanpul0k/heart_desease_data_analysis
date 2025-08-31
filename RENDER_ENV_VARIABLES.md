# 🔧 Render Environment Variables Configuration

## 📋 Required Environment Variables

Copy these **exactly** into your Render service environment variables:

### **Core Streamlit Variables**
```
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=$PORT
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

### **Python Configuration**
```
PYTHON_VERSION=3.11.4
```
DEBUG_MODE=true
LOG_LEVEL=INFO
ENABLE_MODEL_CACHING=true
CACHE_TTL_SECONDS=3600
MODEL_ACCURACY_THRESHOLD=0.80
MAX_UPLOAD_SIZE_MB=10
SESSION_TIMEOUT_MINUTES=30
MAX_CONCURRENT_USERS=100
ENABLE_ANALYTICS=false
HEALTH_CHECK_ENDPOINT=/health

## Instructions:

1. Go to your Render dashboard
2. Select your web service
3. Go to the "Environment" tab
4. Add each variable above as a new environment variable
5. Save and redeploy

## Notes:

- Set DEBUG_MODE=true only for testing
- Adjust CACHE_TTL_SECONDS based on your needs (3600 = 1 hour)
- MODEL_ACCURACY_THRESHOLD is used to warn if model performance drops
- ENABLE_ANALYTICS=true will show analytics info in sidebar
- Health check endpoint will be available at your-app-url/?health=check
