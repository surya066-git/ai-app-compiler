
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/reports")
def handle_post_api_reports():
    return {"message": "Create a reports record", "route": "/api/reports"}
