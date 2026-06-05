
from fastapi import APIRouter
router = APIRouter()
@router.delete("/")
def handle_vehicles__id_():
    return {"message": "Delete a vehicle"}
