
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
import auth
from routers import get_api_users
from routers import post_api_users
from routers import get_api_users_id
from routers import get_api_projects
from routers import post_api_projects
from routers import get_api_projects_id
from routers import get_api_tasks
from routers import post_api_tasks
from routers import get_api_tasks_id
from routers import get_api_vehicles
from routers import post_api_vehicles
from routers import get_api_vehicles_id
from routers import get_api_campaigns
from routers import post_api_campaigns
from routers import get_api_campaigns_id
from routers import get_api_leads
from routers import post_api_leads
from routers import get_api_leads_id


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(get_api_users.router, tags=['get_api_users'])
app.include_router(post_api_users.router, tags=['post_api_users'])
app.include_router(get_api_users_id.router, tags=['get_api_users_id'])
app.include_router(get_api_projects.router, tags=['get_api_projects'])
app.include_router(post_api_projects.router, tags=['post_api_projects'])
app.include_router(get_api_projects_id.router, tags=['get_api_projects_id'])
app.include_router(get_api_tasks.router, tags=['get_api_tasks'])
app.include_router(post_api_tasks.router, tags=['post_api_tasks'])
app.include_router(get_api_tasks_id.router, tags=['get_api_tasks_id'])
app.include_router(get_api_vehicles.router, tags=['get_api_vehicles'])
app.include_router(post_api_vehicles.router, tags=['post_api_vehicles'])
app.include_router(get_api_vehicles_id.router, tags=['get_api_vehicles_id'])
app.include_router(get_api_campaigns.router, tags=['get_api_campaigns'])
app.include_router(post_api_campaigns.router, tags=['post_api_campaigns'])
app.include_router(get_api_campaigns_id.router, tags=['get_api_campaigns_id'])
app.include_router(get_api_leads.router, tags=['get_api_leads'])
app.include_router(post_api_leads.router, tags=['post_api_leads'])
app.include_router(get_api_leads_id.router, tags=['get_api_leads_id'])


@app.get("/")
def health_check():
    return {"status": "ok", "app": "Task Management System"}
