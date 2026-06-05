
from fastapi import APIRouter
router = APIRouter()
@router.get("/")
def handle_api_weather_forecast__city_name_():
    return {"message": "Retrieves a multi-day weather forecast for a specified city."}
