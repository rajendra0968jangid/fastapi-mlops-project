import os
import sys
# Force Python to look in the current working directory inside Docker
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
from train_model import generate_and_train

app = FastAPI(title="FastAPI MLOps Service")

# Setup CORS middleware so your HTML file can communicate with the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = 'house_model.joblib'

# Automatically train the model on startup if it doesn't exist yet
if not os.path.exists(MODEL_PATH):
    print("Model file not found. Triggering baseline training pipeline...")
    generate_and_train()

model = joblib.load(MODEL_PATH)

# Define the incoming data schema using Pydantic
class HouseFeatures(BaseModel):
    avg_income: float
    house_age: float
    num_rooms: float

@app.post("/predict")
def predict(features: HouseFeatures):
    try:
        # Perform inference using the validated schema fields
        prediction = model.predict([[features.avg_income, features.house_age, features.num_rooms]])
        return {
            "status": "success",
            "estimated_price": round(float(prediction[0]), 2)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    # Run using uvicorn server instead of native flask development server
    uvicorn.run(app, host='0.0.0.0', port=5000)