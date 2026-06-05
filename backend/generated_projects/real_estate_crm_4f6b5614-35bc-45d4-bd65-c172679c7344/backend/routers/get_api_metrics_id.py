
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/metrics/{id}")
def handle_get_api_metrics_id(id: int):
    return {"message": "Fetch one metrics record", "route": "/api/metrics/{id}"}
