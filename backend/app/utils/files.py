from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile
from app.core.config import get_settings


settings = get_settings()


def ensure_dirs() -> None:
    Path(settings.UPLOAD_DIR).mkdir(parents=True, exist_ok=True)
    Path(settings.OUTPUT_DIR).mkdir(parents=True, exist_ok=True)


async def save_upload(file: UploadFile) -> str:
    ensure_dirs()
    suffix = Path(file.filename or 'upload.bin').suffix
    filename = f'{uuid4().hex}{suffix}'
    path = Path(settings.UPLOAD_DIR) / filename
    content = await file.read()
    path.write_bytes(content)
    return str(path)


def build_output_path(ext: str = '.png') -> str:
    ensure_dirs()
    return str(Path(settings.OUTPUT_DIR) / f'{uuid4().hex}{ext}')
