from fastapi import APIRouter, HTTPException

from src.posts import models, schemas, service
from src.database import engine
from src.posts.dependecies import SessionDep

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Media
@router.post("/media/", response_model=schemas.Media)
def create_media(media: schemas.MediaCreate, db: SessionDep):
    db_romaji = service.get_media_by_title(db, media_title=media.title_romaji)
    if db_romaji:
        raise HTTPException(status_code=400, detail="Anime already exists")
    return service.create_media(db=db, media=media)


@router.get("/media/", response_model=list[schemas.Media])
def read_medias(db: SessionDep, skip: int = 0, limit: int = 100):
    medias = service.get_medias(db, skip=skip, limit=limit)
    return medias


@router.get("/media/{media_id}", response_model=schemas.Media)
def read_anime(db: SessionDep, media_id: int):
    db_media = service.get_media_by_id(db=db, media_id=media_id)
    if db_media is None:
        raise HTTPException(status_code=400, detail="Anime not found")
    return db_media


# Artists
@router.post("/artist/", response_model=schemas.Artist)
def create_artist(artist: schemas.ArtistCreate, db: SessionDep):
    db_artist = service.get_artist_by_username(db=db, username=artist.username)
    if db_artist:
        raise HTTPException(status_code=400, detail="Artist already exists")
    return service.create_artist(db=db, artist=artist)


@router.get("/artist/", response_model=list[schemas.Artist])
def read_artists(db: SessionDep, skip: int = 0, limit: int = 100):
    medias = service.get_artists(db, skip=skip, limit=limit)
    return medias


@router.get("/artist/{artist_id}", response_model=schemas.Artist)
def read_artist(db: SessionDep, artist_id: int):
    db_artist = service.get_artist_by_id(db=db, artist_id=artist_id)
    if db_artist is None:
        raise HTTPException(status_code=400, detail="Artist not found")
    return db_artist


# Episodes
@router.post("/media/{media_id}/episodes/", response_model=schemas.Episode)
def create_episode_for_media(
    media_id: int, episode: schemas.EpisodeCreate, db: SessionDep
):
    return service.create_media_episode(db=db, episode=episode, media_id=media_id)


@router.get("/episodes/", response_model=list[schemas.Episode])
def read_episodes(db: SessionDep, skip: int = 0, limit: int = 100):
    episodes = service.get_episodes(db, skip=skip, limit=limit)
    return episodes


# Endcards
@router.post(
    "/endcards/",
    response_model=schemas.Endcards,
)
def create_endcard_for_episode(endcard: schemas.EndcardsCreate, db: SessionDep):
    return service.create_media_endcard(db=db, endcard=endcard)


@router.get("/endcards/", response_model=list[schemas.Endcards])
def read_endcards(db: SessionDep, skip: int = 0, limit: int = 100):
    endcards = service.get_endcards(db, skip=skip, limit=limit)
    return endcards
