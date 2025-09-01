# Heart Disease Data Analysis

🫀 **AI-Powered Heart Disease Risk Prediction and Data Analysis**

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://rifatahsanpul0k.github.io/heart_desease_data_analysis/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange)](https://scikit-learn.org/)

## 🌐 Live Website

Visit the project website: **[https://rifatahsanpul0k.github.io/heart_desease_data_analysis/](https://rifatahsanpul0k.github.io/heart_desease_data_analysis/)**

## 📋 Overview

This repository contains a comprehensive heart disease risk prediction system powered by machine learning. The project includes:

- **Interactive Streamlit Application**: Real-time heart disease risk assessment
- **Machine Learning Model**: Optimized ensemble model with 90%+ accuracy
- **Data Analysis**: Comprehensive analysis of 13 clinical parameters
- **GitHub Pages Website**: Professional presentation of the project

## 🚀 Features

### 🤖 Machine Learning Model
- **High Accuracy**: 90%+ prediction accuracy
- **13 Clinical Features**: Age, sex, chest pain type, blood pressure, cholesterol, and more
- **Risk Stratification**: Low, medium, and high-risk categorization
- **Feature Importance**: Understanding which factors contribute most to risk

### 📊 Interactive Analysis
- **Real-time Predictions**: Instant risk assessment
- **Data Visualizations**: Interactive charts and graphs
- **Feature Explanations**: Detailed descriptions of each clinical parameter
- **Model Performance**: Accuracy metrics and validation results

### 🎨 Professional Website
- **Responsive Design**: Mobile-friendly interface
- **Modern UI**: Clean, professional presentation
- **Comprehensive Documentation**: Detailed project information
- **Easy Navigation**: Intuitive user experience

## 🛠️ Technology Stack

- **Python**: Core programming language
- **Streamlit**: Interactive web application framework
- **Scikit-learn**: Machine learning library
- **Pandas & NumPy**: Data manipulation and analysis
- **Plotly**: Interactive data visualization
- **HTML/CSS/JavaScript**: Website frontend
- **GitHub Actions**: Automated deployment
- **GitHub Pages**: Static site hosting

## 📱 Streamlit Application

The heart disease prediction tool is built with Streamlit and provides:

### Input Parameters
1. **Age** (20-100 years)
2. **Sex** (Male/Female)
3. **Chest Pain Type** (4 categories)
4. **Resting Blood Pressure** (mmHg)
5. **Cholesterol Level** (mg/dl)
6. **Fasting Blood Sugar** (>120 mg/dl)
7. **Resting ECG Results** (3 categories)
8. **Maximum Heart Rate** (BPM)
9. **Exercise Induced Angina** (Yes/No)
10. **ST Depression** (0.0-6.0)
11. **ST Slope** (3 categories)
12. **Major Vessels** (0-3)
13. **Thalassemia** (4 categories)

### Output
- **Risk Percentage**: Probability of heart disease
- **Risk Level**: Low, Medium, or High risk classification
- **Feature Importance**: Which factors contribute most to the prediction
- **Recommendations**: Suggested actions based on risk level

## 🏗️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/rifatahsanpul0k/heart_desease_data_analysis.git
   cd heart_desease_data_analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application**
   ```bash
   streamlit run heart_disease_app.py
   ```

4. **View the website locally**
   - Open `index.html` in your browser for the static website
   - Visit `http://localhost:8501` for the Streamlit app

## 🌐 GitHub Pages Deployment

This repository is configured for automatic GitHub Pages deployment:

### Automatic Deployment
- **Workflow**: `.github/workflows/pages.yml`
- **Trigger**: Push to `main` branch
- **Content**: Static website files (HTML, CSS, JS)
- **URL**: `https://rifatahsanpul0k.github.io/heart_desease_data_analysis/`

### Manual Deployment
GitHub Pages can also be deployed manually:
1. Go to repository Settings
2. Navigate to Pages section
3. Select source branch (main)
4. Save settings

## 📁 Project Structure

```
heart_desease_data_analysis/
├── .github/
│   └── workflows/
│       └── pages.yml                 # GitHub Pages deployment workflow
├── assets/
│   ├── style.css                     # Website styles
│   └── script.js                     # Website JavaScript
├── heart_disease_app.py              # Main Streamlit application
├── heart_disease_model_optimized.pkl # Trained ML model
├── feature_names.pkl                 # Feature names for model
├── model_info.pkl                    # Model metadata
├── requirements.txt                  # Python dependencies
├── index.html                        # Main website page
├── .gitignore                        # Git ignore rules
└── README.md                         # Project documentation
```

## 🎯 Model Performance

### Metrics
- **Accuracy**: 90%+
- **Model Type**: Optimized Ensemble
- **Features**: 13 clinical parameters
- **Validation**: Cross-validated training

### Feature Importance
The model identifies the most significant risk factors:
1. Chest pain type
2. Maximum heart rate achieved
3. ST depression during exercise
4. Number of major vessels
5. Thalassemia results

## ⚠️ Important Disclaimers

- **Educational Purpose**: This tool is designed for educational and research purposes only
- **Not Medical Advice**: Results should not replace professional medical consultation
- **Healthcare Professional**: Always consult with qualified healthcare providers for medical decisions
- **Research Tool**: Intended for learning about machine learning applications in healthcare

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Links

- **Live Website**: [https://rifatahsanpul0k.github.io/heart_desease_data_analysis/](https://rifatahsanpul0k.github.io/heart_desease_data_analysis/)
- **GitHub Repository**: [https://github.com/rifatahsanpul0k/heart_desease_data_analysis](https://github.com/rifatahsanpul0k/heart_desease_data_analysis)
- **WHO Cardiovascular Diseases**: [https://www.who.int/health-topics/cardiovascular-diseases](https://www.who.int/health-topics/cardiovascular-diseases)

## 📞 Contact

For questions, suggestions, or collaboration opportunities, please open an issue in this repository.

---

**Built with ❤️ for healthcare education and machine learning research**