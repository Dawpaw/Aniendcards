import os
import boto3

# Constants
PASETO_KEY:str = os.environ.get("PASETO_KEY", "changeme")

ACCESS_TOKEN_EXPIRE_MINUTES: int = 15

IMAGES_TEMP_FOLDER = "./tmp/images/"
IMAGES_MAX_ALLOWED_SIZE = 5 # MB

R2_ENDPOINT_URL = os.environ.get("R2_ENDPOINT_URL") 
R2_ACCESS_KEY_ID = os.environ.get("R2_ACCESS_KEY_ID") 
R2_SECRET_ACCESS_KEY = os.environ.get("R2_SECRET_ACCESS_KEY") 
R2_PUBLIC_ACCESS_DOMAIN = os.environ.get("R2_PUBLIC_ACCESS_DOMAIN")
R2_BUCKET_NAME = os.environ.get("R2_BUCKET_NAME ")


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = os.environ.get("DB_PORT", "5432")
    user = os.environ.get("DB_USER", "aniendcards")
    password = os.environ.get("DB_PASSWORD", "changeme")
    db = os.environ.get("DB_NAME", "aniendcards")
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"


s3 = boto3.client(
    service_name="s3",
    endpoint_url=R2_ENDPOINT_URL,
    aws_access_key_id=R2_ACCESS_KEY_ID,
    aws_secret_access_key=R2_SECRET_ACCESS_KEY,
    region_name="auto",
)
    