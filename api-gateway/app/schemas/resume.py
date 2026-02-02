from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class ResumeUpload(BaseModel):
    pass  # File will be uploaded via multipart form


class ResumeResponse(BaseModel):
    id: int
    user_id: int
    filename: str
    skills: Optional[List[str]] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


class ResumeDetail(ResumeResponse):
    extracted_text: Optional[str] = None
    vector_id: Optional[str] = None
    updated_at: Optional[datetime] = None