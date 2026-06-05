import os

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from compiler_pipeline import PIPELINE_STAGES, run_compiler_pipeline
from config.settings import settings
from utils.logger import app_logger
from utils.security import sanitize_filename


app = FastAPI(title="AI App Compiler", description="Compiler-style AI app generation pipeline")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PromptInput(BaseModel):
    prompt: str


@app.get("/health")
async def health():
    return {"status": "ok", "app": settings.APP_NAME, "stages": len(PIPELINE_STAGES)}


@app.get("/pipeline/stages")
async def pipeline_stages():
    return {"stages": PIPELINE_STAGES}


@app.post("/compile", status_code=status.HTTP_200_OK)
async def compile_app(data: PromptInput):
    app_logger.info(f"Compilation started for: {data.prompt}")
    try:
        return await run_compiler_pipeline(
            data.prompt,
            run_runtime=True,
            require_runtime_success=True,
            raise_on_failure=True,
        )
    except Exception as e:
        app_logger.exception("Compilation failed.")
        raise HTTPException(status_code=500, detail={"error": "CompilerError", "message": str(e)})


@app.get("/download/{file_name}")
async def download_zip(file_name: str):
    safe_name = sanitize_filename(file_name)
    if safe_name != file_name or not safe_name.endswith(".zip"):
        raise HTTPException(status_code=400, detail="Invalid file name")

    file_path = os.path.join(settings.EXPORT_DIR, safe_name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path=file_path, filename=safe_name, media_type="application/zip")
