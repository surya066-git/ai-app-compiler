
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/properties")
def handle_get_api_properties():
    return {"message": "List properties records", "route": "/api/properties"}
