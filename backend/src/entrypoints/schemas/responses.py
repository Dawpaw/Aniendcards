from pydantic import BaseModel, HttpUrl

from src.enums import MediaSeason, MediaType, MediaFormat, Languages

class ArtistsLinkResponse(BaseModel):
    link: HttpUrl
    class Config:
        from_attributes = True


class ArtistReponse(BaseModel):
    username: str
    links: list[ArtistsLinkResponse] | None
    class Config:
        from_attributes = True

class EndcardResponse(BaseModel):
    img_url: HttpUrl
    alt_img_url: HttpUrl | None
    source_url: HttpUrl
    artist: ArtistReponse
    class Config:
        from_attributes = True

class EntryResponse(BaseModel):
    description: str
    entry_number: float
    endcards: list[EndcardResponse] = []
    class Config:
        from_attributes = True

class MediaLinkResponse(BaseModel):
    link: HttpUrl
    class Config:
        from_attributes = True

class MediaTitleResponse(BaseModel):
    language: Languages
    title: str
    class Config:
        from_attributes = True

class MediaResponse(BaseModel):
    type: MediaType
    format: MediaFormat | None
    season: MediaSeason | None
    season_year: int | None
    cover_image: HttpUrl
    description: str
    titles: list[MediaTitleResponse]
    links: list[MediaLinkResponse] | None
    class Config:
        from_attributes = True
