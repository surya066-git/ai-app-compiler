
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/carts")
def handle_get_api_carts():
    return {"message": "List carts records", "route": "/api/carts"}
