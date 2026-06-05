
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/carts")
def handle_post_api_carts():
    return {"message": "Create a carts record", "route": "/api/carts"}
