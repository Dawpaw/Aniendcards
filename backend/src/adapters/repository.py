import abc

from sqlalchemy.orm import Session

import src.enums as enums
import src.domain.model as model


class AbstractMediaRepository(abc.ABC):
    @abc.abstractmethod
    def get_media_by_id(self, media_id:int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_media_by_title(self, media_title: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_medias(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_medias_by_type(self, type: enums.MediaType):
        raise NotImplementedError

    @abc.abstractmethod
    def get_medias_by_format(self,  format: enums.MediaFormat):
        raise NotImplementedError

    @abc.abstractmethod
    def add_media(self,  media: model.Media):
        raise NotImplementedError

    @abc.abstractmethod
    def get_entry_by_id(self, entry_id: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_entries(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_entry(self, entry: model.Entry):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_endcards(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_endcard_by_id(self, endcard_id: int):
        raise NotImplementedError

    @abc.abstractmethod
    def add_endcard(self, endcard: model.Endcard):
        raise NotImplementedError

class AbstractArtistRepository(abc.ABC):
    @abc.abstractmethod
    def get_artist_by_id(self, artist_id: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_artist_by_username(self, username: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_artists(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_artist(self, artist: model.Artist):
        raise NotImplementedError

class SqlAlchemyMediaRepository(AbstractMediaRepository):

    def __init__(self, session: Session) -> None:
        super().__init__()
        self.session:Session = session

    def get_media_by_id(self, media_id:int):
        return self.session.query(model.Media).filter_by(id = media_id).one_or_none()

    def get_media_by_title(self, media_title: str):
        return self.session.query(model.Media).join(model.MediaTitle).filter_by(title=media_title).first()

    def get_medias(self):
        return self.session.query(model.Media).all()

    def get_medias_by_type(self, type: enums.MediaType):
        return self.session.query(model.Media).filter_by(type = type).all()

    def get_medias_by_format(self,  format: enums.MediaFormat):
        return self.session.query(model.Media).filter_by(format = format).all()

    def add_media(self,  media: model.Media):
        self.session.add(media)

    def get_entry_by_id(self, entry_id: int):
        return self.session.query(model.Entry).filter_by(id = entry_id).one_or_none()

    def get_entries(self):
        return self.session.query(model.Entry).all()

    def add_entry(self, entry: model.Entry):
        self.session.add(entry)

    def get_endcards(self):
        return self.session.query(model.Endcard).all()

    def get_endcard_by_id(self, endcard_id: int):
        return self.session.query(model.Endcard).filter_by(id = endcard_id).one_or_none()

    def add_endcard(self, endcard: model.Endcard):
        self.session.add(endcard)

class SqlAlchemyArtistRepository(AbstractArtistRepository):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self.session:Session = session

    def get_artist_by_id(self, artist_id: int):
        return self.session.query(model.Artist).filter_by(id = artist_id).one_or_none()

    def get_artist_by_username(self, username: str):
        return self.session.query(model.Artist).filter_by(username = username).one_or_none()

    def get_artists(self):
        return self.session.query(model.Artist).all()

    def add_artist(self, artist: model.Artist):
        self.session.add(artist)