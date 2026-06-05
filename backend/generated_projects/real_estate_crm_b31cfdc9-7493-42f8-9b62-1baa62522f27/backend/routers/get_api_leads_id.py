
from fastapi import APIRouter
router = APIRouter()

@router.get("/api/leads/{id}")
def handle_get_api_leads_id(id: int):
    return {"message": "Fetch one leads record", "route": "/api/leads/{id}"}
