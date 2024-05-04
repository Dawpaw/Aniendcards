from enum import StrEnum


class MediaType(StrEnum):
    ANIME = "ANIME"
    MANGA = "MANGA"


class MediaFormat(StrEnum):
    TV = "TV"
    TV_SHORT = "TV_SHORT"
    MOVIE = "MOVIE"
    SPECIAL = "SPECIAL"
    OVA = "OVA"
    ONA = "ONA"
    MUSIC = "MUSIC"
    MANGA = "MANGA"
    NOVEL = "NOVEL"
    ONE_SHOT = "ONE_SHOT"


class MediaSeason(StrEnum):
    WINTER = "WINTER"
    SPRINT = "SPRING"
    SUMMER = "SUMMER"
    FALL = "FALL"
