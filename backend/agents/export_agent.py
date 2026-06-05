import os
from config.settings import settings
from exceptions.generation_exceptions import ExportException
from utils.security import sanitize_filename
from utils.file_exporter import write_project_files
from utils.zip_exporter import create_zip_archive

async def export_project(files: dict, generation_id: str, architecture: dict) -> str:
    """
    Writes all files safely to disk, generates a project.json, and zips the project.
    Returns the path to the zip file.
    """
    try:
        app_name = sanitize_filename(architecture.get("app_name", "GeneratedApp").lower().replace(" ", "_"))
        project_dir = os.path.join(settings.EXPORT_DIR, f"{app_name}_{generation_id}")
        
        metadata = {
            "generation_id": generation_id,
            "architecture": architecture,
            "exported_files": list(files.keys())
        }
        
        # Write all files
        write_project_files(project_dir, files, metadata)
            
        # Create ZIP
        zip_base_path = os.path.join(settings.EXPORT_DIR, f"{app_name}_{generation_id}")
        zip_path = create_zip_archive(project_dir, zip_base_path)
        
        return zip_path
        
    except Exception as e:
        raise ExportException(f"Failed to export project: {str(e)}")
