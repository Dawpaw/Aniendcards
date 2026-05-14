# The domain model. 
# See Architecture Pattern with Python - Chapter 1

from dataclasses import dataclass, field
from typing import Optional, List

from src.enums import MediaType, MediaSeason, MediaFormat, Languages

from pydantic import HttpUrl

@dataclass
class Media:
    id: int
    type: MediaType
    format: MediaFormat
    description: str
    season: MediaSeason
    season_year: int
    cover_image: str
    titles: List["MediaTitle"] = field(default_factory=list)
    entries: List["Entry"]  = field(default_factory= list)
    links: List["MediaLink"] = field(default_factory=list)

    @property
    def entries_count(self) -> int:
        return len(self.entries)


@dataclass(frozen=True)
class MediaTitle:
    id: int
    language: Languages
    title: str

@dataclass(frozen=True)
class MediaLink(): 
    id: int
    link: HttpUrl

# Can be either an episode or a chapter
@dataclass
class Entry: 
    id: int
    description: Optional[str]
    entry_number: float
    endcards: List["Endcard"] = field(default_factory=list)

@dataclass
class Endcard:
    id: int
    img_url: str
    alt_img_url: Optional[str]
    source_url: str
    artist: "Artist"

@dataclass
class Artist:
    id: int
    username: str
    links: "ArtistLink"

@dataclass(frozen=True)
class ArtistLink:
    id: int
    link: HttpUrl

