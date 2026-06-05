
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/products/{id}")
def handle_get_api_products_id(id: int):
    return {"message": "Fetch one products record", "route": "/api/products/{id}"}
