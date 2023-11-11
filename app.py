# app.py

from fastapi import FastAPI
from packages.routes import router as api_router

app = FastAPI(title="My API Gateway")

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7888)
