# models.py

from pydantic import BaseModel
from typing import List

# Define Pydantic models for the incoming webhook data

class S3Object(BaseModel):
    key: str

class S3Bucket(BaseModel):
    name: str

class S3Info(BaseModel):
    bucket: S3Bucket
    object: S3Object

class Record(BaseModel):
    s3: S3Info

class Notification(BaseModel):
    Records: List[Record]
