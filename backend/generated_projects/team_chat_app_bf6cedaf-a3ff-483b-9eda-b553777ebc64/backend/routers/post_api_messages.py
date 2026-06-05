
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/messages")
def handle_post_api_messages():
    return {"message": "Create a messages record", "route": "/api/messages"}
