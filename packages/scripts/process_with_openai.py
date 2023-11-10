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
