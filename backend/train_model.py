import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def generate_and_train():
    print("Generating training data...")
    np.random.seed(42)
    n_samples = 100
    
    avg_income = np.random.randint(40000, 120000, n_samples)
    house_age = np.random.uniform(1, 15, n_samples)
    num_rooms = np.random.randint(3, 9, n_samples)
    
    price = (avg_income * 4.5) + (house_age * 12000) + (num_rooms * 25000) + np.random.normal(0, 10000, n_samples)
    
    df = pd.DataFrame({
        'avg_income': avg_income,
        'house_age': house_age,
        'num_rooms': num_rooms,
        'price': price
    })
    
    X = df[['avg_income', 'house_age', 'num_rooms']]
    y = df['price']
    
    print("Training Linear Regression model...")
    model = LinearRegression()
    model.fit(X, y)
    
    joblib.dump(model, 'house_model.joblib')
    print("Model successfully trained and saved as 'house_model.joblib'")

if __name__ == "__main__":
    generate_and_train()