import boto3
from botocore.exceptions import NoCredentialsError

def upload_csv_to_s3(file_name, bucket_name, object_name=None):
    """
    Uploads a CSV file to an AWS S3 bucket.
    
    :param file_name: Path to the local file to upload
    :param bucket_name: Name of the target S3 bucket
    :param object_name: S3 object name (destination path inside the bucket). 
                        If not specified, file_name is used.
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Initialize the boto3 S3 client
    # It automatically picks up the credentials you set in 'aws configure'
    s3_client = boto3.client('s3')

    try:
        print(f"Uploading '{file_name}' to bucket '{bucket_name}'...")
        
        # Upload the file
        s3_client.upload_file(file_name, bucket_name, object_name)
        
        print("Upload successful!")
        return True
        
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found locally.")
        return False
    except NoCredentialsError:
        print("AWS credentials not found. Please run 'aws configure' in your terminal.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# --- Execution ---
if __name__ == "__main__":
    # Change these variables to match your local setup
    LOCAL_CSV_FILE = "file.csv"
    AWS_BUCKET_NAME = "amzn-s3-bucket-sagemaker-rajendra"
    S3_DESTINATION_NAME = "uploads/file.csv" # Optional: nested folder structure

    upload_csv_to_s3(LOCAL_CSV_FILE, AWS_BUCKET_NAME, S3_DESTINATION_NAME)