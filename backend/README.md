# AI Background Remover Backend (FastAPI)

## Features
- JWT Auth (register/login)
- Background removal with RMBG-2.0 default pipeline
- BiRefNet + MODNet refinement stages
- SAM2 segmentation + LaMa inpainting endpoint
- Real-ESRGAN-style upscale endpoint
- PostgreSQL models + Alembic migration
- Redis/Celery worker
- Local upload/output storage + static serving

## Installation
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env .env.local
```

## Local setup
```bash
# start PostgreSQL + Redis separately
alembic upgrade head
python run.py
```

## Celery worker
```bash
celery -A app.tasks.worker.celery_app worker --loglevel=info
```

## Docker
```bash
cd backend
docker build -t ai-bg-remover-backend .
docker run -p 8000:8000 --env-file .env ai-bg-remover-backend
```

## API examples
```bash
curl -X POST http://localhost:8000/api/v1/auth/register -H "Content-Type: application/json" -d '{"email":"test@example.com","password":"pass123456","full_name":"Test User"}'

curl -X POST http://localhost:8000/api/v1/auth/login -H "Content-Type: application/json" -d '{"email":"test@example.com","password":"pass123456"}'

curl -X POST http://localhost:8000/api/v1/background/remove -H "Authorization: Bearer <TOKEN>" -F "file=@input.png"

curl -X POST "http://localhost:8000/api/v1/upscale/?scale=2" -H "Authorization: Bearer <TOKEN>" -F "file=@input.png"

curl -X POST http://localhost:8000/api/v1/inpaint/ -H "Authorization: Bearer <TOKEN>" -F "file=@input.png"
```

## Recommended GPU
- Minimum: NVIDIA T4 (16GB VRAM)
- Recommended: NVIDIA A10/A100 (24GB+ VRAM)
- CPU fallback works for small images but is significantly slower.
