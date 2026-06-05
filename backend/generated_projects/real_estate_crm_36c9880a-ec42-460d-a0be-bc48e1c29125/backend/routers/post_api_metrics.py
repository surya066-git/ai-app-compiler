
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/metrics")
def handle_post_api_metrics():
    return {"message": "Create a metrics record", "route": "/api/metrics"}
