from sqlalchemy import ForeignKey, MetaData, Table, Column, Integer, String, Date, Text, Float
from sqlalchemy.orm import registry, relationship, Mapped, mapped_column

from src.database import Base
from src.enums import MediaType, MediaFormat, MediaSeason
import backend.src.domain.model as model


mapper_registry = registry()
metadata = mapper_registry.metadata


media = Table(
    "media", 
    metadata, 
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("type", String(5)), 
    Column("format", String), 
    Column("description", Text), 
    Column("season", String), 
    Column("season_year", String), 
)

media_titles = Table(
    "media_titles", 
    metadata, 
    Column("id", Integer, primary_key=True, autoincrement=True), 
    Column("media_id", ForeignKey("media.id")), 
    Column("language", String(8)),
    Column("title", String)
)


media_links = Table(
    "media_links", 
    metadata, 
    Column("id", Integer, primary_key=True, autoincrement=True), 
    Column("media_id", ForeignKey("media.id")), 
    Column("link", String)
)

entries = Table(
    "entries", 
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True), 
    Column("media.id", ForeignKey("media.id")),
    Column("description", Text, nullable=True),
    Column("entry_number", Float), 
)

artists = Table(
    "artists", 
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True), 
    Column("username", String(255))
)

artist_links = Table(
    "artists_links", 
    metadata, 
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("artist_id", ForeignKey("artists.id")), 
    Column("link", String)
)

endcards = Table(
    "endcards",
    metadata, 
    Column("id", Integer, primary_key=True, autoincrement=True), 
    Column("entry_id", ForeignKey("entries.id")), 
    Column("artist_id", ForeignKey("artists.id")), 
    Column("img_url", String), 
    Column("alt_img_url", String, nullable=True),
    Column("source_url", String)
)

def start_mappers():
    media_mapper = mapper_registry.map_imperatively(
                            model.Media,
                            media,
                            properties = {
                                "titles": relationship(model.MediaTitle, collection_class=list), 
                                "entries" : relationship(model.Entry, collection_class=list),
                                "links" : relationship(model.MediaLink, collection_class=list)
                            }
    )

    media_links_mapper = mapper_registry.map_imperatively(model.MediaLink, media_links)

    media_title_mapper = mapper_registry.map_imperatively(model.MediaTitle, media_titles)

    entries_mapper = mapper_registry.map_imperatively(
                            model.Entry, 
                            entries, 
                            properties = {
                                "endcards": relationship(model.Endcard, collection_class=list)
                            })

    artists_mapper = mapper_registry.map_imperatively(
                            model.Artist, 
                            artists,
                            properties = {
                                "links" : relationship(model.ArtistLink) 
                            }
    )

    artist_links_mapper = mapper_registry.map_imperatively(model.ArtistLink, artist_links)

    endcards_mapper  = mapper_registry.map_imperatively(
                            model.Endcard, 
                            endcards,
                            properties = {
                                "artist" : relationship(model.Artist)
                            }
    )