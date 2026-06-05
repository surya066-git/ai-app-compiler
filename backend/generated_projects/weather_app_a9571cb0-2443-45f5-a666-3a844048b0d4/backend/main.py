
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
import auth
from routers import api_weather_current__city_name_
from routers import api_weather_forecast__city_name_
from routers import api_cities


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
app.include_router(api_weather_current__city_name_.router, prefix='/api_weather_current__city_name_', tags=['api_weather_current__city_name_'])
app.include_router(api_weather_forecast__city_name_.router, prefix='/api_weather_forecast__city_name_', tags=['api_weather_forecast__city_name_'])
app.include_router(api_cities.router, prefix='/api_cities', tags=['api_cities'])


@app.get("/")
def health_check():
    return {"status": "ok", "app": "Weather App"}
