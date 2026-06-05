
from fastapi import APIRouter
router = APIRouter()
@router.get("/")
def handle_students():
    return {"message": "Get all students"}
