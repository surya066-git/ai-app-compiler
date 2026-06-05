
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/orders")
def handle_get_api_orders():
    return {"message": "List orders records", "route": "/api/orders"}
