
from fastapi import APIRouter
router = APIRouter()

@router.post("/login")
def handle_post_login():
    return {"message": "Login endpoint", "route": "/login"}
