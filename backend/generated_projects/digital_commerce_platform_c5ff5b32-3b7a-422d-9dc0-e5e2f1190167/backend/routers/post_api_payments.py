
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/payments")
def handle_post_api_payments():
    return {"message": "Create a payments record", "route": "/api/payments"}
