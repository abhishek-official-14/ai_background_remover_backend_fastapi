# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from app.api.router import api_router
# from app.core.config import get_settings
# from app.core.database import Base, engine
# from app.utils.files import ensure_dirs

# settings = get_settings()
# app = FastAPI(title=settings.PROJECT_NAME)

# Base.metadata.create_all(bind=engine)
# ensure_dirs()
# app.mount('/static', StaticFiles(directory=settings.OUTPUT_DIR), name='static')
# app.include_router(api_router, prefix=settings.API_V1_PREFIX)



from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import get_settings
from app.core.database import Base, engine
from app.utils.files import ensure_dirs

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME
)

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- DB ----------------
Base.metadata.create_all(bind=engine)

# ---------------- Folders ----------------
ensure_dirs()

# ---------------- Static ----------------
app.mount(
    "/static",
    StaticFiles(directory=settings.OUTPUT_DIR),
    name="static"
)

# ---------------- Routes ----------------
app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX
)