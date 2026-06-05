
from fastapi import APIRouter
router = APIRouter()

@router.delete("/tasks/{id}")
def handle_delete_tasks_id(id: int):
    return {"message": "Deletes a task by ID for the authenticated user.", "route": "/tasks/{id}"}
