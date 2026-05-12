from fastapi import APIRouter
from app.api.routes import auth, background, health, inpaint, upscale

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(background.router)
api_router.include_router(upscale.router)
api_router.include_router(inpaint.router)
