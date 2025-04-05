# 🏦 Loan Approval Prediction App

This is an AI-based web application that predicts whether a loan will be approved based on user inputs. It is built using traditional Machine Learning techniques and deployed using Flask and Render.

## 🚀 Features

- Predicts loan approval status using a trained Random Forest model.
- Built with a preprocessing pipeline using OneHotEncoder for categorical variables.
- Deployed and accessible via Render.
- Simple and user-friendly interface.

## 📊 Technologies Used

- Python
- Pandas, NumPy, Scikit-learn
- Flask (for API and web interface)
- Render (for deployment)

## 🧠 Model Overview

- **Algorithm:** RandomForestClassifier
- **Pipeline:** Combines preprocessing (OneHotEncoding) with model fitting
- **Training Data:** Preprocessed dataset with loan applicant features
- **Target Variable:** Loan approval status (Yes/No)

## ⚙️ How It Works

1. User enters loan applicant details via the web form.
2. Input is preprocessed and passed through the trained pipeline.
3. The model outputs a prediction (Approved / Not Approved).

## 📎 Links

- 🔗 **Live App on Render:** https://loan-approval-model-o7sk.onrender.com
- **GitHub Repository:** - **GitHub Repository:**(https://github.com/PNB001/Loan_Approval_Model.git)

## 📝 Installation (for local development)

```bash
git clone https://github.com/your-username/loan-approval-app.git
cd loan-approval-app
pip install -r requirements.txt
python app.py
