from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
import auth
from routers import students
from routers import attendance

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Attendance Tracker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(students.router, prefix='/students', tags=['students'])
app.include_router(attendance.router, prefix='/attendance', tags=['attendance'])

# Install psycopg2-binary instead of psycopg2 to avoid building from source
# This change should be made in the requirements.txt file or the environment where the application is running
# psycopg2-binary should be installed instead of psycopg2

@app.get("/")
def health_check():
    return {"status": "ok", "app": "Student Attendance Tracker"}