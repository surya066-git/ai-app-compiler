
from fastapi import APIRouter
router = APIRouter()

@router.get("/tasks/{id}")
def handle_get_tasks_id(id: int):
    return {"message": "Retrieves a specific task by ID for the authenticated user.", "route": "/tasks/{id}"}
