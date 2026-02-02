from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict
from app.models.interview import InterviewStatus


class InterviewStart(BaseModel):
    resume_id: int


class InterviewResponse(BaseModel):
    id: int
    user_id: int
    resume_id: int
    session_id: str
    status: InterviewStatus
    created_at: datetime
    
    class Config:
        from_attributes = True


class InterviewQuestion(BaseModel):
    question_id: int
    question: str
    topic: str


class InterviewQuestions(BaseModel):
    interview_id: int
    session_id: str
    questions: List[InterviewQuestion]


class AnswerSubmit(BaseModel):
    session_id: str
    question_id: int
    answer: str


class AnswerFeedback(BaseModel):
    question_id: int
    question: str
    answer: str
    feedback: str
    score: int


class InterviewReport(BaseModel):
    interview_id: int
    session_id: str
    status: InterviewStatus
    overall_score: int
    answers_feedback: List[AnswerFeedback]
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    
    class Config:
        from_attributes = True