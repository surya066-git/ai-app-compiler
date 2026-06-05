
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/products")
def handle_get_api_products():
    return {"message": "List products records", "route": "/api/products"}
