import abc


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from src import config
from src.adapters import repository


class AbstractUnitOfWork(abc.ABC):
    medias: repository.AbstractMediaRepository
    artists: repository.AbstractArtistRepository

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc, tb):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
    
DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(config.get_postgres_uri()),
    expire_on_commit=False
)

class SqlAlchemyUnitOfWork(AbstractUnitOfWork):

    def __init__(self, session_factory = DEFAULT_SESSION_FACTORY) -> None:
        self.session_factory = session_factory

    def __enter__(self) -> AbstractUnitOfWork:
        self.session: Session = self.session_factory()
        self.medias = repository.SqlAlchemyMediaRepository(self.session)
        self.artists = repository.SqlAlchemyArtistRepository(self.session)
        return super().__enter__()
    
    def __exit__(self, exc_type, exc, tb):
        super().__exit__(exc_type, exc, tb)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()