# Flask MLOps Project

A simple Flask-based Machine Learning API project using Docker and Docker Compose.

## Project Structure

```bash
FLASK-MLOPS-PROJECT/
│
├── backend/
│   ├── app.py
│   ├── train_model.py
│   ├── house_model.joblib
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
│
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   └── .dockerignore
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

# Features

* Flask REST API
* Machine Learning Model Integration
* Docker Support
* Docker Compose Support
* Frontend + Backend Separation
* Model Training Script
* Joblib Model Storage

---

# Technologies Used

* Python 3.11
* Flask
* Scikit-learn
* NumPy
* Pandas
* Docker
* Docker Compose
* HTML

---

# Backend Setup

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Flask App

```bash
python app.py
```

Backend runs on:

```bash
http://localhost:5000
```

---

# Docker Setup

## Build Containers

```bash
docker compose build
```

## Run Containers

```bash
docker compose up
```

## Stop Containers

```bash
docker compose down
```

---

# Docker Compose Services

| Service           | Port |
| ----------------- | ---- |
| Backend Flask API | 5000 |
| Frontend HTML UI  | 8080 |

---

# API Example

## Prediction Endpoint

```http
POST /predict
```

## Sample Request

```json
{
  "feature": 10
}
```

## Sample Response

```json
{
  "prediction": 250000
}
```

---

# Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Model Training
4. Model Saving using Joblib
5. Flask API Integration
6. Docker Containerization
7. Deployment

---

# Training Model

Run:

```bash
python train_model.py
```

This creates:

```bash
house_model.joblib
```

---

# Frontend

Frontend is a simple HTML UI served using Docker.

Open:

```bash
http://localhost:8080
```

---

# Useful Docker Commands

## Check Running Containers

```bash
docker ps
```

## Rebuild Containers

```bash
docker compose build --no-cache
```

## View Logs

```bash
docker compose logs
```

---

# Future Improvements

* Add React Frontend
* Add Database Support
* Add CI/CD Pipeline
* Deploy on AWS
* Add Model Monitoring
* Add Authentication

---

# Author

Aicodecenter
