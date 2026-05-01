

from fastapi import FastAPI, Header, HTTPException
import joblib
import logging
import pandas as pd
from dotenv import load_dotenv
import os

# =========================
# Load ENV
# =========================
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = FastAPI()

# =========================
# Logging setup
# =========================
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,#DEBUG < INFO < WARNING < ERROR < CRITICAL this is say start from info debug not show i mean we can use 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# Load model + columns
# =========================
model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

logging.info("Model and columns loaded successfully")

# =========================
# Home route
# =========================
@app.get("/")
def home():
    return {"message": "House Price Prediction API is running 🚀"}

# =========================
# Prediction API (with monitoring)
# =========================
@app.post("/predict")
def predict(data: dict, x_api_key: str = Header(None)):

    # 🔐 API Key check
    if x_api_key != API_KEY:
        logging.warning("Unauthorized access attempt")
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        # Input values
        area = data["area"]
        bedrooms = data["bedrooms"]
        bathrooms = data["bathrooms"]
        location = data["location"]

        # Base input
        input_data = {
            "area": area,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms
        }

        # Add missing columns
        for col in columns:
            if col not in input_data:
                input_data[col] = 0

        # Encode location
        loc_col = f"location_{location}"
        if loc_col in input_data:
            input_data[loc_col] = 1

        # Convert to DataFrame (correct ML method)
        input_df = pd.DataFrame([input_data])
        input_df = input_df.reindex(columns=columns, fill_value=0)

        # Prediction
        prediction = model.predict(input_df)[0]

        # =========================
        # Monitoring (SAVE DATA)
        # =========================
        #1.
        log_data = {
            "area": area,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "location": location,
            "prediction": prediction
        }

        # If actual value provided → calculate error this is optionel
        if "actual_price" in data:
            actual = data["actual_price"]
            error = abs(actual - prediction)
            log_data["actual_price"] = actual #this is rigistor in log fill
            log_data["error"] = error#also this rigistor in log fill
        else:
            log_data["actual_price"] = None
            log_data["error"] = None

        # Save to CSV (monitoring file)
        df = pd.DataFrame([log_data])
        df.to_csv("prediction_logs.csv", mode="a", header=False, index=False)
                              #OR USE OLD DATA SET
         #import pandas as pd 
        # new_data = pd.DataFrame([log_data]) this manuuly add the new ender  data in same data set
        # new_data["price"] = prediction
        # new_data.to_csv("house_price_dataset.csv", mode="a", header=False, index=False) #this new fill

        # Log info
        logging.info(f"Monitoring Data: {log_data}") #this is  add in log fill
                              #log fill save like this  INFO - Monitoring Data: {'area': 1200, 'bedrooms': 2, 'bathrooms': 2, 'location': 'urban', 'prediction': np.float64(48902.4299232634), 'actual_price': None, 'error': None}
        return {
            "predicted_price": prediction,
            "error": log_data["error"]
        }

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"error": "Prediction failed"}
    
#uvicorn api:app --reload  this run in terminal

