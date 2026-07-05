from typing import Annotated, Generator

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.adapters import orm
from src.entrypoints.schemas import requests, responses
from src.services import services, unit_of_work
from src.services.commands import (CreateMediaCommand, CreateEntryCommand, CreateEndcardCommand, 
                                    CreateArtistCommand, CreateUserCommand, MediaTitle)

orm.start_mappers()
router = APIRouter()

def get_uow() -> Generator[unit_of_work.SqlAlchemyUnitOfWork, None, None]:
    yield unit_of_work.SqlAlchemyUnitOfWork()
UowDep = Annotated[unit_of_work.SqlAlchemyUnitOfWork, Depends(get_uow)]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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

@router.post("/user/", response_model=responses.UserResponse)
def create_user(request: requests.CreateUserRequest, uow: UowDep):
    user = services.create_user(
        CreateUserCommand(
            username=request.username,
            password=request.password,
            email=request.email
        ),
        uow
    )
    return user

# This is just a temporary endpoint
@router.post("/role/", response_model=responses.RoleResponse)
def create_role(request: requests.CreateRoleRequest, uow: UowDep):
    role = services.create_role(
        request.name,
        request.description,
        uow
    )
    return role

# Authentication
@router.post("/token", response_model=responses.TokenResponse)
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], uow: UowDep):
    user = services.autheticate_user(form_data.username, form_data.password, uow)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = services.create_auth_token(user)
    return responses.TokenResponse(access_token=access_token, token_type="bearer")

# Too shallow for my liking
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], uow: UowDep):
    return services.get_current_user(token, uow)

def get_current_active_user(current_user = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# TODO Delete - it is just for test
@router.get("/users/me/")
async def read_users_me(current_user = Depends(get_current_active_user)):
    return {"message": "test worked yay"}