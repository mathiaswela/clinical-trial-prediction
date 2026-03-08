# Predicting Clinical Trial Success

## Project overview
This project aims to build a robust machine learning pipeline to predict if a clinical trial is successfully completed or terminated before completion. Using data from **AACT (Aggregate Analysis of ClinicalTrials.gov)** database, the project explores data science in relation to pharmaceutical drug development.

The goal is to demonstrate a complete Data Science pipeline: From raw SQL database extraction, statistical EDA to classification modelling and hyperparameter tuning.

## Data Pipeline
- **Extraction**
- **Cleaning & Validation**
- **EDA**
- **Modelling**

## Tech Stack
- **Languages:** Python (SQLAlchemy, Pandas, scikit-learn, Seaborn)
- **Database:** PostgreSQL (AACT Database)
- **Tools:** PyCharm, Git/GitHub, Jupyter Notebooks
- **Methodology:** Advanced Statistical Imputation & Missing Data Mechanism Analysis (MDMA)

## Key Features Implemented:
- **PostgreSQL Integration:** Raw data is managed via a SQL backend to simulate a production-like data environment.
- **Missing Data Mechanism Analysis (MDMA):** Deep dive into whether data is missing at random (MAR) or has systematic biases. Important for avoiding skewed model results.
- **Advanced Imputation (MICE):** Using Multivariate Imputation by Chained Equations to handle missing data with higher statistical accuracy than mean/median imputation.
- **Feature Engineering & Encoding:** Implemented One-Hot Encoding of categorical variables transforming qualitative data into model-ready numerical vectors.

## Current Status: Phase 1 (Data Acquisition, Data Audit, Feature Engineering and Baseline Modelling) 
I have deliberately chosen to focus on building a robust pipeline before applying predictive models like XGBoost.
 - [x] Environment setup and credential management
 - [x] Database Migration (PostgreSQL)
 - [x] Missing Data Analysis & MICE Imputation
 - [x] Feature Engineering (Encoding implemente)
 - [ ] Baseline Modeling (XGBoost/Random Forest)
 - [ ] Model Validation & Tuning
