from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Optional: If a user can submit observations, add a relationship like below
    # submitted_observations = relationship("WeatherObservation", back_populates="submitter")

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    country = Column(String(255), nullable=True) # Adding country for better city identification

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationship to WeatherObservation: one city can have many observations
    observations = relationship("WeatherObservation", back_populates="city")

class WeatherObservation(Base):
    __tablename__ = "weather_observations"

    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign key to City model
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    
    temperature = Column(Float, nullable=False) # e.g., in Celsius or Fahrenheit
    humidity = Column(Float, nullable=False)    # Percentage (e.g., 0-100)
    pressure = Column(Float, nullable=True)     # Atmospheric pressure (e.g., in hPa or mbar)
    description = Column(String(500), nullable=True) # e.g., "Clear sky", "Partly cloudy", "Rainy"
    
    # The actual time the observation was made, distinct from when the record was created in the DB
    observation_time = Column(DateTime, nullable=False, default=func.now()) 

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationship to City model: an observation belongs to one city
    city = relationship("City", back_populates="observations")

    # Optional: If observations are submitted by users
    # user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    # submitter = relationship("User", back_populates="submitted_observations")