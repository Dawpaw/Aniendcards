from typing import Annotated, Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from src.services import unit_of_work, users

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_uow() -> Generator[unit_of_work.SqlAlchemyUnitOfWork, None, None]:
    yield unit_of_work.SqlAlchemyUnitOfWork()
UowDep = Annotated[unit_of_work.SqlAlchemyUnitOfWork, Depends(get_uow)]


# Too shallow for my liking
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], uow: UowDep):
    return users.get_current_user(token, uow)

def is_user_admin(current_user = Depends(get_current_user)):
    current_user_admin: bool = users.is_user_admin(current_user)
    if not current_user_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return 