"""User manipulation functions."""

from typing import Optional

from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from source.database.models import User
from source.dependencies.authentication import check_password


def authenticate_user(
    form_data: OAuth2PasswordRequestForm, database_session: Session
) -> None:
    """
    Authenticate user in the service.

    Parameters
    ----------
    form_data : OAuth2PasswordRequestForm
        User's username (email) and password.
    database_session : sqlalchemy.orm.session.Session
        Service database session.

    Raises
    ------
    fastapi.HTTPException
        If Email and/or password are incorrect.

    """
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
