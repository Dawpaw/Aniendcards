from dataclasses import (
    dataclass,
)
from pathlib import (
    Path,
)
from uuid import (
    uuid4,
)

from PIL import (
    Image,
)
from src.config import (
    IMAGES_TEMP_FOLDER,
    R2_BUCKET_NAME,
    s3,
)
from src.enums import (
    ImageTypes,
)


@dataclass
class ImageSize:
    width: int
    height:int


IMAGE_FORMAT = "webp"

def save_images(file_bytes: bytes, file_name: str):
    upload_dir = Path(IMAGES_TEMP_FOLDER)
    upload_dir.mkdir(exist_ok=True, parents=True)
    file_save_path = upload_dir / Path(file_name)
    with open(file_save_path, "wb") as file_doc:
        file_doc.write(file_bytes)  

def process_image(file_bytes: bytes, file_name: str | None, image_type: ImageTypes):
    temp_name : str = file_name or f"{uuid4()}"
    save_images(file_bytes, temp_name)  
    sizes_endcards: list[ImageSize] = [
        ImageSize(1920, 1080),
        ImageSize(1280, 720), 
        ImageSize(640, 360)
    ]

    sizes_cover: list[ImageSize] = [ImageSize(460, 650)]
    if(image_type == ImageTypes.COVER):
        _process_image_internal(temp_name, sizes_cover, "covers/")
    
    elif(image_type == ImageTypes.ENDCARD):
        _process_image_internal(temp_name, sizes_endcards, "endcard/")
    
    else:
        print("How did you even get here?")
    
    
def _process_image_internal(file_name: str, sizes: list[ImageSize], s3_folder: str):
    original_image_path = Path(IMAGES_TEMP_FOLDER) / Path(file_name)
    image = Image.open(original_image_path)
    # TODO maybe try to extract the image name creation and return that in the api
    if(len(sizes) == 1):
        image_names = [f"{uuid4()}_l.{IMAGE_FORMAT}"]
    else:
        image_names = [f"{uuid4()}_{k}.{IMAGE_FORMAT}" for k in ("l", "m", "s")]
    images_dests: list[Path] = [Path(IMAGES_TEMP_FOLDER) / Path(image_name) for image_name in image_names]

    for image_dest, size in zip(images_dests, sizes):
        image_copy = image.copy()
        image_copy.thumbnail((size.width, size.height))
        image_copy.info.clear()
        image_copy.save(image_dest, IMAGE_FORMAT)
    
    for image_dest, image_name in zip(images_dests, image_names):
        upload_images_s3(image_dest, f"{s3_folder}{image_name}")

    # Delete all saved images
    for img in images_dests:
        img.unlink(missing_ok=True)
    original_image_path.unlink(missing_ok=True)    

# TODO probably eventually do some dependency injection here 
def upload_images_s3(file_path: Path, image_name: str):
    with open(file_path, "rb") as f:
        s3.upload_fileobj(f, R2_BUCKET_NAME, image_name,
                            ExtraArgs={"ACL": "public-read"})