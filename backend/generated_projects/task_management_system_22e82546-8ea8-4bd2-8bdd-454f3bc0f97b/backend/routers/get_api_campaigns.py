
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/campaigns")
def handle_get_api_campaigns():
    return {"message": "List campaigns records", "route": "/api/campaigns"}
