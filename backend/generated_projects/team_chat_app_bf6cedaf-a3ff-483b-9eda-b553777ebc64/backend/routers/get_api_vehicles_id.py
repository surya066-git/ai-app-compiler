
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/vehicles/{id}")
def handle_get_api_vehicles_id(id: int):
    return {"message": "Fetch one vehicles record", "route": "/api/vehicles/{id}"}
