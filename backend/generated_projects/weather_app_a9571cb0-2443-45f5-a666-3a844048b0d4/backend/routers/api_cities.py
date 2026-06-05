
from fastapi import APIRouter
router = APIRouter()
@router.get("/")
def handle_api_cities():
    return {"message": "Lists all cities available for weather lookup."}
