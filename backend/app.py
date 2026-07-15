import os
import sys
import requests
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

# MODEL_PATH = 'model (1).joblib' # model name

# # Automatically train the model on startup if it doesn't exist yet
# if not os.path.exists(MODEL_PATH):
#     print("Model file not found. Triggering baseline training pipeline...")
#     generate_and_train()

# model = joblib.load(MODEL_PATH)


# ==========================
# API Gateway URL
# ==========================

API_GATEWAY_URL = "https://a34n5jhwbh.execute-api.us-east-1.amazonaws.com/predict"

# ==========================
# Request Model
# ==========================

class Student(BaseModel):
    maths: float
    english: float


@app.post("/predict")
def predict(student: Student):

    payload = student.model_dump()

    try:

        response = requests.post(
            API_GATEWAY_URL,
            json=payload,
            headers={
                "Content-Type": "application/json"
            },
            timeout=30
        )

        response.raise_for_status()

        prediction = response.json()

        return {
            "status": "success",
            "prediction": prediction
        }

    except requests.exceptions.HTTPError as e:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )

    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# Define the incoming data schema using Pydantic
# class HouseFeatures(BaseModel): # 
#     maths: float
#     english: float
#     # num_rooms: float
    
# @app.post("/predict")
# def predict(features: HouseFeatures):
#     try:
#         # Perform inference using the validated schema fields
#         prediction = model.predict([[features.maths, features.english]])
#         return {
#             "status": "success",
#             "estimated_marks": round(float(prediction[0]), 2)
#         }
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    # Run using uvicorn server instead of native flask development server
    uvicorn.run(app, host='0.0.0.0', port=5000)