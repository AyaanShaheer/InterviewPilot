from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Enum as SQLEnum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base
import enum


class InterviewStatus(str, enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Interview(Base):
    __tablename__ = "interviews"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    resume_id = Column(Integer, ForeignKey("resumes.id"), nullable=False)
    session_id = Column(String, unique=True, index=True, nullable=False)
    status = Column(SQLEnum(InterviewStatus), default=InterviewStatus.PENDING)
    questions = Column(JSON, nullable=True)  # List of generated questions
    answers = Column(JSON, nullable=True)    # List of user answers
    feedback = Column(JSON, nullable=True)   # AI-generated feedback
    score = Column(Integer, nullable=True)   # Overall score
    started_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("User", backref="interviews")
    resume = relationship("Resume", backref="interviews")
    
    def __repr__(self):
        return f"<Interview {self.session_id}>"