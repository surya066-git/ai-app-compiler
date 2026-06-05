@echo off
echo Starting AI App Compiler...

:: Start Backend in a new terminal window
start "AI Compiler Backend" cmd /c "cd backend && .\venv\Scripts\activate && uvicorn main:app --port 8000"

:: Start Frontend in a new terminal window
start "AI Compiler Frontend" cmd /c "cd frontend && npm run dev"

echo Services are launching in new windows!
echo Frontend will be at http://localhost:3001
echo Backend will be at http://localhost:8000
