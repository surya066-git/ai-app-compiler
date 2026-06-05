
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/agents")
def handle_post_api_agents():
    return {"message": "Create a agents record", "route": "/api/agents"}
