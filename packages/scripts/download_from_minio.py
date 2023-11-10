async def download_from_minio(object_name: str):
    try:
        data = minio_client.get_object('data-dump', object_name)
        return data.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))