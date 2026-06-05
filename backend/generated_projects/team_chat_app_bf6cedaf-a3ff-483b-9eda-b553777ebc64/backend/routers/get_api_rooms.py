
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/rooms")
def handle_get_api_rooms():
    return {"message": "List rooms records", "route": "/api/rooms"}
