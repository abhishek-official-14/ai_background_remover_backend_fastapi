from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from app.core.database import Base


class ImageJob(Base):
    __tablename__ = 'image_jobs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    task_type = Column(String(50), nullable=False)
    input_path = Column(Text, nullable=False)
    output_path = Column(Text, nullable=True)
    model_used = Column(String(100), nullable=True)
    status = Column(String(50), default='queued')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
