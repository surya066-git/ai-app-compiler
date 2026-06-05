
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/messages")
def handle_get_api_messages():
    return {"message": "List messages records", "route": "/api/messages"}
