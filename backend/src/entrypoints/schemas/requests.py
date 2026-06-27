from pydantic import BaseModel, HttpUrl, EmailStr, Field

from src.enums import MediaSeason, MediaType, MediaFormat, Languages, Roles

class CreateArtistsLinkRequest(BaseModel):
    link: HttpUrl

class CreateArtistRequest(BaseModel):
    username: str
    links: list[CreateArtistsLinkRequest] | None

class CreateEncardRequest(BaseModel):
    img_url: HttpUrl
    alt_img_url: HttpUrl | None
    source_url: HttpUrl
    artist_id: int
    entry_id: int

class CreateEntryRequest(BaseModel):
    description: str
    entry_number: float
    endcards: list[int] | None
    media_id: int | None
    media_title: str | None

class CreateMediaLinkRequest(BaseModel):
    link: HttpUrl  

class CreateMediaTitleRequest(BaseModel):
    language: Languages
    title: str

class CreateMediaRequest(BaseModel):
    type: MediaType
    format: MediaFormat | None
    season: MediaSeason | None
    season_year: int | None
    cover_image: HttpUrl
    description: str
    titles: list[CreateMediaTitleRequest]
    links: list[CreateMediaLinkRequest] | None

class CreateUserRequest(BaseModel):
    username: str = Field(pattern=r"^[^\s]+$", 
                            min_length=3, 
                            max_length=20,
                            description="Username cannot contain spaces.")
    password: str = Field(min_length=8, max_length=20)
    email: EmailStr
    
class CreateRoleRequest(BaseModel):
    name: Roles
    description: str