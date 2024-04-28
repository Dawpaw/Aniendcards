from fastapi import APIRouter, HTTPException

from src.posts import models, schemas, service
from src.database import  engine
from src.posts.dependecies import SessionDep

models.Base.metadata.create_all(bind=engine)

router = APIRouter()



@router.post('/animes/', response_model=schemas.Anime)
def create_anime(anime: schemas.AnimeCreate, db: SessionDep):
    db_anime = service.get_anime_by_anilist_url(db, url=anime.anilist_url)
    if db_anime:
        raise HTTPException(status_code=400, detail="Anime already exists")
    return service.create_anime(db=db, anime=anime)

@router.get('/animes/', response_model=list[schemas.Anime])
def read_animes(db:SessionDep, skip: int = 0, limit: int = 100):
    animes = service.get_animes(db, skip=skip, limit=limit)
    return animes

@router.get('/animes/{anime_id}', response_model=schemas.Anime)
def read_anime(db:SessionDep, anime_id:int):
    db_anime = service.get_anime(db, anime_id=anime_id)
    if db_anime is None:
        raise HTTPException(status_code=400, detail="Anime not found")
    return db_anime

@router.post('/animes/{anime_id}/endcards/', response_model=schemas.EndCard)
def create_endcard_for_anime(anime_id: int, endcard: schemas.EndcardCreate, db:SessionDep):
    return service.create_anime_endcard(db=db, endcard=endcard, anime_db_id=anime_id)

@router.get('/endcards/', response_model=list[schemas.EndCard])
def read_endcards(db:SessionDep, skip: int = 0, limit: int = 100):
    endcards = service.get_endcards(db, skip=skip, limit=limit)
    return endcards