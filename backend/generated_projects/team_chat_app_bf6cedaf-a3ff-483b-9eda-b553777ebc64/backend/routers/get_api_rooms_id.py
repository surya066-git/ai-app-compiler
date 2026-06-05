
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/rooms/{id}")
def handle_get_api_rooms_id(id: int):
    return {"message": "Fetch one rooms record", "route": "/api/rooms/{id}"}
