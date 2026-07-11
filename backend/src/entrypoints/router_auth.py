from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import  OAuth2PasswordRequestForm

from src.entrypoints.schemas import requests, responses
from src.entrypoints.dependencies import UowDep, is_user_admin
from src.services import  users
from src.services.commands import  CreateUserCommand

router = APIRouter()

@router.post("/user/", response_model=responses.UserResponse,
                dependencies=[Depends(is_user_admin)])
def create_user(request: requests.CreateUserRequest, uow: UowDep):
    user = users.create_user(
        CreateUserCommand(
            username=request.username,
            password=request.password,
            email=request.email
        ),
        uow
    )
    if user is None:
        raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="User alreaedy exists",
                )
        
    return user

@router.post("/user/role", response_model=responses.UserResponse,
                dependencies=[Depends(is_user_admin)])
def assign_role_to_user(request: requests.AssignRoleRequest, uow: UowDep):
    user = users.assign_role_to_user(
        request.username,
        request.role,
        uow
    )
    return user

@router.get("/users/", response_model=list[responses.UserResponse],
            dependencies=[Depends(is_user_admin)])
def get_all_users(uow: UowDep):
    user = users.get_users(uow)
    return user

# This is just a temporary endpoint
@router.post("/role/", response_model=responses.RoleResponse,
                dependencies=[Depends(is_user_admin)])
def create_role(request: requests.CreateRoleRequest, uow: UowDep):
    role = users.create_role(
        request.name,
        request.description,
        uow
    )
    return role

# Authentication
@router.post("/token", response_model=responses.TokenResponse)
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], uow: UowDep):
    user = users.autheticate_user(form_data.username, form_data.password, uow)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = users.create_auth_token(user)
    return responses.TokenResponse(access_token=access_token, token_type="bearer")
