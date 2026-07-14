import json
import joblib
import numpy as np


def model_fn(model_dir):
    model = joblib.load(f"{model_dir}/model.joblib")
    return model


def input_fn(request_body, request_content_type):

    if request_content_type == "application/json":

        data = json.loads(request_body)

        # If JSON is a dictionary
        if isinstance(data, dict):
            features = [[
                data["maths"],
                data["english"]
            ]]

        # If JSON is already a list
        elif isinstance(data, list):
            features = data

        else:
            raise ValueError("Invalid JSON format")

        return np.array(features)

    raise ValueError("Unsupported content type")


def predict_fn(input_data, model):
    prediction = model.predict(input_data)
    return prediction


def output_fn(prediction, accept):

    return json.dumps({
        "prediction": prediction.tolist()
    })