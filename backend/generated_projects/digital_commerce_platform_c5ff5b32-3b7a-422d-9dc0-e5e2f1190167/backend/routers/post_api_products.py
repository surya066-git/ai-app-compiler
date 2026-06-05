
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/products")
def handle_post_api_products():
    return {"message": "Create a products record", "route": "/api/products"}
