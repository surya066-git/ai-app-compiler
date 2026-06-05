
from fastapi import APIRouter
router = APIRouter()

@router.get("/contacts")
def handle_get_contacts():
    return {"message": "Get all contacts", "route": "/contacts"}
