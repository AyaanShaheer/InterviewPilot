import redis 
from app.config import settings

# Redis client instance
redis_client = redis.from_url(
    settings.REDIS_URL,
    decode_responses=True,
    socket_connect_timeout=5,
    socker_keepalive=True
)

def get_redis():
    """Get Redis Client instance"""
    return redis_client


def cache_set(key: str, value: str, expiration: int = 3600):
    """Set cache with expiration"""
    redis_client.setex(key, expiration, value)

def cache_get(key: str) -> str:
    """Get cached value"""
    return redis_client.get(key)

def cache_delete(key: str):
    """Delete cached value"""
    redis_client.delete(key)