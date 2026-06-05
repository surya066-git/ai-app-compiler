
from fastapi import APIRouter
router = APIRouter()

@router.post("/login")
def handle_post_login():
    return {"message": "Authenticates a user and returns an access token.", "route": "/login"}
