
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/projects")
def handle_post_api_projects():
    return {"message": "Create a projects record", "route": "/api/projects"}
