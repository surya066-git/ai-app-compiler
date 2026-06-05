
from fastapi import APIRouter
router = APIRouter()
@router.get("/")
def handle_api_weather_current():
    return {"message": "Fetches current weather conditions for a specified location (e.g., city name or lat/lon) via OpenWeatherMap API proxy."}
