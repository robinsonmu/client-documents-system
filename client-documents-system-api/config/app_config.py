from dotenv import load_dotenv
from pydantic import BaseSettings
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str
    max_logging_attemps: int = 10
    algorithm: str
    secret_key: str
    access_token_expire_minutes: int
    origins = [
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:8000",
    ]

    def add_cors_middleware(self, app):
        app.add_middleware(
            CORSMiddleware,
            allow_origins=self.origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


settings = Settings()
