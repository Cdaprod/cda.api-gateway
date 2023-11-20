# File: routers.py in the same package directory

from fastapi import APIRouter
from .models import Notification  # Assuming models.py contains the Notification model
from .utils import process_text_data  # Assuming utils.py contains the process_text_data function

router = APIRouter()


@router.get("/health")
def health_check():
    # Implement your health check logic here.
    # For a simple health check, just return a positive HTTP status.
    return {"status": "healthy"}

@router.get("/")
async def root():
    return {"message": "Welcome to my API Gateway"}

@router.post("/minio-events/")
async def handle_minio_event(request: Request):
    event_data = await request.json()
    # Process the event_data, for example, logging it or triggering another process
    return {"message": "Event received"}
    
@router.post("/minio-webhook/")
async def handle_webhook(notification: Notification):
    errors = []
    results = []
    for record in notification.Records:
        if record.s3.bucket.name == 'data-dump':
            result = await process_text_data(record.s3.object.key)
            results.append(result)
    return {"message": "Webhook processed", "results": results, "errors": errors} 