import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

st.set_page_config(
    page_title="Heart Disease Risk Predictor - Debug",
    page_icon="🫀",
    layout="wide"
)

st.title("🔧 Debug Mode - Heart Disease Predictor")

# Test basic functionality
st.header("1. Basic Tests")

try:
    st.success("✅ Streamlit import successful")
    st.success("✅ Pandas import successful") 
    st.success("✅ NumPy import successful")
    st.success("✅ Pickle import successful")
except Exception as e:
    st.error(f"❌ Import error: {e}")

# Test file existence
st.header("2. File Existence Check")

files_to_check = [
    'optimized_xgb_model.pkl',
    'feature_names.pkl', 
    'model_info.pkl'
]

for file in files_to_check:
    if os.path.exists(file):
        st.success(f"✅ {file} exists")
        try:
            # Test if file can be loaded
            with open(file, 'rb') as f:
                data = pickle.load(f)
            st.success(f"✅ {file} loaded successfully")
        except Exception as e:
            st.error(f"❌ {file} loading failed: {e}")
    else:
        st.error(f"❌ {file} not found")

# Test model loading
st.header("3. Model Loading Test")

try:
    with open('optimized_xgb_model.pkl', 'rb') as f:
        model = pickle.load(f)
    st.success("✅ Model loaded successfully")
    st.info(f"Model type: {type(model)}")
    
    # Test prediction with dummy data
    dummy_data = np.array([[63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]])
    prediction = model.predict(dummy_data)
    st.success(f"✅ Model prediction test successful: {prediction}")
    
except Exception as e:
    st.error(f"❌ Model loading/prediction failed: {e}")
    st.error(f"Error type: {type(e)}")

# Environment info
st.header("4. Environment Information")
st.info(f"Python path: {os.sys.executable}")
st.info(f"Current directory: {os.getcwd()}")
st.info(f"Files in current directory: {os.listdir('.')}")

# Test imports one by one
st.header("5. Individual Import Tests")

imports_to_test = [
    ('plotly.express', 'px'),
    ('plotly.graph_objects', 'go'),
    ('sklearn.metrics', 'classification_report'),
    ('joblib', None)
]

for module, alias in imports_to_test:
    try:
        if alias:
            exec(f"import {module} as {alias}")
        else:
            exec(f"import {module}")
        st.success(f"✅ {module} import successful")
    except Exception as e:
        st.error(f"❌ {module} import failed: {e}")

st.header("6. Query Params Test")
try:
    query_params = st.query_params
    st.success("✅ New st.query_params works")
    st.json(dict(query_params))
except Exception as e:
    st.warning(f"⚠️ New query_params failed: {e}")
    try:
        query_params = st.experimental_get_query_params()
        st.success("✅ Old st.experimental_get_query_params works")
        st.json(query_params)
    except Exception as e2:
        st.error(f"❌ Both query params methods failed: {e2}")
