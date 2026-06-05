
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/reports/{id}")
def handle_get_api_reports_id(id: int):
    return {"message": "Fetch one reports record", "route": "/api/reports/{id}"}
