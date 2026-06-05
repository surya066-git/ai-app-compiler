
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/rooms")
def handle_post_api_rooms():
    return {"message": "Create a rooms record", "route": "/api/rooms"}
