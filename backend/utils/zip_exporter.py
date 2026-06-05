import shutil

def create_zip_archive(source_dir: str, target_zip_base: str) -> str:
    """
    Creates a ZIP archive from the given source directory.
    target_zip_base should be the path without the .zip extension.
    Returns the path to the created zip file.
    """
    shutil.make_archive(target_zip_base, "zip", source_dir)
    return f"{target_zip_base}.zip"
