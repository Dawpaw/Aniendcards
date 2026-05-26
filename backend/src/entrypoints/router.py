from typing import Annotated, Generator

from fastapi import APIRouter, HTTPException, Query, Depends, Response, status

from src.adapters import orm
from src.entrypoints.schemas import requests, responses
from src.services import services, commands, unit_of_work
from src.services.commands import CreateMediaCommand, CreateEntryCommand, CreateEndcardCommand, CreateArtistCommand, MediaTitle

orm.start_mappers()
router = APIRouter()

def get_uow() -> Generator[unit_of_work.SqlAlchemyUnitOfWork, None, None]:
    yield unit_of_work.SqlAlchemyUnitOfWork()
UowDep = Annotated[unit_of_work.SqlAlchemyUnitOfWork, Depends(get_uow)]


# Media
@router.post("/media/", response_model=responses.MediaResponse)
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
    return responses.MediaResponse.model_validate(media)


@router.get("/media/{media_title}", response_model=responses.MediaResponse)
def read_media_by_title(media_title:str, uow: UowDep):
    media = services.get_media_by_title(media_title, uow)
    return responses.MediaResponse.model_validate(media)


# @router.get("/media/{media_id}", response_model=schemas.Media)
# def read_anime(db: SessionDep, media_id: int):
#     db_media = service.get_media_by_id(db=db, media_id=media_id)
#     if db_media is None:
#         raise HTTPException(status_code=400, detail="Anime not found")
#     return db_media


# Artists
@router.post("/artist/", response_model=responses.ArtistReponse)
def create_artist(request: requests.CreateArtistRequest, uow: UowDep):

    artist = services.create_artist(
        CreateArtistCommand(
            username=request.username,
            links=[str(link.link) for link in request.links] if request.links else None
        ),
        uow
    )
    
    return responses.ArtistReponse.model_validate(artist)


# @router.get("/artists/", response_model=list[schemas.Artist])
# def read_artists(db: SessionDep, skip: int = 0, limit: int = 100):
#     artists = service.get_artists(db, skip=skip, limit=limit)
#     return artists


# @router.get("/artist/", response_model=schemas.Artist)
# def read_artist_by_username(
#     db: SessionDep, username: Annotated[str, Query(min_length=3)] = ...
# ):
#     artist = service.get_artist_by_username(db, username=username)
#     if not artist:
#         raise HTTPException(status_code=404, detail="Artist doesn't exist")
#     return artist


# @router.get("/artist/{artist_id}", response_model=schemas.Artist)
# def read_artist(db: SessionDep, artist_id: int):
#     db_artist = service.get_artist_by_id(db=db, artist_id=artist_id)
#     if db_artist is None:
#         raise HTTPException(status_code=400, detail="Artist not found")
#     return db_artist


# Entry
@router.post("/entry/", response_model=responses.EntryResponse)
def create_entry(request: requests.CreateEntryRequest, uow: UowDep):
    # TODO find a way to use the media
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
    return responses.EntryResponse.model_validate(entry)

# Endcards
@router.post("/endcards/", response_model=responses.EndcardResponse)
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
    return responses.EndcardResponse.model_validate(endcard)

# @router.get("/endcards/", response_model=list[schemas.EndcardsLazy])
# def read_endcards(db: SessionDep, skip: int = 0, limit: int = 100):
#     endcards = service.get_endcards(db, skip=skip, limit=limit)
#     return endcards


# @router.get("/endcards/{endcard_id}", response_model=schemas.EndcardsLazy)
# def read_endcard(db: SessionDep, endcard_id: int):
#     db_endcard = service.get_endcard_by_id(db=db, endcard_id=endcard_id)
#     if db_endcard is None:
#         raise HTTPException(status_code=400, detail="Endcard not found")
#     return db_endcard
