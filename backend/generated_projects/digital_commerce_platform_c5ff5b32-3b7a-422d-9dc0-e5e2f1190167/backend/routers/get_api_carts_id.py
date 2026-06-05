
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/carts/{id}")
def handle_get_api_carts_id(id: int):
    return {"message": "Fetch one carts record", "route": "/api/carts/{id}"}
