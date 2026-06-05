
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/tasks/{id}")
def handle_get_api_tasks_id(id: int):
    return {"message": "Fetch one tasks record", "route": "/api/tasks/{id}"}
