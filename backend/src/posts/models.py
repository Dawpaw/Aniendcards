from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.database import Base
from src.posts.enums import MediaType, MediaFormat, MediaSeason


# Enums
# Tables
class Media(Base):
    __tablename__ = "media"

    id: Mapped[int] = mapped_column(primary_key=True)
    title_original: Mapped[str]
    title_romaji: Mapped[str]
    title_english: Mapped[str] = mapped_column(nullable=True)
    type: Mapped[MediaType]
    format: Mapped[MediaFormat]
    description: Mapped[str]
    season: Mapped[MediaSeason]
    season_year: Mapped[int]
    episodes_count: Mapped[int]
    chapters_count: Mapped[int]
    cover_image: Mapped[str]

    # titles: Mapped["MediaTitles"] = relationship(back_populates="media")
    external_links: Mapped[list["MediaLinks"]] = relationship(back_populates="media")
    episodes: Mapped[list["Episodes"]] = relationship(back_populates="media")


# class MediaTitles(Base):
#     __tablename__ = "media_titles"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))
#     original: Mapped[str]
#     english: Mapped[str]
#     romaji: Mapped[str]

#     media: Mapped["Media"] = relationship(back_populates="titles")


class MediaLinks(Base):
    __tablename__ = "media_links"

    id: Mapped[int] = mapped_column(primary_key=True)
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))
    link: Mapped[str]

    media: Mapped["Media"] = relationship(back_populates="external_links")


class Episodes(Base):
    __tablename__ = "episodes"

    id: Mapped[int] = mapped_column(primary_key=True)
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))
    description: Mapped[str]
    episode_number: Mapped[int]

    media: Mapped["Media"] = relationship(back_populates="episodes")
    endcards: Mapped[list["Endcards"]] = relationship(back_populates="episode")


class Endcards(Base):
    __tablename__ = "endcards"

    id: Mapped[int] = mapped_column(primary_key=True)
    episode_id: Mapped[int] = mapped_column(ForeignKey("episodes.id"))
    artist_id: Mapped[int] = mapped_column(ForeignKey("artists.id"))
    img_url: Mapped[str]
    alt_img_url: Mapped[str]
    source_url: Mapped[str]

    episode: Mapped["Episodes"] = relationship(back_populates="endcards")
    artist: Mapped["Artists"] = relationship(back_populates="endcards")


class Artists(Base):
    __tablename__ = "artists"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]

    endcards: Mapped[list["Endcards"]] = relationship(back_populates="artist")
    links: Mapped[list["ArtistsLinks"]] = relationship(back_populates="artist")


class ArtistsLinks(Base):
    __tablename__ = "artists_links"
    id: Mapped[int] = mapped_column(primary_key=True)
    artist_id: Mapped[int] = mapped_column(ForeignKey("artists.id"))
    link: Mapped[str]

    artist: Mapped["Artists"] = relationship(back_populates="links")
