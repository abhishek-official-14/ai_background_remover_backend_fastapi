from pydantic import BaseModel


class ImageProcessResponse(BaseModel):
    job_id: int
    status: str
    output_url: str | None = None
    detail: str
