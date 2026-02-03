from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db
from app.utils.redis_client import get_redis
import httpx

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
def health_check():
    """Basic health check"""
    return {
        "status": "healthy",
        "service": "InterviewPilot API Gateway"
    }


@router.get("/db")
def database_health(db: Session = Depends(get_db)):
    """Check database connectivity"""
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }


@router.get("/redis")
def redis_health():
    """Check Redis connectivity"""
    try:
        redis_client = get_redis()
        redis_client.ping()
        return {
            "status": "healthy",
            "redis": "connected"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "redis": "disconnected",
            "error": str(e)
        }


@router.get("/full")
def full_health_check(db: Session = Depends(get_db)):
    """Comprehensive health check for all services"""
    health_status = {
        "api": "healthy",
        "database": "unknown",
        "redis": "unknown",
        "go_service": "unknown"
    }
    
    # Check database
    try:
        db.execute(text("SELECT 1"))
        health_status["database"] = "healthy"
    except Exception:
        health_status["database"] = "unhealthy"
    
    # Check Redis
    try:
        redis_client = get_redis()
        redis_client.ping()
        health_status["redis"] = "healthy"
    except Exception:
        health_status["redis"] = "unhealthy"
    
    # Check Go service (we'll implement this later)
    health_status["go_service"] = "pending"
    
    overall_status = "healthy" if all(
        v == "healthy" or v == "pending" for v in health_status.values()
    ) else "unhealthy"
    
    return {
        "status": overall_status,
        "services": health_status
    }