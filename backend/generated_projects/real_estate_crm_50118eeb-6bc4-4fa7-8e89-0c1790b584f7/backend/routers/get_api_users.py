
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/users")
def handle_get_api_users():
    return {"message": "List users records", "route": "/api/users"}
