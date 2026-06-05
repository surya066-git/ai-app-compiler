
from fastapi import APIRouter
router = APIRouter()

@router.get("/dashboard")
def handle_get_dashboard():
    return {"message": "Get dashboard data", "route": "/dashboard"}
