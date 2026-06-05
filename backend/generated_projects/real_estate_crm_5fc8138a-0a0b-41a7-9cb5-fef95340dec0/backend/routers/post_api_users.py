
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/users")
def handle_post_api_users():
    return {"message": "Create a users record", "route": "/api/users"}
