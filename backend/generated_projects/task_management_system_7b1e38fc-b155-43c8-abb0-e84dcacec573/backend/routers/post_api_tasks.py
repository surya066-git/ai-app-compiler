
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/tasks")
def handle_post_api_tasks():
    return {"message": "Create a tasks record", "route": "/api/tasks"}
