
from fastapi import APIRouter
router = APIRouter()

@router.post("/payments")
def handle_post_payments():
    return {"message": "Make a payment", "route": "/payments"}
