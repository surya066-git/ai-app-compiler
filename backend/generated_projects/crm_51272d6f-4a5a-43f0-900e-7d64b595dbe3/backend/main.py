from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
import auth
from routers import post_login
from routers import get_contacts
from routers import get_dashboard
from routers import get_analytics
from routers import post_payments

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRM")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(post_login.router, prefix="/post_login", tags=['post_login'])
app.include_router(get_contacts.router, prefix="/get_contacts", tags=['get_contacts'])
app.include_router(get_dashboard.router, prefix="/get_dashboard", tags=['get_dashboard'])
app.include_router(get_analytics.router, prefix="/get_analytics", tags=['get_analytics'])
app.include_router(post_payments.router, prefix="/post_payments", tags=['post_payments'])

@app.get("/")
def health_check():
    return {"status": "ok", "app": "CRM"}