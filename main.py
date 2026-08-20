from fastapi import FastAPI
from database import engine
from models import Base

app = FastAPI(
    title="AI Growth Agent",
    description="AI-powered Growth and Agentic Commerce Platform",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "AI Growth Agent is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
