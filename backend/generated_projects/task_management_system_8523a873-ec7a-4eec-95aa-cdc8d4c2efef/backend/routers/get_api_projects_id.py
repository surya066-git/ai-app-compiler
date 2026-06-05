
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/projects/{id}")
def handle_get_api_projects_id(id: int):
    return {"message": "Fetch one projects record", "route": "/api/projects/{id}"}
