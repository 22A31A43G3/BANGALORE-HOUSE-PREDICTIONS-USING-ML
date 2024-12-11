
#Bangalore House Price Prediction
This repository contains the code and process used for predicting house prices in Bangalore, India, using machine learning. This is my first data science project, where I focused on exploring, cleaning, and modeling house price data to build predictive models. The final model was deployed using Streamlit to showcase the results.

Project Overview
The goal of this project is to predict the prices of houses in Bangalore based on features such as location, area, number of bedrooms, etc. We used a dataset containing historical house price data, performed exploratory data analysis (EDA), preprocessed the data, and built multiple models to predict house prices. The project also explores the impact of outliers on model performance.

Key Steps in the Project:
Data Loading & Exploration:

Loaded the dataset from a CSV file.
Performed Exploratory Data Analysis (EDA) to understand the distribution of variables, check for missing values, and explore correlations between different features and the target variable (house price).
Data Preprocessing:

Handled missing values, feature encoding, and scaling of data as needed.
Removed outliers that were identified during the EDA process to improve the model's accuracy.
Model Training:

Trained multiple machine learning models to predict house prices, such as:
Linear Regression
Random Forest Regressor
Decision Tree Regressor
Created and evaluated a model both with and without outliers to compare the effects on accuracy.
Model Evaluation:

Evaluated models using mean absolute error (MAE), root mean squared error (RMSE), and R^2 score to assess performance.
Trained the best model with the highest accuracy, which achieved 73% accuracy.
Deployment:

Deployed the model with the highest accuracy using Streamlit, providing a user-friendly interface to input features and predict house prices in real-time.
Technologies Used:
Python
Pandas
Numpy
Matplotlib, Seaborn (for EDA and visualization)
Scikit-learn (for modeling)
Streamlit (for deployment)
