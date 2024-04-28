from sqlalchemy.orm import Session

from src.posts import models, schemas

def get_anime(db:Session, anime_id:int):
    return db.query(models.Anime).filter(models.Anime.id == anime_id).first()

def get_anime_by_anilist_url(db:Session, url:str):
    return db.query(models.Anime).filter(models.Anime.anilist_url == url).first()

def create_anime(db: Session, anime: schemas.AnimeCreate):
    db_anime = models.Anime(**anime.model_dump())
    db.add(db_anime)
    db.commit()
    db.refresh(db_anime)
    return db_anime

def get_animes(db:Session, skip:int= 0, limit:int =100):
    return db.query(models.Anime).offset(skip).limit(limit).all()

def get_endcards(db:Session, skip:int= 0, limit:int =100):
    return db.query(models.Endcard).offset(skip).limit(limit).all()


def create_anime_endcard(db: Session, endcard: schemas.EndcardCreate, anime_db_id: int):
    db_endcard = models.Endcard(**endcard.model_dump(), anime_id = anime_db_id)
    db.add(db_endcard)
    db.commit()
    db.refresh(db_endcard)
    return db_endcard