from fastapi import FastAPI
from interview_project.routes import router as api_router

app = FastAPI(title="OTP Auth Service")

app.include_router(api_router, prefix="/api/v1")