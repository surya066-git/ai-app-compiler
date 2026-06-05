
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
import auth
from routers import todos
from routers import todos__id_


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
app.include_router(todos.router, prefix='/todos', tags=['todos'])
app.include_router(todos__id_.router, prefix='/todos__id_', tags=['todos__id_'])


@app.get("/")
def health_check():
    return {"status": "ok", "app": "Todo App"}
