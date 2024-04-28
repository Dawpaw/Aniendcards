from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base

class Anime(Base):
    __tablename__ = "anime"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    anilist_url = Column(String, unique=True)
    
    endcards = relationship("Endcard", back_populates="anime")
    
class Endcard(Base):
    __tablename__ = "endcards"
    
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True, index=True)
    anime_id = Column(Integer, ForeignKey("anime.id"))
    episode_number = Column(Integer)
    
    anime = relationship("Anime", back_populates="endcards")
    
    
    
    
    