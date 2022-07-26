"""User related endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from source.database.functions.user import authenticate_user
from source.database.models import User
from source.dependencies.authentication import (
    create_authentication_token,
    create_hashed_password,
)
from source.dependencies.database import get_database_session
from source.schemas.message import Message
from source.schemas.user import Token, UserForm
from source.settings import TOKEN_URL, USER_URL

router = APIRouter(
    prefix=USER_URL,
    tags=["User"],
)


@router.post(
    "/create",
    name="user-create",
    status_code=status.HTTP_201_CREATED,
    description="Create a user in service database",
    response_model=Message,
)
async def create_user(
    user: UserForm = Depends(UserForm.form),
    database_session: Session = Depends(get_database_session),
) -> Message:
    """
    Create a user endpoint.

    Parameters
    ----------
    user : UserForm
        User's email and password, by default Depends(UserForm.form)
    database_session : sqlalchemy.orm.session.Session
        Service database session, by default Depends(get_database_session)

    Returns
    -------
    Message
        Success message.

    Raises
    ------
    fastapi.HTTPException
        If email is already registered.

    """
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
    return Message(detail=f"Email {user.email} registered successfully.")


@router.post(
    TOKEN_URL,
    name="user-token",
    status_code=status.HTTP_200_OK,
    description="Create access token for a user",
    response_model=Token,
)
async def create_user_token(
    user: OAuth2PasswordRequestForm = Depends(),
    database_session: Session = Depends(get_database_session),
) -> Token:
    """
    Create a user token endpoint.

    Parameters
    ----------
    user : OAuth2PasswordRequestForm
        User's username (email) and password, by default Depends()
    database_session : sqlalchemy.orm.session.Session
        Service database session, by default Depends(get_database_session)

    Returns
    -------
    Token
        Authentication token.

    """
    authenticate_user(form_data=user, database_session=database_session)
    authentication_token: Token = create_authentication_token(user.username)
    return authentication_token
