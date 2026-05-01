# 🏠 House Price Prediction API

This project is a Machine Learning-based **House Price Prediction System** built using FastAPI and deployed using Docker. The model predicts house prices based on input features like area, location, bedrooms, etc.

---

## 🚀 Features

- Machine Learning model for house price prediction
- FastAPI backend for API development
- Docker support for containerization
- Logging for tracking API usage
- Environment variable support (.env file)

---

## 🧠 Tech Stack

- Python
- FastAPI
- Pandas
- Joblib
- Scikit-learn (if used in model training)
- Docker
- Uvicorn

# 🏠 House Price Prediction (Dockerized)

## 📌 Overview
This project predicts house prices using Machine Learning.  
The model is wrapped in a FastAPI/Flask API and fully containerized using Docker.

---

## ⚙️ Tech Stack
- Python 🐍
- Pandas & NumPy
- Scikit-learn
- FastAPI / Flask
- Docker 🐳


## 🧠 Model Workflow
- Data Cleaning
- EDA (Exploratory Data Analysis)
- Feature Engineering
- Model Training (Linear Regression / Random Forest)
- Model Evaluation
- Model Saving (.pkl file)



---
## 🐳 Run with Docker

### 1️⃣ Build Docker Image

```bash
docker build -t house-price-app .
```

### 2️⃣ Run Container

```bash
docker run -p 8000:8000 house-price-app
```

