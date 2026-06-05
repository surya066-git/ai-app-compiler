
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/messages/{id}")
def handle_get_api_messages_id(id: int):
    return {"message": "Fetch one messages record", "route": "/api/messages/{id}"}
