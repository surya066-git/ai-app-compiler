
from fastapi import APIRouter
router = APIRouter()
@router.post("/")
def handle_vehicles():
    return {"message": "Create a new vehicle"}
