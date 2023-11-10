# utils.py

import aiohttp
from fastapi import HTTPException
from minio import Minio
import os
import openai
from .config import get_minio_client

minio_client = get_minio_client()

async def download_from_minio(object_name: str):
    try:
        data = minio_client.get_object('data-dump', object_name)
        return data.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def process_with_openai(data: bytes):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.openai.com/v1/engines/davinci/completions",
                headers={"Authorization": f"Bearer {openai.api_key}"},
                json={"prompt": data.decode('utf-8'), "max_tokens": 1024}
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    return result['choices'][0]['text'].strip()
                else:
                    raise HTTPException(status_code=response.status, detail="Error from OpenAI API")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def upload_to_minio(bucket_name: str, object_name: str, data: str):
    try:
        minio_client.put_object(bucket_name, object_name, data, len(data))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def process_text_data(object_name: str):
    try:
        data = await download_from_minio(object_name)
        cleaned_data = await process_with_openai(data)
        await upload_to_minio('objects', f'cleaned_{object_name}', cleaned_data)
        return {"object_name": object_name, "status": "processed"}
    except Exception as e:
        return {"object_name": object_name, "status": "error", "error": str(e)}
