
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/properties/{id}")
def handle_get_api_properties_id(id: int):
    return {"message": "Fetch one properties record", "route": "/api/properties/{id}"}
