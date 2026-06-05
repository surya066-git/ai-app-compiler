
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/users/{id}")
def handle_get_api_users_id(id: int):
    return {"message": "Fetch one users record", "route": "/api/users/{id}"}
