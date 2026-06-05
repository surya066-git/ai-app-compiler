
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/orders")
def handle_post_api_orders():
    return {"message": "Create a orders record", "route": "/api/orders"}
