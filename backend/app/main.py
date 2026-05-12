from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.router import api_router
from app.core.config import get_settings
from app.core.database import Base, engine
from app.utils.files import ensure_dirs

settings = get_settings()
app = FastAPI(title=settings.PROJECT_NAME)

Base.metadata.create_all(bind=engine)
ensure_dirs()
app.mount('/static', StaticFiles(directory=settings.OUTPUT_DIR), name='static')
app.include_router(api_router, prefix=settings.API_V1_PREFIX)
