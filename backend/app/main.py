import uvicorn
from fastapi import Depends, FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from app.api.api_v1.routers.articles import articles_router
from app.api.api_v1.routers.auth import auth_router
from app.api.api_v1.routers.users import users_router
from app.api.api_v1.routers.websites import websites_router
from app.core import config
from app.core.auth import get_current_active_user
from app.core.celery_app import celery_app
from app.db.session import SessionLocal

app = FastAPI(title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "https://www.nytimes.com",
    "https://nytimes.com",
]

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["*"], allow_headers=["*"]
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/task")
async def example_task():
    celery_app.send_task("app.tasks.example_task", args=["Hello World"])

    return {"message": "success"}


# Routers
app.include_router(
    users_router,
    prefix="/api/v1",
    tags=["users"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(articles_router, prefix="/api", tags=["articles"])
app.include_router(websites_router, prefix="/api", tags=["websites"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
