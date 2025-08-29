# 🫀 Heart Disease Risk Predictor

A machine learning web application that predicts heart disease risk using XGBoost classifier with Optuna hyperparameter optimization. Built with Streamlit and deployed on Render.

## 🚀 Live Demo

Access the application at: [Your Render URL will be here]

## 🎯 Features

- **Machine Learning Model**: XGBoost classifier with 85.25% accuracy
- **Hyperparameter Optimization**: Optuna-based Bayesian optimization
- **Interactive Web Interface**: Built with Streamlit
- **Real-time Predictions**: Instant heart disease risk assessment
- **Feature Importance**: Visual analysis of key risk factors
- **Health Check Endpoint**: Monitoring and status checking
- **Environment Configuration**: Comprehensive production settings

## 📊 Model Performance

- **Accuracy**: 85.25%
- **Optimization**: 100 trials using Optuna
- **Features**: 13 clinical parameters
- **Validation**: Cross-validated for reliability

## 🛠️ Technology Stack

- **Backend**: Python 3.11.4
- **ML Framework**: XGBoost 1.7.6+
- **Web Framework**: Streamlit 1.28.0+
- **Optimization**: Optuna 3.4.0+
- **Deployment**: Render (Cloud Platform)
- **Version Control**: Git/GitHub

## 🚀 Quick Start

### Local Deployment
```bash
# Clone the repository
git clone https://github.com/your-username/heart_disease_predictor.git
cd heart_disease_predictor

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env

# Run the app
streamlit run heart_disease_app.py
```

### Render Cloud Deployment
1. **Fork this repository** to your GitHub account
2. **Connect to Render**: Sign up at [render.com](https://render.com)
3. **Create Web Service**: Connect your GitHub repository
4. **Configure Environment Variables** (see Environment Variables section)
5. **Deploy**: Automatic deployment on every commit

## 🔧 Environment Variables

Configure these variables in your Render dashboard or `.env` file:

```bash
# App Configuration
APP_TITLE=Heart Disease Risk Predictor
APP_VERSION=1.2.0
MODEL_NAME=heart_disease_model

# Environment Settings
APP_ENVIRONMENT=production
DEBUG_MODE=false
LOG_LEVEL=INFO

# Model Configuration
ENABLE_MODEL_CACHING=true
CACHE_TTL_SECONDS=3600
MODEL_ACCURACY_THRESHOLD=0.80

# Performance Settings
MAX_UPLOAD_SIZE_MB=10
SESSION_TIMEOUT_MINUTES=30
MAX_CONCURRENT_USERS=100

# Feature Flags
ENABLE_ANALYTICS=false
HEALTH_CHECK_ENDPOINT=/health
```

## 🏥 Clinical Features

The model uses the following medical parameters:
1. **Age** (20-100 years)
2. **Sex** (Male/Female)
3. **Chest Pain Type** (4 categories)
4. **Resting Blood Pressure** (80-200 mmHg)
5. **Cholesterol** (100-600 mg/dl)
6. **Fasting Blood Sugar** (>120 mg/dl)
7. **Resting ECG** (3 categories)
8. **Maximum Heart Rate** (60-220 bpm)
9. **Exercise Induced Angina** (Yes/No)
10. **ST Depression** (0-6.2)
11. **ST Slope** (3 categories)
12. **Major Vessels** (0-4)
13. **Thalassemia** (3 categories)

## 🩺 Health Check

Monitor application health:

- **Endpoint**: `/?health=check`
- **Response**: JSON with app status, version, and metadata
- **Use Case**: Load balancer health checks, monitoring

## 📁 Project Structure

```
heart_disease_predictor/
├── heart_disease_app.py          # Main Streamlit application
├── heart_disease_model.pkl       # Trained XGBoost model
├── feature_names.pkl             # Feature name mappings
├── model_info.pkl                # Model metadata
├── data.csv                      # Training dataset
├── hello.ipynb                   # Data analysis notebook
├── requirements.txt              # Python dependencies
├── runtime.txt                   # Python version for Render
├── Procfile                      # Render startup command
├── render.yaml                   # Render deployment config
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## ⚠️ Medical Disclaimer

**Important**: This application is for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical decisions.

## 🔄 Continuous Deployment

- **GitHub Integration**: Automatic builds on push
- **Environment Management**: Render environment variables
- **Version Control**: Semantic versioning
- **Monitoring**: Health checks and logging

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Made with ❤️ for healthcare AI**

## Disclaimer
This application is for educational and research purposes only. 
It should not be used as a substitute for professional medical advice, 
diagnosis, or treatment.

## License
MIT License - Feel free to use and modify for educational purposes.
