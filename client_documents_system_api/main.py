import uvicorn
from functools import lru_cache
from fastapi import Depends, FastAPI
from config import app_config
from routers import auth
from db.database import SessionLocal, engine
from models import file_requests, users

file_requests.Base.metadata.create_all(bind=engine)
users.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(
    auth.router,
    prefix="/auth",
    responses={404: {"description": "Not found"}},
)


@lru_cache()
def get_settings():
    return app_config.settings


@app.get("/info")
async def info(settings: app_config.Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "max_logging_attemps": settings.max_logging_attemps,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
