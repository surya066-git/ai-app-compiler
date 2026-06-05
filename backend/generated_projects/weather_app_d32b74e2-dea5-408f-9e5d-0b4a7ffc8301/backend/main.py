
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
import auth
from routers import api_weather_current
from routers import api_weather_forecast_hourly
from routers import api_weather_forecast_daily
from routers import api_location_search


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Weather App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(api_weather_current.router, prefix='/api_weather_current', tags=['api_weather_current'])
app.include_router(api_weather_forecast_hourly.router, prefix='/api_weather_forecast_hourly', tags=['api_weather_forecast_hourly'])
app.include_router(api_weather_forecast_daily.router, prefix='/api_weather_forecast_daily', tags=['api_weather_forecast_daily'])
app.include_router(api_location_search.router, prefix='/api_location_search', tags=['api_location_search'])


@app.get("/")
def health_check():
    return {"status": "ok", "app": "Weather App"}
