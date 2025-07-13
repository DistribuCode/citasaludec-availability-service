from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str
    JWT_SECRET: str
    PORT: int = 4010

    class Config:
        env_file = ".env"

settings = Settings()
