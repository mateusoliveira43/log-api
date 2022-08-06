"""User manipulation functions."""

from typing import Optional

from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from source.database.models import User
from source.dependencies.authentication import (
    check_password,
    create_hashed_password,
)
from source.dependencies.database import get_database_session
from source.schemas.user import UserForm


def register_user(user: UserForm) -> None:
    """
    Register a user in service database.

    Parameters
    ----------
    user : UserForm
        User information.

    Raises
    ------
    HTTPException
        If email is already registered.

    """
    with get_database_session() as database_session:
        if database_session.query(User).filter_by(email=user.email).first():
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Email {user.email} is already registered.",
            )
        database_session.add(
            User(
                email=user.email,
                hashed_password=create_hashed_password(user.password),
            )
        )
        database_session.commit()


def authenticate_user(form_data: OAuth2PasswordRequestForm) -> None:
    """
    Authenticate user in the service.

    Parameters
    ----------
    form_data : OAuth2PasswordRequestForm
        User's username (email) and password.

    Raises
    ------
    fastapi.HTTPException
        If Email and/or password are incorrect.

    """
    with get_database_session() as database_session:
        user: Optional[User] = (
            database_session.query(User)
            .filter_by(email=form_data.username)
            .first()
        )
    if not user or not check_password(
        form_data.password, user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email and/or password incorrect",
        )
