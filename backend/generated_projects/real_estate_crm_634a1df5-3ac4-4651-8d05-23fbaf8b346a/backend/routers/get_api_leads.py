
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/leads")
def handle_get_api_leads():
    return {"message": "List leads records", "route": "/api/leads"}
