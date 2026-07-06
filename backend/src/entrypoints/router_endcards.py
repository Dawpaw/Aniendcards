from typing import Annotated, Generator

from fastapi import APIRouter, Depends

from src.entrypoints.schemas import requests, responses
from src.entrypoints.router_auth import is_user_admin
from src.services import services, unit_of_work
from src.services.commands import (CreateMediaCommand, CreateEntryCommand, CreateEndcardCommand, 
                                    CreateArtistCommand, MediaTitle)

router = APIRouter()

# TODO Move this 
def get_uow() -> Generator[unit_of_work.SqlAlchemyUnitOfWork, None, None]:
    yield unit_of_work.SqlAlchemyUnitOfWork()
UowDep = Annotated[unit_of_work.SqlAlchemyUnitOfWork, Depends(get_uow)]

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
    return media

@router.get("/media/{media_title}", response_model=responses.MediaResponse)
def read_media_by_title(media_title:str, uow: UowDep):
    media = services.get_media_by_title(media_title, uow)
    return media

@router.get("/media/", response_model=list[responses.MediaOnlyResponse])
def read_all_media(uow: UowDep):
    media = services.get_all_media(uow)
    return media

@router.get("/media/id/{media_id}", response_model=responses.MediaResponse)
def read_media_by_id(media_id: int, uow: UowDep):
    media = services.get_media_by_id(media_id, uow)
    return media


@router.delete("/media/id/{media_id}", response_model=responses.MediaResponse)
def delete_media_by_id(media_id: int, uow: UowDep):
    media = services.delete_media_by_id(media_id, uow)
    return media

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
    
    return artist


@router.get("/artists/", response_model=list[responses.ArtistReponse])
def read_artists(uow: UowDep):
    artists = services.get_artists(uow)
    return artists


@router.get("/artist/{username}", response_model=responses.ArtistReponse)
def read_artist_by_username(username: str, uow: UowDep):
    artist = services.get_artist_by_username(username, uow)
    return artist


@router.get("/artist/id/{artist_id}", response_model=responses.ArtistReponse)
def read_artist(artist_id: int, uow: UowDep):
    db_artist = services.get_artist_by_id(artist_id, uow)
    return db_artist

@router.delete("/artist/id/{artist_id}", response_model=responses.ArtistReponse)
def delete_artist(artist_id: int, uow: UowDep):
    db_artist = services.delete_artist_by_id(artist_id, uow)
    return db_artist

# Entry
@router.post("/entry/", response_model=responses.EntryResponse)
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
    return entry

# Endcards
@router.post("/endcard/", response_model=responses.EndcardResponse)
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
    return endcard

@router.get("/endcards/", response_model=list[responses.EndcardResponse])
def read_endcards(uow: UowDep):
    endcards = services.get_endcards(uow)
    return endcards


@router.get("/endcard/{endcard_id}", response_model=responses.EndcardResponse)
def read_endcard(endcard_id: int, uow: UowDep):
    db_endcard = services.get_endcard_by_id(endcard_id, uow)
    return db_endcard

@router.delete("/endcard/{endcard_id}", response_model=responses.EndcardResponse)
def delete_endcard(endcard_id: int, uow: UowDep):
    db_endcard = services.delete_endcard_by_id(endcard_id, uow)
    return db_endcard
