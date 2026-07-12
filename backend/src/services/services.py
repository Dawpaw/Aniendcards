import src.domain.model as model
from src.services.commands import CreateMediaCommand, CreateEntryCommand, CreateEndcardCommand, CreateArtistCommand
from src.services.unit_of_work import SqlAlchemyUnitOfWork


def create_media(request: CreateMediaCommand, uow: SqlAlchemyUnitOfWork):
    with uow:
        titles = [t.title for t in request.titles]
        media_exist = [uow.medias.get_media_by_title(title) for title in titles]
        if any(media_exist):
            return None
        media = model.Media(
                type=request.type,
                format=request.format,
                description=request.description, 
                season=request.season,
                season_year=request.season_year,
                cover_image=request.cover_image,
                titles=[model.MediaTitle(language=t.language, title=t.title) for t in request.titles],
                entries=[],
                links=[model.MediaLink(link=link) for link in request.links] if request.links else []
        )
        uow.medias.add_media(media)
        uow.commit()
        return media

def create_entry(request: CreateEntryCommand, uow: SqlAlchemyUnitOfWork):
    with uow:
        endcards = []
        if request.endcards:
            endcards = [uow.medias.get_endcard_by_id(endcard_id) for endcard_id in request.endcards]
    
        entry = model.Entry(
                    description=request.description,
                    entry_number=request.entry_number, 
                    endcards=endcards
        )

        uow.medias.add_entry(entry)
        
        # Update the media
        media:model.Media | None = uow.medias.get_media_by_id(request.media_id) if request.media_id  \
                    else uow.medias.get_media_by_title(request.media_title) if request.media_title \
                    else None 
        if media is None:
            # TODO confirm if this is needed 
            uow.rollback()
            return None 
        media.entries.append(entry)
        uow.medias.add_media(media)
        uow.commit()
        return entry

def create_endcard(request: CreateEndcardCommand, uow: SqlAlchemyUnitOfWork):
    with uow:
        artist = uow.artists.get_artist_by_id(request.artist_id)
        if not artist:
            return None
        endcard = model.Endcard(
                img_url= request.img_url,
                alt_img_url= request.alt_img_url,
                source_url=request.source_url,
                artist=artist
        )
        uow.medias.add_endcard(endcard)
        # Update the entry
        entry = uow.medias.get_entry_by_id(request.entry_id)
        if entry is None:
            # TODO confirm if this is needed 
            uow.rollback()
            return None
        entry.endcards.append(endcard)
        uow.medias.add_entry(entry)
        uow.commit()
        return endcard

def create_artist(request: CreateArtistCommand, uow: SqlAlchemyUnitOfWork):
    with uow:
        artist_exist = uow.artists.get_artist_by_username(request.username)
        if artist_exist:
            return None
        artist = model.Artist(
                username=request.username, 
                links=[model.ArtistLink(link=link) for link in request.links] if request.links else None
        )
        uow.artists.add_artist(artist)
        uow.commit()
        return artist
    


def get_all_media(uow: SqlAlchemyUnitOfWork):
    with uow:
        medias = uow.medias.get_medias()
        uow.commit()
        return medias

def get_media_by_id(id: int , uow: SqlAlchemyUnitOfWork):
    with uow:
        media = uow.medias.get_media_by_id(id)
        uow.commit()
        return media

def get_media_by_title(title: str , uow: SqlAlchemyUnitOfWork):
    with uow:
        media = uow.medias.get_media_by_title(title)
        uow.commit()
        return media


def get_artists(uow: SqlAlchemyUnitOfWork):
    with uow:
        artists = uow.artists.get_artists()
        return artists

def get_artist_by_username(username: str, uow: SqlAlchemyUnitOfWork):
    with uow:
        artist = uow.artists.get_artist_by_username(username)
        uow.commit()
        return artist

def get_artist_by_id(artists_id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        artist = uow.artists.get_artist_by_id(artists_id)
        uow.commit()
        return artist


def get_endcards(uow: SqlAlchemyUnitOfWork):
    with uow:
        endcards = uow.medias.get_endcards()
        uow.commit()
        return endcards

def get_endcard_by_id(endcard_id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        endcard = uow.medias.get_endcard_by_id(endcard_id)
        uow.commit()
        return endcard
    
def delete_media_by_id(media_id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        media = uow.medias.get_media_by_id(media_id)
        uow.medias.delete_media_by_id(media.id)
        uow.commit()
        return media
    

def delete_entry_by_id(entry_id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        entry = uow.medias.get_endcard_by_id(entry_id)
        uow.medias.delete_entry_by_id(entry.id)
        uow.commit()
        return entry

def delete_endcard_by_id(endcard_id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        endcard = uow.medias.get_endcard_by_id(endcard_id)
        uow.medias.delete_endcard_by_id(endcard.id)
        uow.commit()
        return endcard

def delete_artist_by_id(entry_id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        artist = uow.artists.get_artist_by_id(entry_id)
        uow.artists.delete_artist_by_id(artist.id)
        uow.commit()
        return artist