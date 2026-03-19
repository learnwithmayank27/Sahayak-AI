from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Shayak AI"
    DEBUG: bool = True

    GEMINI_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    CLAUDE_API_KEY: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
