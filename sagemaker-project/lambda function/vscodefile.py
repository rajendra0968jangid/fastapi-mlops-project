import json
import boto3

runtime = boto3.client("sagemaker-runtime")

ENDPOINT_NAME = "sagemaker-scikit-learn-2026-07-14-10-14-42-660"

def lambda_handler(event, context):

    body = json.loads(event["body"])

    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType="application/json",
        Body=json.dumps(body)
    )

    prediction = response["Body"].read().decode()

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": prediction
    }
    
