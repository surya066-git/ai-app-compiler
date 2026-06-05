
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
import auth
from routers import get_api_users
from routers import post_api_users
from routers import get_api_users_id
from routers import get_api_leads
from routers import post_api_leads
from routers import get_api_leads_id
from routers import get_api_properties
from routers import post_api_properties
from routers import get_api_properties_id
from routers import get_api_agents
from routers import post_api_agents
from routers import get_api_agents_id
from routers import get_api_metrics
from routers import post_api_metrics
from routers import get_api_metrics_id
from routers import get_api_reports
from routers import post_api_reports
from routers import get_api_reports_id


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Real Estate CRM")

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
app.include_router(get_api_leads.router, tags=['get_api_leads'])
app.include_router(post_api_leads.router, tags=['post_api_leads'])
app.include_router(get_api_leads_id.router, tags=['get_api_leads_id'])
app.include_router(get_api_properties.router, tags=['get_api_properties'])
app.include_router(post_api_properties.router, tags=['post_api_properties'])
app.include_router(get_api_properties_id.router, tags=['get_api_properties_id'])
app.include_router(get_api_agents.router, tags=['get_api_agents'])
app.include_router(post_api_agents.router, tags=['post_api_agents'])
app.include_router(get_api_agents_id.router, tags=['get_api_agents_id'])
app.include_router(get_api_metrics.router, tags=['get_api_metrics'])
app.include_router(post_api_metrics.router, tags=['post_api_metrics'])
app.include_router(get_api_metrics_id.router, tags=['get_api_metrics_id'])
app.include_router(get_api_reports.router, tags=['get_api_reports'])
app.include_router(post_api_reports.router, tags=['post_api_reports'])
app.include_router(get_api_reports_id.router, tags=['get_api_reports_id'])


@app.get("/")
def health_check():
    return {"status": "ok", "app": "Real Estate CRM"}
