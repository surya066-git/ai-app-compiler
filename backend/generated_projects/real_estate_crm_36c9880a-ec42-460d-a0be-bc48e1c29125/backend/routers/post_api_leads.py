
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/leads")
def handle_post_api_leads():
    return {"message": "Create a leads record", "route": "/api/leads"}
