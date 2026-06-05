
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/metrics")
def handle_get_api_metrics():
    return {"message": "List metrics records", "route": "/api/metrics"}
