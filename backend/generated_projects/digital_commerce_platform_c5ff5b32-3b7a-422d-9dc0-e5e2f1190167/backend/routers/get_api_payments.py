
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/payments")
def handle_get_api_payments():
    return {"message": "List payments records", "route": "/api/payments"}
