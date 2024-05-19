from pydantic import BaseModel

from src.posts.enums import MediaSeason, MediaType, MediaFormat


# MediaTitles
# class MediaTitlesBase(BaseModel):
#     original: str
#     english: str
#     romaji: str


# class MediaTitlesCreate(MediaTitlesBase):
#     pass


# class MediaTitles(MediaTitlesBase):
#     id: int
#     media_id: int

#     class Config:
#         from_attributes = True


# MediaLinks
class MediaLinksBase(BaseModel):
    link: str


class MediaLinksCreate(MediaLinksBase):
    pass


class MediaLinks(MediaLinksBase):
    id: int
    media_id: int

    class Config:
        from_attributes = True


# ArtistsLinks
class ArtistsLinksBase(BaseModel):
    link: str


class ArtistsLinksCreate(ArtistsLinksBase):
    pass


class ArtistsLinks(ArtistsLinksBase):
    id: int
    artist_id: int

    class Config:
        from_attributes = True


# Endcards


class EndcardsBase(BaseModel):
    img_url: str
    alt_img_url: str
    source_url: str
    episode_id: int
    artist_id: int


class EndcardsCreate(EndcardsBase):
    pass


class Endcards(EndcardsBase):
    id: int

    class Config:
        from_attributes = True


# Artist
class ArtistBase(BaseModel):
    username: str


class ArtistCreate(ArtistBase):
    pass


class Artist(ArtistBase):
    id: int
    endcards: list[Endcards] = []
    links: list[ArtistsLinks] = []

    class Config:
        from_attributes = True


# Episodes
class EpisodeBase(BaseModel):
    description: str
    episode_number: int


class EpisodeCreate(EpisodeBase):
    pass


class Episode(EpisodeBase):
    id: int
    media_id: int
    endcards: list[Endcards] = []

    class Config:
        from_attributes = True


# Media
class MediaBase(BaseModel):
    title_original: str
    title_romaji: str
    title_english: str
    type: MediaType
    format: MediaFormat
    description: str
    season: MediaSeason
    season_year: int
    episodes_count: int
    chapters_count: int
    cover_image: str


class MediaCreate(MediaBase):
    pass


class Media(MediaBase):
    id: int
    external_links: list[MediaLinks] = []
    episodes: list[Episode] = []

    class Config:
        from_attributes = True


class MediaLazy(MediaBase):
    id: int

    class Config:
        from_attributes = True


class EpisodeLazy(EpisodeBase):
    id: int
    media_id: int
    media: MediaLazy

    class Config:
        from_attributes = True


class ArtistLazy(ArtistBase):
    id: int
    links: list[ArtistsLinks] = []

    class Config:
        from_attributes = True


class EndcardsLazy(EndcardsBase):
    id: int
    episode: EpisodeLazy
    artist: ArtistLazy

    class Config:
        from_attributes = True
