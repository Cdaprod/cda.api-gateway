async def upload_to_minio(bucket_name: str, object_name: str, data: str):
    try:
        minio_client.put_object(bucket_name, object_name, data, len(data))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))