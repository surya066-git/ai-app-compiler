
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/payments/{id}")
def handle_get_api_payments_id(id: int):
    return {"message": "Fetch one payments record", "route": "/api/payments/{id}"}
