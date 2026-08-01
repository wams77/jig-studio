from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "JIG Studio"

    DEBUG: bool = False

    GROQ_API_KEY: str = ""

    PEXELS_API_KEY: str = ""

    FACEBOOK_ACCESS_TOKEN: str = ""

    FACEBOOK_PAGE_ID: str = ""

    SABDA_BASE_URL: str = "https://alkitab.sabda.org"

    LOG_LEVEL: str = "INFO"

    DATABASE_URL: str = "sqlite:///database/jig.db"

    OUTPUT_DIR: str = "output"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
