from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.image import ImageJob
from app.models.user import User
from app.schemas.image import ImageProcessResponse
from app.services.lama.inpaint import LaMaInpaintService
from app.services.sam2.predictor import SAM2Predictor
from app.services.storage.local_storage import LocalStorage
from app.utils.files import build_output_path, save_upload
from app.utils.image import save_png

router = APIRouter(prefix='/inpaint', tags=['inpaint'])


@router.post('/', response_model=ImageProcessResponse)
async def inpaint_image(file: UploadFile = File(...), db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    in_path = await save_upload(file)
    segmented = SAM2Predictor().segment(in_path)
    output_path = build_output_path('.png')
    segmented.save(output_path)
    img = LaMaInpaintService().inpaint(output_path)
    save_png(img, output_path)
    job = ImageJob(user_id=user.id, task_type='inpaint', input_path=in_path, output_path=output_path, model_used='SAM2+LaMa', status='completed')
    db.add(job)
    db.commit()
    db.refresh(job)
    return ImageProcessResponse(job_id=job.id, status='completed', output_url=LocalStorage.to_url(output_path), detail='Inpainting complete')
