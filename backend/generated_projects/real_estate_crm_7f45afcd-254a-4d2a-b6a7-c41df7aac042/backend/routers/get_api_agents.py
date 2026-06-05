
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/agents")
def handle_get_api_agents():
    return {"message": "List agents records", "route": "/api/agents"}
