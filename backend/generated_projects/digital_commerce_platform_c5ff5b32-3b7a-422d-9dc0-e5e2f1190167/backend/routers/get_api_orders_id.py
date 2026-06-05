
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/orders/{id}")
def handle_get_api_orders_id(id: int):
    return {"message": "Fetch one orders record", "route": "/api/orders/{id}"}
