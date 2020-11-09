import uvicorn
from functools import lru_cache
from fastapi import Depends, FastAPI
from config import app_config
from routers import auth_route, users_route, files_request_route
from db.database import SessionLocal, engine
from models import file_requests_models, users_models
from sqlalchemy.orm import Session
from models import users_models
from schemas import user_schemas
from services import user_service
from typing import List

users_models.Base.metadata.create_all(bind=engine)
file_requests_models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.include_router(
    auth_route.router,
    prefix="/auth",
    responses={404: {"description": "Not found"}},

)

app.include_router(
    users_route.router,
    prefix="/users"
)

app.include_router(
    files_request_route.router,
    prefix="/requests"
)


@lru_cache()
def get_settings():
    return app_config.settings


@app.get("/info")
async def info(settings: app_config.Settings = Depends(get_settings), db: Session = Depends(get_db)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "max_logging_attempts": settings.max_logging_attempts,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, debug=True)
