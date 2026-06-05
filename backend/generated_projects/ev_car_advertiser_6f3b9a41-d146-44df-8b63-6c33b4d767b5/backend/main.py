
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
import auth
from routers import vehicles
from routers import vehicles__id_
from routers import users
from routers import users__id_


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="EV Car Advertiser")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(vehicles.router, prefix='/vehicles', tags=['vehicles'])
app.include_router(vehicles__id_.router, prefix='/vehicles__id_', tags=['vehicles__id_'])
app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(users__id_.router, prefix='/users__id_', tags=['users__id_'])


@app.get("/")
def health_check():
    return {"status": "ok", "app": "EV Car Advertiser"}
