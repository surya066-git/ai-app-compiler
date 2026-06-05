
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/reports")
def handle_get_api_reports():
    return {"message": "List reports records", "route": "/api/reports"}
