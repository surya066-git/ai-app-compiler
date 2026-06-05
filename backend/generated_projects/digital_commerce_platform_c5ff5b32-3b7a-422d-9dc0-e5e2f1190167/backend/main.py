
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
import auth
from routers import get_api_users
from routers import post_api_users
from routers import get_api_users_id
from routers import get_api_products
from routers import post_api_products
from routers import get_api_products_id
from routers import get_api_carts
from routers import post_api_carts
from routers import get_api_carts_id
from routers import get_api_orders
from routers import post_api_orders
from routers import get_api_orders_id
from routers import get_api_payments
from routers import post_api_payments
from routers import get_api_payments_id
from routers import get_api_vehicles
from routers import post_api_vehicles
from routers import get_api_vehicles_id
from routers import get_api_campaigns
from routers import post_api_campaigns
from routers import get_api_campaigns_id


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Digital Commerce Platform")

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
app.include_router(get_api_products.router, tags=['get_api_products'])
app.include_router(post_api_products.router, tags=['post_api_products'])
app.include_router(get_api_products_id.router, tags=['get_api_products_id'])
app.include_router(get_api_carts.router, tags=['get_api_carts'])
app.include_router(post_api_carts.router, tags=['post_api_carts'])
app.include_router(get_api_carts_id.router, tags=['get_api_carts_id'])
app.include_router(get_api_orders.router, tags=['get_api_orders'])
app.include_router(post_api_orders.router, tags=['post_api_orders'])
app.include_router(get_api_orders_id.router, tags=['get_api_orders_id'])
app.include_router(get_api_payments.router, tags=['get_api_payments'])
app.include_router(post_api_payments.router, tags=['post_api_payments'])
app.include_router(get_api_payments_id.router, tags=['get_api_payments_id'])
app.include_router(get_api_vehicles.router, tags=['get_api_vehicles'])
app.include_router(post_api_vehicles.router, tags=['post_api_vehicles'])
app.include_router(get_api_vehicles_id.router, tags=['get_api_vehicles_id'])
app.include_router(get_api_campaigns.router, tags=['get_api_campaigns'])
app.include_router(post_api_campaigns.router, tags=['post_api_campaigns'])
app.include_router(get_api_campaigns_id.router, tags=['get_api_campaigns_id'])


@app.get("/")
def health_check():
    return {"status": "ok", "app": "Digital Commerce Platform"}
