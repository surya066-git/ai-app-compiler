
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/properties")
def handle_post_api_properties():
    return {"message": "Create a properties record", "route": "/api/properties"}
