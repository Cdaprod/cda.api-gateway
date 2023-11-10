async def process_text_data(object_name: str):
    try:
        data = await download_from_minio(object_name)
        cleaned_data = await process_with_openai(data)
        await upload_to_minio('objects', f'cleaned_{object_name}', cleaned_data)
        return {"object_name": object_name, "status": "processed"}
    except Exception as e:
        return {"object_name": object_name, "status": "error", "error": str(e)}
