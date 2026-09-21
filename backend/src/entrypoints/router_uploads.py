from fastapi import (
    APIRouter,
    BackgroundTasks,
    HTTPException,
    UploadFile,
)
from src.config import (
    IMAGES_MAX_ALLOWED_SIZE,
)
from src.enums import (
    ImageTypes,
)
from src.services import (
    image_processing,
)

router = APIRouter()

@router.post("/upload/endcard")
async def upload_endcard(background_tasks: BackgroundTasks, file: UploadFile):
    file_bytes = await file.read()
    # Simple file validation
    if len(file_bytes) > IMAGES_MAX_ALLOWED_SIZE * 1024 * 1024:
        # more than 2 MB
        raise HTTPException(status_code=400, detail="File too large")

    content_type = file.content_type
    # https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types
    if content_type not in ["image/jpeg", "image/png", "image/avif", "image/webp"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    background_tasks.add_task(image_processing.process_image, file_bytes, file.filename, ImageTypes.ENDCARD)
    
    return {"message": "Uploaded successfully"}

@router.post("/upload/cover")
async def upload_cover(background_tasks: BackgroundTasks, file: UploadFile):
    file_bytes = await file.read()
    # Simple file validation
    if len(file_bytes) > IMAGES_MAX_ALLOWED_SIZE * 1024 * 1024:
        # more than 2 MB
        raise HTTPException(status_code=400, detail="File too large")

    content_type = file.content_type
    # https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types
    if content_type not in ["image/jpeg", "image/png", "image/avif", "image/webp"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    background_tasks.add_task(image_processing.process_image, file_bytes, file.filename, ImageTypes.COVER)
    
    return {"message": "Uploaded successfully"}