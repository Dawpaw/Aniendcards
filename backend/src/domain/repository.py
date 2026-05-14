import abc

from sqlalchemy.orm import Session

import src.enums as enums
import src.domain.model as model


class AbstractRepostiory(abc.ABC):

    @abc.abstractmethod
    def get_media_by_id(self, media_id:int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_media_by_title(self, media_title: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_medias(self, skip: int = 0, limit: int = 100):
        raise NotImplementedError

    @abc.abstractmethod
    def get_medias_by_type(self, type: enums.MediaType, skip: int = 0, limit: int = 100):
        raise NotImplementedError

    @abc.abstractmethod
    def get_medias_by_format(self,  format: enums.MediaFormat, skip: int = 0, limit: int = 100):
        raise NotImplementedError

    @abc.abstractmethod
    def add_media(self,  media: model.Media):
        raise NotImplementedError

    @abc.abstractmethod
    def get_entries(self, skip: int = 0, limit: int = 100):
        raise NotImplementedError

    @abc.abstractmethod
    def add_entry(self, entry: model.Entry):
        raise NotImplementedError

    @abc.abstractmethod
    def get_endcards(self, skip: int = 0, limit: int = 100):
        raise NotImplementedError

    @abc.abstractmethod
    def get_endcard_by_id(self, endcard_id: int):
        raise NotImplementedError

    @abc.abstractmethod
    def add_endcard(self, endcard: model.Endcard):
        raise NotImplementedError

    @abc.abstractmethod
    def get_artist_by_id(self, artist_id: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_artist_by_username(self, username: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_artists(self, skip: int = 0, limit: int = 100):
        raise NotImplementedError

    @abc.abstractmethod
    def add_artist(self, artist: model.Artist):
        raise NotImplementedError
    

class SqlAlchemyRepository(AbstractRepostiory):

    def __init__(self, session: Session) -> None:
        super().__init__()
        self.session:Session = session

    def get_media_by_id(self, media_id:int):
        return self.session.query(model.Media).filter_by(id = media_id).one()

    def get_media_by_title(self, media_title: str):
        raise NotImplementedError

    def get_medias(self, skip: int = 0, limit: int = 100):
        return self.session.query(model.Media).offset(skip).limit(limit).all()

    def get_medias_by_type(self, type: enums.MediaType, skip: int = 0, limit: int = 100):
        return self.session.query(model.Media).filter_by(type = type).offset(skip).limit(limit).all()

    def get_medias_by_format(self,  format: enums.MediaFormat, skip: int = 0, limit: int = 100):
        return self.session.query(model.Media).filter_by(format = format).offset(skip).limit(limit).all()

    def add_media(self,  media: model.Media):
        self.session.add(media)

    def get_entries(self, skip: int = 0, limit: int = 100):
        return self.session.query(model.Entry).offset(skip).limit(limit).all()

    def add_entry(self, entry: model.Entry):
        self.session.add(entry)

    def get_endcards(self, skip: int = 0, limit: int = 100):
        return self.session.query(model.Endcard).offset(skip).limit(limit).all()

    def get_endcard_by_id(self, endcard_id: int):
        return self.session.query(model.Endcard).filter_by(id = endcard_id).one()

    def add_endcard(self, endcard: model.Endcard):
        self.session.add(endcard)

    def get_artist_by_id(self, artist_id: int):
        return self.session.query(model.Artist).filter_by(id = artist_id).one()

    def get_artist_by_username(self, username: str):
        return self.session.query(model.Artist).filter_by(username = username).one()

    def get_artists(self, skip: int = 0, limit: int = 100):
        return self.session.query(model.Artist).offset(skip).limit(limit).all()

    def add_artist(self, artist: model.Artist):
        self.session.add(artist)

