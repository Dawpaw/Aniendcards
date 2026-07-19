from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, BackgroundTasks

from src.config import IMAGES_MAX_ALLOWED_SIZE, IMAGES_TEMP_FOLDER
from src.entrypoints.schemas import requests, responses
from src.entrypoints.dependencies import UowDep, is_user_admin
from src.services import services, image_processing
from src.services.commands import (CreateMediaCommand, CreateEntryCommand, CreateEndcardCommand, 
                                    CreateArtistCommand, MediaTitle)

router = APIRouter()

# Media
@router.post("/media/", response_model=responses.MediaResponse,
                dependencies=[Depends(is_user_admin)])
def create_media(request: requests.CreateMediaRequest, uow: UowDep):
    media = services.create_media(
        CreateMediaCommand(
            type=request.type,
            format=request.format,
            season=request.season,
            season_year=request.season_year,
            cover_image=str(request.cover_image),
            description=request.description,
            titles=[MediaTitle(language=t.language, title=t.title) for t in request.titles],
            links=[str(link.link) for link in request.links] if request.links else None
        ),
        uow
    )
    if media is None:
        raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Media alreaedy exists",
                )
    return media

@router.get("/media/{media_title}", response_model=responses.MediaResponse)
def read_media_by_title(media_title:str, uow: UowDep):
    media = services.get_media_by_title(media_title, uow)
    if media is None:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Media not found",
                )
    return media

@router.get("/media/", response_model=list[responses.MediaOnlyResponse])
def read_all_media(uow: UowDep):
    media = services.get_all_media(uow)
    if media is None:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Media not found",
                )
    return media

@router.get("/media/id/{media_id}", response_model=responses.MediaResponse)
def read_media_by_id(media_id: int, uow: UowDep):
    media = services.get_media_by_id(media_id, uow)
    if media is None:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Media not found",
                )
    return media


@router.delete("/media/id/{media_id}", status_code=status.HTTP_204_NO_CONTENT,
                dependencies=[Depends(is_user_admin)])
def delete_media_by_id(media_id: int, uow: UowDep):
    services.delete_media_by_id(media_id, uow)

# Artists
@router.post("/artist/", response_model=responses.ArtistReponse,
                dependencies=[Depends(is_user_admin)])
def create_artist(request: requests.CreateArtistRequest, uow: UowDep):

    artist = services.create_artist(
        CreateArtistCommand(
            username=request.username,
            links=[str(link.link) for link in request.links] if request.links else None
        ),
        uow
    )
    
    if artist is None:
        raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Artists already exists",
                )
    return artist


@router.get("/artists/", response_model=list[responses.ArtistReponse])
def read_artists(uow: UowDep):
    artists = services.get_artists(uow)
    if artists is None:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Artists not found",
                )
    return artists


@router.get("/artist/{username}", response_model=responses.ArtistReponse)
def read_artist_by_username(username: str, uow: UowDep):
    artist = services.get_artist_by_username(username, uow)
    if artist is None:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Artist not found",
                )
    return artist


@router.get("/artist/id/{artist_id}", response_model=responses.ArtistReponse)
def read_artist(artist_id: int, uow: UowDep):
    artist = services.get_artist_by_id(artist_id, uow)
    if artist is None:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Artist not found",
                )
    return artist

@router.delete("/artist/id/{artist_id}", status_code=status.HTTP_204_NO_CONTENT,
                dependencies=[Depends(is_user_admin)])
def delete_artist(artist_id: int, uow: UowDep):
    services.delete_artist_by_id(artist_id, uow)

# Entry
@router.post("/entry/", response_model=responses.EntryResponse,
                dependencies=[Depends(is_user_admin)])
def create_entry(request: requests.CreateEntryRequest, uow: UowDep):
    entry = services.create_entry(
        CreateEntryCommand(
            description=request.description,
            entry_number=request.entry_number,
            endcards=request.endcards,
            media_id=request.media_id,
            media_title=request.media_title
        ),
        uow
    )    
    if entry is None:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Media not found for this entry",
                )
    return entry

# Endcards
@router.post("/endcard/", response_model=responses.EndcardResponse,
                dependencies=[Depends(is_user_admin)])
def create_endcard(request: requests.CreateEncardRequest, uow: UowDep):
    endcard = services.create_endcard(
        CreateEndcardCommand(
            img_url=str(request.img_url),
            alt_img_url=str(request.alt_img_url) if request.alt_img_url else None,
            source_url=str(request.source_url),
            artist_id=request.artist_id,
            entry_id=request.entry_id
        ),
        uow
    )
    if endcard is None:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Media or Artists not found for this endcard",
                )
    return endcard

@router.get("/endcards/", response_model=list[responses.EndcardResponse])
def read_endcards(uow: UowDep):
    endcards = services.get_endcards(uow)
    if endcards is None:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Endcards not found",
                )
    return endcards


@router.get("/endcard/{endcard_id}", response_model=responses.EndcardResponse)
def read_endcard(endcard_id: int, uow: UowDep):
    endcard = services.get_endcard_by_id(endcard_id, uow)
    if endcard is None:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Endcard not found",
                )
    return endcard

@router.delete("/endcard/{endcard_id}", status_code=status.HTTP_204_NO_CONTENT,
                dependencies=[Depends(is_user_admin)])
def delete_endcard(endcard_id: int, uow: UowDep):
    services.delete_endcard_by_id(endcard_id, uow)
    
# FIXME this needs to be moved 
@router.post("/upload/endcard")
async def upload_endcard(background_tasks: BackgroundTasks, file: UploadFile, uow: UowDep):
    # Simple file validation
    file.file.seek(0, 2)
    file_size = file.file.tell()
    await file.seek(0)
    if file_size > IMAGES_MAX_ALLOWED_SIZE * 1024 * 1024:
        # more than 2 MB
        raise HTTPException(status_code=400, detail="File too large")

    content_type = file.content_type
    # https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types
    if content_type not in ["image/jpeg", "image/png", "image/avif", "image/webp"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    upload_dir = Path(IMAGES_TEMP_FOLDER)
    # TODO dir creation somewhere else
    upload_dir.mkdir(exist_ok=True, parents=True)
    file_name = str(file.filename)
    file_save_path = upload_dir / Path(file_name)
    with open(file_save_path, "wb") as file_doc:
        file_doc.write(await file.read())
    background_tasks.add_task(image_processing.process_image, file_name, uow)
    
    return {"message": "Uploaded successfully"}