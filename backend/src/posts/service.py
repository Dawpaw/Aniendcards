from sqlalchemy.orm import Session

from src.posts import models, schemas
from src.posts.enums import MediaFormat, MediaType


# Media
def get_media_by_id(db: Session, media_id: int):
    return db.query(models.Media).filter(models.Media.id == media_id).first()


# TODO This will probably not work
def get_media_by_title(db: Session, media_title: int):
    return (
        db.query(models.Media).filter(models.Media.title_romaji == media_title).first()
    )


# I know the plural of media is media, but programming does not like this
def get_medias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Media).offset(skip).limit(limit).all()


def get_medias_by_type(db: Session, type: MediaType, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Media)
        .filter(models.Media.type == type)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_medias_by_format(
    db: Session, format: MediaFormat, skip: int = 0, limit: int = 100
):
    return (
        db.query(models.Media)
        .filter(models.Media.format == format)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_media(db: Session, media: schemas.MediaCreate):
    db_media = models.Media(**media.model_dump())
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media


# Episodes
def get_episodes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Episodes).offset(skip).limit(limit).all()


def create_media_episode(db: Session, episode: schemas.EpisodeCreate, media_id: int):
    db_episode = models.Episodes(**episode.model_dump(), media_id=media_id)
    db.add(db_episode)
    db.commit()
    db.refresh(db_episode)
    return db_episode


# Endcards
def get_endcards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Endcards).offset(skip).limit(limit).all()


def create_media_endcard(db: Session, endcard: schemas.EndcardsCreate):
    db_endcard = models.Endcards(**endcard.model_dump())
    db.add(db_endcard)
    db.commit()
    db.refresh(db_endcard)
    return db_endcard


# Artist
def get_artist_by_id(db: Session, artist_id: int):
    return db.query(models.Artists).filter(models.Artists.id == artist_id).first()


def get_artist_by_username(db: Session, username: str):
    return db.query(models.Artists).filter(models.Artists.username == username).first()


def get_artists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Artists).offset(skip).limit(limit).all()


def create_artist(db: Session, artist: schemas.ArtistCreate):
    db_artist = models.Artists(**artist.model_dump())
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist
