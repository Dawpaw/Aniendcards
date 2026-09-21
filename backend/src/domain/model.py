# The domain model. 
# See Architecture Pattern with Python - Chapter 1

from dataclasses import dataclass, field
from typing import Optional, List

from src.enums import MediaType, MediaSeason, MediaFormat, Languages, Roles

@dataclass
class Media:
    type: MediaType
    format: Optional[MediaFormat]
    description: str
    season: Optional[MediaSeason]
    season_year: Optional[int]
    cover_image: str
    titles: List["MediaTitle"] = field(default_factory=list)
    entries: List["Entry"]  = field(default_factory= list)
    links: List["MediaLink"] = field(default_factory=list)

    @property
    def entries_count(self) -> int:
        return len(self.entries)


@dataclass
class MediaTitle:
    language: Languages
    title: str

@dataclass
class MediaLink(): 
    link: str

# Can be either an episode or a chapter
@dataclass
class Entry: 
    description: Optional[str]
    entry_number: float
    endcards: List["Endcard"] = field(default_factory=list)

@dataclass
class Endcard:
    img_url_large: str
    img_url_medium: str
    img_url_small: str
    alt_img_url: Optional[str]
    source_url: str
    artist: "Artist"

@dataclass
class Artist:
    username: str
    links: Optional[List["ArtistLink"]]

@dataclass
class ArtistLink:
    link: str

# User
@dataclass 
class Role:
    name: Roles
    description: str

@dataclass
class User:
    username: str
    password: str
    email: str
    roles: List[Role]
    is_active: bool

