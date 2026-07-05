from datetime import timedelta

from src.enums import Roles as RolesEnum
from src.config import ACCESS_TOKEN_EXPIRE_MINUTES
import src.domain.model as model
from src.services.commands import CreateMediaCommand, CreateEntryCommand, CreateEndcardCommand, CreateArtistCommand, CreateUserCommand
from src.services.exceptions import CreateException, GetException, DeleteException
from src.services.unit_of_work import SqlAlchemyUnitOfWork

from src.services.security import hash_password, verify_password, create_access_token, decode_access_token

def create_media(request: CreateMediaCommand, uow: SqlAlchemyUnitOfWork):
    with uow:
        titles = [t.title for t in request.titles]
        media_exist = [uow.medias.get_media_by_title(title) for title in titles]
        if any(media_exist):
            raise CreateException("Media already exist") 
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
            raise CreateException("Media does not exist")
        media.entries.append(entry)
        uow.medias.add_media(media)
        uow.commit()
        return entry

def create_endcard(request: CreateEndcardCommand, uow: SqlAlchemyUnitOfWork):
    with uow:
        artist = uow.artists.get_artist_by_id(request.artist_id)
        if not artist:
            raise CreateException("Artist does not exist")
        endcard = model.Endcard(
                img_url= request.img_url,
                alt_img_url= request.alt_img_url,
                source_url=request.source_url,
                artist=artist
        )
        uow.medias.add_endcard(endcard)
        # Update the entry
        entry = uow.medias.get_endcard_by_id(request.entry_id)
        if entry is None:
            raise CreateException("Entry does not exist")
        entry.endcards.append(endcard)
        uow.medias.add_entry(entry)
        uow.commit()
        return endcard

def create_artist(request: CreateArtistCommand, uow: SqlAlchemyUnitOfWork):
    with uow:
        artist_exist = uow.artists.get_artist_by_username(request.username)
        if artist_exist:
            raise CreateException("Artist already exist")
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
        if not medias:
            raise GetException("No medias found") 
        uow.commit()
        return medias

def get_media_by_id(id: int , uow: SqlAlchemyUnitOfWork):
    with uow:
        media = uow.medias.get_media_by_id(id)
        if not media:
            raise GetException("Media does not exist") 
        uow.commit()
        return media

def get_media_by_title(title: str , uow: SqlAlchemyUnitOfWork):
    with uow:
        media = uow.medias.get_media_by_title(title)
        if not media:
            raise GetException("Media does not exist") 
        uow.commit()
        return media


def get_artists(uow: SqlAlchemyUnitOfWork):
    with uow:
        artists = uow.artists.get_artists()
        if not artists:
            raise GetException("No artist exist")
        uow.commit()
        return artists

def get_artist_by_username(username: str, uow: SqlAlchemyUnitOfWork):
    with uow:
        artist = uow.artists.get_artist_by_username(username)
        if not artist:
            raise GetException("No artist exist")
        uow.commit()
        return artist

def get_artist_by_id(artists_id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        artist = uow.artists.get_artist_by_id(artists_id)
        if not artist:
            raise GetException("No artist exist")
        uow.commit()
        return artist


def get_endcards(uow: SqlAlchemyUnitOfWork):
    with uow:
        endcards = uow.medias.get_endcards()
        if not endcards:
            raise GetException("No endcard exist")
        uow.commit()
        return endcards

def get_endcard_by_id(endcard_id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        endcard = uow.medias.get_endcard_by_id(endcard_id)
        if not endcard:
            raise GetException("Endcard not found")
        uow.commit()
        return endcard
    
def delete_media_by_id(media_id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        media = uow.medias.get_media_by_id(media_id)
        if not media:
            raise DeleteException(("Media not found"))
        uow.medias.delete_endcard_by_id(media.id)
        uow.commit()
        return media
    

def delete_entry_by_id(entry_id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        entry = uow.medias.get_endcard_by_id(entry_id)
        if not entry:
            raise DeleteException("Entry not found")
        uow.medias.delete_entry_by_id(entry.id)
        uow.commit()
        return entry

def delete_endcard_by_id(endcard_id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        endcard = uow.medias.get_endcard_by_id(endcard_id)
        if not endcard:
            raise DeleteException("Endcard not found")
        uow.medias.delete_endcard_by_id(endcard.id)
        uow.commit()
        return endcard

def delete_artist_by_id(entry_id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        artist = uow.artists.get_artist_by_id(entry_id)
        if not artist:
            raise DeleteException("Artist not found")
        uow.artists.delete_artist_by_id(artist.id)
        uow.commit()
        return artist

        
# TODO Move the user services 
def to_domain_user(orm_user) -> model.User:
    return model.User(
        username=orm_user.username,
        password=orm_user.password,
        email=orm_user.email,
        roles=[model.Role(o.name, o.description) for o in orm_user.roles],
        is_active=orm_user.is_active
    )

def create_user(request: CreateUserCommand, uow: SqlAlchemyUnitOfWork):
    hashed_password = hash_password(request.password)
    with uow: 
        previous_user = uow.users.get_user_by_username(username=request.username.lower())
        default_role: list[model.Role] = [uow.users.get_role_by_name(role_name=RolesEnum.NUMBERS)]
        if (previous_user is not None):
            raise CreateException("User already exists") 
        
        user = model.User(
            username=request.username.lower(),
            password=hashed_password,
            email=request.email,
            roles=default_role,
            is_active=True
        )
        uow.users.add_user(user)
        uow.commit()
        return user

def autheticate_user(username: str, password: str, uow: SqlAlchemyUnitOfWork):
    with uow:
        user = uow.users.get_user_by_username(username.lower())
        if user is None:
            raise Exception("Wrong user information") # TODO remove all this exceptions
        
        if not verify_password(password, user.password):
            raise Exception("Wrong user information")
        return to_domain_user(user)

def create_auth_token(user: model.User) -> str:
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"data": user.username}, expires_delta=access_token_expires
    )
    return access_token
    
def get_current_user(token: str, uow: SqlAlchemyUnitOfWork):
    payload = decode_access_token(token)
    username = payload.get("data")
    if username is None:
        raise Exception("Something went wrong with the user")
    with uow:
        user = uow.users.get_user_by_username(username)
        if user is None:
            raise Exception("Something went wrong with the user")
        return to_domain_user(user)
    

def create_role(role_name: RolesEnum, description:str , uow: SqlAlchemyUnitOfWork):
    with uow:
        prev_role = uow.users.get_role_by_name(role_name.lower())
        if prev_role is not None:
            raise Exception("Role already exists")
        role = model.Role(
            name=role_name,
            description=description
        )

        uow.users.add_role(role)
        uow.commit()
        return role
