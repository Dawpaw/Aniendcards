from datetime import timedelta

from src.enums import Roles as RolesEnum
from src.config import ACCESS_TOKEN_EXPIRE_MINUTES
import src.domain.model as model
from src.services.commands import CreateUserCommand
from src.services.unit_of_work import SqlAlchemyUnitOfWork

from src.services.security import hash_password, verify_password, create_access_token, decode_access_token

        
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
            return None
        
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
    
def is_user_admin(current_user: model.User):
    return any(role.name in (RolesEnum.SHADOW, RolesEnum.ALPHA, RolesEnum.BETA) for role in current_user.roles)

def create_role(role_name: RolesEnum, description:str , uow: SqlAlchemyUnitOfWork):
    with uow:
        prev_role = uow.users.get_role_by_name(role_name)
        if prev_role is not None:
            raise Exception("Role already exists")
        role = model.Role(
            name=role_name,
            description=description
        )

        uow.users.add_role(role)
        uow.commit()
        return role
    
# TODO clean this
def assign_role_to_user(username: str, role_name:RolesEnum, uow: SqlAlchemyUnitOfWork):
    with uow:
        user = uow.users.get_user_by_username(username=username.lower())
        role = uow.users.get_role_by_name(role_name)
        if role is None or user is None:
            raise Exception("Role or user does not exists")

        user.roles.append(role)
        uow.commit()
        return user


def get_users(uow: SqlAlchemyUnitOfWork):
    with uow:
        users = uow.users.get_users()
        uow.commit()
        return users