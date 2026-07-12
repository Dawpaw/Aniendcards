from sqlalchemy import ForeignKey, Table, Column, Integer, String, Text, Float, Boolean, DateTime
from sqlalchemy.orm import registry, relationship
from sqlalchemy.sql import func

from enum import StrEnum

import src.domain.model as model


mapper_registry = registry()
metadata = mapper_registry.metadata

class ForeignKeyConstraintType(StrEnum):
    CASCADE = "CASCADE"
    RESTRICT = "RESTRICT"
    SET_NULL = "SET NULL"


media = Table(
    "media", 
    metadata, 
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("type", String(5)), 
    Column("format", String), 
    Column("description", Text), 
    Column("season", String), 
    Column("season_year", String), 
    Column("cover_image", String)
)

media_titles = Table(
    "media_titles", 
    metadata, 
    Column("id", Integer, primary_key=True, autoincrement=True), 
    Column("media_id", ForeignKey("media.id", ondelete=ForeignKeyConstraintType.CASCADE)), 
    Column("language", String(8)),
    Column("title", String, unique=True)
)


media_links = Table(
    "media_links", 
    metadata, 
    Column("id", Integer, primary_key=True, autoincrement=True), 
    Column("media_id", ForeignKey("media.id", ondelete=ForeignKeyConstraintType.CASCADE)), 
    Column("link", String)
)

entries = Table(
    "entries", 
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True), 
    Column("media.id", ForeignKey("media.id", ondelete=ForeignKeyConstraintType.CASCADE)),
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
    Column("artist_id", ForeignKey("artists.id", ondelete=ForeignKeyConstraintType.CASCADE)), 
    Column("link", String)
)

endcards = Table(
    "endcards",
    metadata, 
    Column("id", Integer, primary_key=True, autoincrement=True), 
    Column("entry_id", ForeignKey("entries.id", ondelete=ForeignKeyConstraintType.SET_NULL)), 
    Column("artist_id", ForeignKey("artists.id", ondelete=ForeignKeyConstraintType.SET_NULL)), 
    Column("img_url", String), 
    Column("alt_img_url", String, nullable=True),
    Column("source_url", String)
)

users = Table(
    "users", 
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String, nullable=False, unique=True),
    Column("password", String, nullable=False),
    Column("email", String, unique=True),
    Column("is_active", Boolean, default=True),
    Column("created_at", DateTime, default=func.now() )
)

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, unique=True, index=True),
    Column("description", Text)
)

user_roles = Table(
    "user_roles", 
    metadata,
    Column("user_id", ForeignKey("users.id", ondelete=ForeignKeyConstraintType.CASCADE)),
    Column("role_id", ForeignKey("roles.id", ondelete=ForeignKeyConstraintType.CASCADE))
)

def start_mappers():
    media_mapper = mapper_registry.map_imperatively(
                            model.Media,
                            media,
                            properties = {
                                "titles": relationship(model.MediaTitle, collection_class=list, lazy="joined"), 
                                "entries" : relationship(model.Entry, collection_class=list, lazy="joined"),
                                "links" : relationship(model.MediaLink, collection_class=list, lazy="joined")
                            }
    )

    media_links_mapper = mapper_registry.map_imperatively(model.MediaLink, media_links)

    media_title_mapper = mapper_registry.map_imperatively(model.MediaTitle, media_titles)

    entries_mapper = mapper_registry.map_imperatively(
                            model.Entry, 
                            entries, 
                            properties = {
                                "endcards": relationship(model.Endcard, collection_class=list, lazy="joined")
                            })

    artists_mapper = mapper_registry.map_imperatively(
                            model.Artist, 
                            artists,
                            properties = {
                                "links" : relationship(model.ArtistLink, lazy="joined") 
                            }
    )

    artist_links_mapper = mapper_registry.map_imperatively(model.ArtistLink, artist_links)

    endcards_mapper  = mapper_registry.map_imperatively(
                            model.Endcard, 
                            endcards,
                            properties = {
                                "artist" : relationship(model.Artist, lazy="joined")
                            }
    )

    roles_mapper = mapper_registry.map_imperatively(model.Role, roles)

    users_mapper = mapper_registry.map_imperatively(
                            model.User, 
                            users,
                            properties = {
                                "roles": relationship(model.Role, secondary=user_roles, collection_class=list, lazy="joined")
                            })
