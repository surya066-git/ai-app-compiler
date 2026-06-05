
from fastapi import APIRouter
router = APIRouter()

@router.post("/tasks")
def handle_post_tasks():
    return {"message": "Creates a new task for the authenticated user.", "route": "/tasks"}
