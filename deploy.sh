#!/bin/bash

# 🚀 Quick Deployment Script for Heart Disease Predictor
# Run this script to prepare and deploy your app

echo "🔧 Heart Disease Predictor - Quick Deploy Script"
echo "================================================="

# Check if we're in the right directory
if [ ! -f "heart_disease_app.py" ]; then
    echo "❌ Error: heart_disease_app.py not found. Please run this script from the project directory."
    exit 1
fi

echo "📍 Current directory: $(pwd)"

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source .venv/bin/activate

# Verify Python version
echo "🐍 Python version: $(python --version)"

# Install/update dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Test model files
echo "🤖 Checking model files..."
if [ -f "heart_disease_model_optimized.pkl" ] && [ -f "feature_names.pkl" ] && [ -f "model_info.pkl" ]; then
    echo "✅ All model files present"
else
    echo "❌ Missing model files!"
    exit 1
fi

# Test app import
echo "🧪 Testing app imports..."
python -c "
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
print('✅ All imports successful')
"

if [ $? -ne 0 ]; then
    echo "❌ Import test failed!"
    exit 1
fi

# Git operations
echo "📤 Preparing Git repository..."
git add .
git status

echo ""
echo "🎯 Ready for deployment! Choose your platform:"
echo ""
echo "1. 🆓 Streamlit Cloud (FREE):"
echo "   Go to: https://share.streamlit.io"
echo "   Repository: rifatahsanpul0k/heart_desease_data_analysis"
echo "   Main file: heart_disease_app.py"
echo ""
echo "2. 💰 Render:"
echo "   Go to: https://render.com"
echo "   Build: pip install -r requirements.txt"
echo "   Start: streamlit run heart_disease_app.py --server.port=\$PORT --server.address=0.0.0.0"
echo ""
echo "3. 🚄 Railway:"
echo "   Go to: https://railway.app"
echo "   Connect GitHub repository"
echo ""
echo "📝 Commit your changes first:"
echo "   git commit -m 'Ready for deployment'"
echo "   git push origin main"
echo ""
echo "🎉 Your app is ready for production!"
