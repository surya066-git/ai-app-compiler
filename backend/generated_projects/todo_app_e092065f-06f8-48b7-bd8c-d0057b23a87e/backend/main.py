
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
import auth
from routers import post_register
from routers import post_login
from routers import get_users_me
from routers import post_tasks
from routers import get_tasks
from routers import get_tasks_id
from routers import put_tasks_id
from routers import delete_tasks_id


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(post_register.router, tags=['post_register'])
app.include_router(post_login.router, tags=['post_login'])
app.include_router(get_users_me.router, tags=['get_users_me'])
app.include_router(post_tasks.router, tags=['post_tasks'])
app.include_router(get_tasks.router, tags=['get_tasks'])
app.include_router(get_tasks_id.router, tags=['get_tasks_id'])
app.include_router(put_tasks_id.router, tags=['put_tasks_id'])
app.include_router(delete_tasks_id.router, tags=['delete_tasks_id'])


@app.get("/")
def health_check():
    return {"status": "ok", "app": "Todo App"}
