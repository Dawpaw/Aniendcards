from typing import Annotated, Generator

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.entrypoints.schemas import requests, responses
from src.services import services, unit_of_work
from src.services.commands import  CreateUserCommand

router = APIRouter()

# TODO Move this to another file
def get_uow() -> Generator[unit_of_work.SqlAlchemyUnitOfWork, None, None]:
    yield unit_of_work.SqlAlchemyUnitOfWork()
UowDep = Annotated[unit_of_work.SqlAlchemyUnitOfWork, Depends(get_uow)]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



@router.post("/user/", response_model=responses.UserResponse)
def create_user(request: requests.CreateUserRequest, uow: UowDep):
    user = services.create_user(
        CreateUserCommand(
            username=request.username,
            password=request.password,
            email=request.email
        ),
        uow
    )
    return user

# This is just a temporary endpoint
@router.post("/role/", response_model=responses.RoleResponse)
def create_role(request: requests.CreateRoleRequest, uow: UowDep):
    role = services.create_role(
        request.name,
        request.description,
        uow
    )
    return role

# Authentication
@router.post("/token", response_model=responses.TokenResponse)
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], uow: UowDep):
    user = services.autheticate_user(form_data.username, form_data.password, uow)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = services.create_auth_token(user)
    return responses.TokenResponse(access_token=access_token, token_type="bearer")

# Too shallow for my liking
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], uow: UowDep):
    return services.get_current_user(token, uow)

def is_user_admin(current_user = Depends(get_current_user)):
    current_user_admin: bool = services.is_user_admin(current_user)
    if not current_user_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return 