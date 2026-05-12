from functools import lru_cache
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / '.env', env_file_encoding='utf-8', extra='ignore')

    PROJECT_NAME: str = 'AI Background Remover API'
    API_V1_PREFIX: str = '/api/v1'

    SECRET_KEY: str = Field(default='change_me', min_length=16)
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    DATABASE_URL: str = 'postgresql+psycopg2://postgres:postgres@localhost:5432/ai_bg_remover'
    REDIS_URL: str = 'redis://localhost:6379/0'

    UPLOAD_DIR: str = str(BASE_DIR / 'uploads')
    OUTPUT_DIR: str = str(BASE_DIR / 'outputs')
    MAX_FILE_SIZE_MB: int = 25

    DEVICE: str = 'cuda'
    RMBG_MODEL: str = 'briaai/RMBG-2.0'


@lru_cache
def get_settings() -> Settings:
    return Settings()
