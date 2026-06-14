

from backend.app.api.v1.router import api_router
from backend.app.core.config import settings
from backend.app.api.routes import auth
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

app.include_router(
    api_router,
    prefix="/api/v1"
)


@app.get("/")
def root():
    return {
        "message": "Enterprise RAG Platform Running"
    }


from backend.app.api.routes.chat import (
    router as chat_router
)

app.include_router(
    auth.router
)

app.include_router(
    chat_router,
    prefix="/chat",
    tags=["chat"]
)