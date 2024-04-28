from pydantic import BaseModel

class EndcardBase(BaseModel):
    url: str
    episode_number: int
    
class EndcardCreate(EndcardBase):
    pass

class EndCard(EndcardBase):
    anime_id: int
    
    class Config:
        orm_mode = True

class AnimeBase(BaseModel):
    title: str
    anilist_url: str
    
class AnimeCreate(AnimeBase):
    pass 

class Anime(AnimeBase):
    id:int 
    endcards: list[EndCard] = []
    
    class Config:
        orm_mode = True