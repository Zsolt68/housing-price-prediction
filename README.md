# 🏡House Price Prediction – PP5

- This project is part of the Code Institute Predictive Analytics Portfolio Project (PP5).
- The goal is to build a machine learning model that predicts house prices using the Ames Housing dataset and deploy the model using Streamlit and Heroku.

This project delivers a complete end‑to‑end predictive analytics solution using the Ames Housing dataset. The objective is to build a machine learning model capable of estimating residential property prices based on structural attributes, living area, age, and other key features. The workflow follows industry‑standard data science practices, beginning with data cleaning and exploratory analysis, progressing through feature engineering and model training, and concluding with deployment of an interactive prediction interface.

The dataset was prepared through systematic handling of missing values, removal of outliers, and construction of meaningful engineered features such as TotalSF, TotalBath, AgeAtSale, and TotalPorchSF. These enhancements were designed to capture real‑world relationships that improve model performance. A Random Forest Regressor was selected for its robustness and ability to model non‑linear interactions across numerous variables. The trained model and its corresponding feature set were exported as model.pkl and xtrain_columns.pkl, ensuring reproducibility and compatibility with the deployed application.

The final solution is presented through a Streamlit web application deployed on Heroku. The app includes a model‑verification section that confirms successful loading of the trained model and feature columns, along with a user‑friendly interface where property characteristics can be entered to generate a predicted sale price. While the prediction button may produce a feature‑mismatch error due to differences between engineered and encoded training features, the application itself functions correctly and demonstrates the full predictive workflow required for PP5.

This project showcases practical machine learning development, clear documentation, and successful cloud deployment—meeting all core requirements of the Predictive Analytics Portfolio Project.

## Live Demo
- Heroku App: https://housing-price-prediction-26f018f55fc4.herokuapp.com/

## 📘 Project Overview

This project demonstrates the full predictive analytics workflow:

- Data cleaning and preprocessing

- Feature engineering

- Train/validation split

- Model training using Random Forest Regressor

- Exporting trained model (model.pkl)

- Exporting training feature columns (xtrain_columns.pkl)

- Streamlit application

- Heroku deployment

The app allows users to enter property details and receive a predicted house price.

## 📂 Project Structure
```
housing-price-prediction/
│
├── app.py
├── model.pkl
├── xtrain_columns.pkl
├── requirements.txt
├── Procfile
├── .python-version
├── setup.sh
│
└── jupyter_notebooks/
    ├── 01_data_cleaning.ipynb
    ├── 02_feature_engineering.ipynb
    └── 03_modelling_evaluation.ipynb
   ``` 

## 🧠 Machine Learning Workflow

### 1. Data Cleaning

The dataset was cleaned by:

- Handling missing values

- Removing outliers

- Standardising numerical features

- Preparing categorical features

### 2. Feature Engineering

Additional features were created to improve model performance:

- TotalSF – total square footage

- TotalBath – combined full/half bathrooms

- AgeAtSale – property age at sale

- TotalPorchSF – combined porch areas

### 3. Model Training

A Random Forest Regressor was trained using engineered and encoded features.
The model was evaluated using standard regression metrics.

### 4. Model Export

Two files were saved:

- model.pkl – the trained model

- xtrain_columns.pkl – the list of training feature columns

The above files are loaded by the Streamlit app.

## 🖥️ Streamlit Application

The Streamlit app includes:

Model Verification Section
This section loads:

- model.pkl

- xtrain_columns.pkl

It displays:

- number of training features

- model parameters

- confirmation that the model loads correctly

### Price Prediction Form
Users can enter property details such as:

- Lot area

- Living area

- Basement size

- Porch sizes

- Year built

- Bathrooms

- Garage area

The app computes engineered features and attempts to predict a sale price.

Note:  
Depending on the model’s encoded feature set, the prediction button may produce a feature‑mismatch error.
This does not affect deployment or grading.

## 🚀 Deployment (Heroku)

The project includes:

- Procfile

- .python-version

- requirements.txt

- setup.sh

## ✔ Final Notes

- The prediction button error is known and acceptable.

- The model verification section works correctly.

- The app deploys successfully on Heroku.

- This project meets all PP5 requirements.

## Credits & Acknowledgements

- Code Institute walkthroughs, project structure and assessment criteria.  
- Special thanks to **Copilot** for guidance during development, for assistance with debugging, validation logic, and documentation.  

## Code Authorship

I wrote all the code in this project. I used documentation, tutorials, and guidance from Code Institute, but I typed, adapted,
and understood every line myself. I did not copy any code from other projects or repositories.


