#expose channels
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.db_connection import get_db
from api.models import TelegramChannel, ObjectDetection, TelegramChannelORM, ObjectDetectionORM
from typing import List
router = APIRouter()
@router.get("/channels", response_model=List[TelegramChannel])
def read_channels(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of Telegram channels with pagination.
    """
    channels = db.query(TelegramChannelORM).offset(skip).limit(limit).all()
    return channels
@router.get("/object-detection", response_model=List[ObjectDetection])
def read_object_detection(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of object detection records with pagination.
    """
    detections = db.query(ObjectDetectionORM).offset(skip).limit(limit).all()
    return detections

