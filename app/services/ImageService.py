import os
from uuid import uuid4
from dotenv import load_dotenv
from fastapi import UploadFile, HTTPException
from pathlib import Path

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
try:
    UPLOAD_DIR = os.environ["UPLOAD_DIR"]
    BASE_URL = os.environ["BASE_URL"]
except KeyError as e:
    raise RuntimeError(f"ENV var is missing: {e}")

UPLOAD_DIR_PATH = (PROJECT_ROOT / UPLOAD_DIR).resolve()
UPLOAD_DIR_PATH.mkdir(parents=True, exist_ok=True)


class ImageService:
    @staticmethod
    def store_image(image: UploadFile) -> str:
        if not image.content_type.startswith("image/"):
            raise HTTPException(
                status_code=400, detail="File must be an image")

        ext = os.path.splitext(image.filename)[1]
        filename = f"{uuid4().hex}{ext}"
        file_path = UPLOAD_DIR_PATH / filename

        with open(file_path, "wb") as f:
            f.write(image.file.read())

        return f"{BASE_URL}/images/{filename}"
