
from fastapi import APIRouter
router = APIRouter()
@router.get("/")
def handle_api_weather_forecast_daily():
    return {"message": "Fetches daily weather forecast for a specified location via OpenWeatherMap API proxy."}
