# setup.py

from setuptools import setup, find_packages

setup(
    name="ApiGateway",
    version="0.1.0",
    author="David Cannan",
    author_email="Cdaprod@Cdaprod.dev",
    description="A FastAPI application for webhook handling",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "aiohttp", 
        "minio", 
        "openai"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
