
from fastapi import APIRouter
router = APIRouter()

@router.post("/register")
def handle_post_register():
    return {"message": "Registers a new user.", "route": "/register"}
