
from fastapi import APIRouter
router = APIRouter()

@router.get("/tasks")
def handle_get_tasks():
    return {"message": "Retrieves all tasks for the authenticated user.", "route": "/tasks"}
