
from fastapi import APIRouter
router = APIRouter()
@router.post("/")
def handle_users():
    return {"message": "Create a new user"}
