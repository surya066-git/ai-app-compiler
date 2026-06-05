MAIN_PY_TEMPLATE = """
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
import auth
{router_imports}

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="{app_name}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
{router_includes}

@app.get("/")
def health_check():
    return {"status": "ok", "app": "{app_name}"}
"""

REQUIREMENTS_TXT = """
fastapi>=0.115,<1
uvicorn>=0.30,<1
sqlalchemy>=2.0,<3
psycopg[binary]>=3.2,<4
python-jose[cryptography]>=3.3,<4
passlib[bcrypt]>=1.7,<2
bcrypt>=4,<5
python-multipart>=0.0.20,<1
pydantic>=2.10,<3
pydantic-settings>=2.7,<3
"""

DATABASE_PY = """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

# Use sqlite for default fallback if no postgres URL is provided
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""

SECURITY_PY = """
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
import os

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "{jwt_secret}")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
"""
