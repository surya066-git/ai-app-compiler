
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/agents/{id}")
def handle_get_api_agents_id(id: int):
    return {"message": "Fetch one agents record", "route": "/api/agents/{id}"}
