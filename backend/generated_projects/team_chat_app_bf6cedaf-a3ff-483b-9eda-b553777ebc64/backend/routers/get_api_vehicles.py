
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/vehicles")
def handle_get_api_vehicles():
    return {"message": "List vehicles records", "route": "/api/vehicles"}
