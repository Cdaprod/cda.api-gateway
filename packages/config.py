# packages/config.py

import os
from minio import Minio
import openai

# Initialize the MinIO client
def get_minio_client():
    return Minio(
        os.getenv('MINIO_ENDPOINT'),
        access_key=os.getenv('MINIO_ACCESS_KEY'),
        secret_key=os.getenv('MINIO_SECRET_KEY'),
        secure=bool(os.getenv('MINIO_SECURE', 'False') == 'False')
    )

# Function to retrieve OpenAI API key
def get_openai_api_key():
    return os.getenv('OPENAI_API_KEY')

# Assign OpenAI API key
openai.api_key = get_openai_api_key()
