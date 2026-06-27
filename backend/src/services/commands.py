from dataclasses import dataclass

from src.enums import MediaSeason, MediaType, MediaFormat, Languages


@dataclass
class MediaTitle:
    language: Languages
    title: str


@dataclass
class CreateMediaCommand:  
    type: MediaType
    format: MediaFormat | None
    season: MediaSeason | None
    season_year: int | None
    cover_image: str
    description: str
    titles: list[MediaTitle]
    links: list[str] | None

@dataclass 
class CreateEntryCommand:
    description: str
    entry_number: float
    endcards: list[int] | None
    media_id: int | None
    media_title: str | None


@dataclass
class CreateEndcardCommand:
    img_url: str
    alt_img_url: str | None
    source_url: str
    artist_id: int
    entry_id: int

@dataclass 
class CreateArtistCommand:
    username: str
    links: list[str] | None
    

@dataclass
class CreateUserCommand:
    username: str
    password: str
    email: str