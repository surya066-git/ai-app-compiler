
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/campaigns/{id}")
def handle_get_api_campaigns_id(id: int):
    return {"message": "Fetch one campaigns record", "route": "/api/campaigns/{id}"}
