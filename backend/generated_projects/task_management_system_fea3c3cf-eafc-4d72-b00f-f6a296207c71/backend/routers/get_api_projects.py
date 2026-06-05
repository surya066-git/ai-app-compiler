
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/projects")
def handle_get_api_projects():
    return {"message": "List projects records", "route": "/api/projects"}
