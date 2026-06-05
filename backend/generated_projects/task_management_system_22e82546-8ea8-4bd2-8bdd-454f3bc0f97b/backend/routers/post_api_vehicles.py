
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/vehicles")
def handle_post_api_vehicles():
    return {"message": "Create a vehicles record", "route": "/api/vehicles"}
