from pathlib import Path
from uuid import uuid4


from src.services.unit_of_work import SqlAlchemyUnitOfWork
from src.config import IMAGES_TEMP_FOLDER, s3, R2_BUCKET_NAME
from PIL import Image

IMAGE_FORMAT = "webp"
def process_image(file_name: str, uow: SqlAlchemyUnitOfWork):
    original_image_path = Path(IMAGES_TEMP_FOLDER) / Path(file_name)
    image = Image.open(original_image_path)
    sizes = [
        {"width": 1920, "height": 1080},
        {"width": 1280, "height": 720},
        {"width": 640, "height": 360},
    ]
    image_names = [f"{uuid4()}_{k}.{IMAGE_FORMAT}" for k in ("l", "m", "s")]
    images_dests: list[Path] = [Path(IMAGES_TEMP_FOLDER) / Path(image_name) for image_name in image_names]

    for image_dest, size in zip(images_dests,sizes):
        image_copy = image.copy()
        image_copy.thumbnail((size["width"], size["height"]))
        image_copy.info.clear()
        image_copy.save(image_dest, IMAGE_FORMAT)
    
    # TODO upload the images to object storage
    for image_dest, image_name in zip(images_dests, image_names):
        upload_images_s3(image_dest, image_name)

    # TODO get the images urls and save them into the database

    # Delete all saved images
    for img in images_dests:
        img.unlink(missing_ok=True)
    original_image_path.unlink(missing_ok=True)    

# TODO probably eventually do some dependency injection here 
def upload_images_s3(file_path: Path, image_name: str):
    with open(file_path, "rb") as f:
        s3.upload_fileobj(f, R2_BUCKET_NAME, image_name,
                            ExtraArgs={"ACL": "public-read"})