from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.image import ImageJob
from app.models.user import User
from app.schemas.image import ImageProcessResponse
from app.services.background.birefnet import BiRefNetService
from app.services.background.modnet import MODNetService
from app.services.background.rmbg import RMBGService
from app.services.storage.local_storage import LocalStorage
from app.utils.files import build_output_path, save_upload
from app.utils.image import save_png

router = APIRouter(prefix='/background', tags=['background'])


@router.post('/remove', response_model=ImageProcessResponse, summary='Remove image background using RMBG + refinements')
async def remove_background(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    in_path = await save_upload(file)
    output_path = build_output_path('.png')
    img = RMBGService().process(in_path)
    img = BiRefNetService().refine(img)
    img = MODNetService().refine_hair(img)
    save_png(img, output_path)

    job = ImageJob(user_id=user.id, task_type='background_remove', input_path=in_path, output_path=output_path, model_used='RMBG-2.0')
    db.add(job)
    db.commit()
    db.refresh(job)

    return ImageProcessResponse(job_id=job.id, status='completed', output_url=LocalStorage.to_url(output_path), detail='Background removed successfully')
