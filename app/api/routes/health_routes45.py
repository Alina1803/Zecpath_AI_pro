from fastapi import APIRouter
from datetime import datetime
import platform
import psutil

router = APIRouter()


@router.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": "HR Interview AI",
        "timestamp": str(datetime.now()),
    }


@router.get("/health/system")
def system_health():

    return {
        "platform": platform.system(),
        "platform_version": platform.version(),
        "processor": platform.processor(),
        "cpu_usage_percent": psutil.cpu_percent(),
        "memory_usage_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage("/").percent,
    }


@router.get("/health/api")
def api_health():

    return {
        "api_status": "running",
        "interview_engine": "active",
        "voice_pipeline": "active",
        "database": "connected",
    }
