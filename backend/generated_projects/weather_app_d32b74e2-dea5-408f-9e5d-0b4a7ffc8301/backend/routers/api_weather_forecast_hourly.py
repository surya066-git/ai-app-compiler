
from fastapi import APIRouter
router = APIRouter()
@router.get("/")
def handle_api_weather_forecast_hourly():
    return {"message": "Fetches hourly weather forecast for a specified location via OpenWeatherMap API proxy."}
