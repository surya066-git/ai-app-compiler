
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/tasks")
def handle_get_api_tasks():
    return {"message": "List tasks records", "route": "/api/tasks"}
