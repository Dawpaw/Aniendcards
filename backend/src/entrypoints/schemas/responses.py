from pydantic import BaseModel, HttpUrl

from src.enums import MediaSeason, MediaType, MediaFormat, Languages, Roles

class ArtistsLinkResponse(BaseModel):
    link: HttpUrl
    class Config:
        from_attributes = True


class ArtistReponse(BaseModel):
    id: int
    username: str
    links: list[ArtistsLinkResponse] | None
    class Config:
        from_attributes = True

class EndcardResponse(BaseModel):
    id: int
    img_url: HttpUrl
    alt_img_url: HttpUrl | None
    source_url: HttpUrl
    artist: ArtistReponse
    class Config:
        from_attributes = True

class EntryResponse(BaseModel):
    id: int
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
    id: int
    type: MediaType
    format: MediaFormat | None
    season: MediaSeason | None
    season_year: int | None
    cover_image: HttpUrl
    description: str
    titles: list[MediaTitleResponse]
    links: list[MediaLinkResponse] | None
    entries: list[EntryResponse]
    class Config:
        from_attributes = True

class MediaOnlyResponse(BaseModel):
    id: int
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

class UserResponse(BaseModel):
    id: int
    username: str
    roles: list["RoleResponse"] | None

class RoleResponse(BaseModel):
    name: Roles
    description: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str