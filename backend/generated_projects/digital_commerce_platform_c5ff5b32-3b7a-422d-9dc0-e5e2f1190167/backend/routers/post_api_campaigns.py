
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/campaigns")
def handle_post_api_campaigns():
    return {"message": "Create a campaigns record", "route": "/api/campaigns"}
