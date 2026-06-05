from templates.fastapi_templates import SECURITY_PY
from utils.security import generate_jwt_secret

def generate_security_file() -> dict:
    """Generates the security.py file with a unique JWT secret."""
    jwt_secret = generate_jwt_secret()
    security_code = SECURITY_PY.replace("{jwt_secret}", jwt_secret)
    
    return {
        "security.py": security_code,
        "jwt_secret": jwt_secret
    }

def generate_auth_routes() -> str:
    """Generates auth.py with standard login and signup endpoints."""
    return """
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
import models
from security import verify_password, get_password_hash, create_access_token
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    password: str

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    new_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
"""
