
from fastapi import APIRouter
router = APIRouter()
@router.delete("/")
def handle_users__id_():
    return {"message": "Delete a user"}
