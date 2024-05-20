from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    OPENAI_API_KEY: str


def get_settings() -> Settings:
    return Settings()  # type: ignore


settings = get_settings()
