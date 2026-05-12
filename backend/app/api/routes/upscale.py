from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.image import ImageJob
from app.models.user import User
from app.schemas.image import ImageProcessResponse
from app.services.storage.local_storage import LocalStorage
from app.services.upscale.realesrgan_service import RealESRGANService
from app.utils.files import build_output_path, save_upload
from app.utils.image import save_png

router = APIRouter(prefix='/upscale', tags=['upscale'])


@router.post('/', response_model=ImageProcessResponse)
async def upscale_image(file: UploadFile = File(...), scale: int = 2, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    in_path = await save_upload(file)
    output_path = build_output_path('.png')
    img = RealESRGANService().upscale(in_path, scale=scale)
    save_png(img, output_path)
    job = ImageJob(user_id=user.id, task_type='upscale', input_path=in_path, output_path=output_path, model_used='Real-ESRGAN', status='completed')
    db.add(job)
    db.commit()
    db.refresh(job)
    return ImageProcessResponse(job_id=job.id, status='completed', output_url=LocalStorage.to_url(output_path), detail='Image upscaled')
