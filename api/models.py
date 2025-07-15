# db/models.py
from sqlalchemy import Column, Integer, String, DateTime, Text, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TelegramChannelORM(Base):
    __tablename__ = 'stg_telegram'
    id = Column(Integer, primary_key=True, index=True)
    message_time = Column(DateTime)
    message = Column(Text)
    channel = Column(String(255))
    phone_numbers = Column(Text, nullable=True)
    business_type = Column(String(50), nullable=True)
class ObjectDetectionORM(Base):
    __tablename__ = 'stg_detectios'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    message = Column(Text)
    channel = Column(String(255))
    media_path = Column(String(255), nullable=True)
    has_media = Column(Integer, default=0)
    phone_numbers = Column(Text, nullable=True)
    business_type = Column(String(50), nullable=True)
    confidence_score = Column(Float, nullable=True)
#models for FASTAPI
# api/models.py (Pydantic models)
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# api/models.py
class TelegramChannel(BaseModel):
    id: int
    message_time: datetime
    message: Optional[str] = ""  # Changed to Optional
    channel: str
    phone_numbers: Optional[str] = ""
    business_type: Optional[str] = ""

    class Config:
        from_attributes = True

class ObjectDetection(BaseModel):
    id: int
    date: datetime
    message: Optional[str] = ""  # Changed to Optional
    channel: str
    media_path: Optional[str] = ""
    has_media: int = 0
    phone_numbers: Optional[str] = ""
    business_type: Optional[str] = ""
    confidence_score: Optional[float] = 0.0

    class Config:
        from_attributes = True