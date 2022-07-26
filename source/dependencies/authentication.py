"""Authentication related functions."""

from datetime import datetime, timedelta

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.hash import bcrypt

from source.schemas.user import JWTToken, Token
from source.settings import (
    TOKEN_ALGORITHM,
    TOKEN_EXPIRATION_TIME,
    TOKEN_SECRET_KEY,
    TOKEN_URL,
    USER_URL,
)


def create_hashed_password(password: str) -> str:
    """
    Create hashed password to be stored in the service.

    Parameters
    ----------
    password : str
        Plain password.

    Returns
    -------
    str
        Hashed password.

    Raises
    ------
    fastapi.HTTPException
        If hashed password could not be created.

    """
    hashed_password = bcrypt.hash(secret=password)
    if isinstance(hashed_password, str):
        return hashed_password
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Error while generating hashed password",
    )


def check_password(password: str, hashed_password: str) -> bool:
    """
    Check if password is correct.

    Parameters
    ----------
    password : str
        Plain password.
    hashed_password : str
        Hashed password.

    Returns
    -------
    bool
        True if password is correct, False otherwise.

    Raises
    ------
    fastapi.HTTPException
        If password and hashed could not be checked.

    """
    is_valid = bcrypt.verify(secret=password, hash=hashed_password)
    if isinstance(is_valid, bool):
        return is_valid
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Error while checking hashed password",
    )


def create_authentication_token(username: str) -> Token:
    """
    Create authentication token to user.

    Parameters
    ----------
    username : str
        User's username (email).

    Returns
    -------
    Token
        Authentication token.

    """
    jwt_token = JWTToken(
        sub=username,
        iat=datetime.timestamp(datetime.utcnow()),
        exp=datetime.timestamp(
            datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_TIME)
        ),
    )
    return Token(
        access_code=jwt.encode(
            jwt_token.dict(), TOKEN_SECRET_KEY, algorithm=TOKEN_ALGORITHM
        )
    )


def check_authentication(
    token: str = Depends(
        OAuth2PasswordBearer(tokenUrl=f"{USER_URL}{TOKEN_URL}")
    ),
) -> None:
    """
    Check if user has valid authentication token.

    Parameters
    ----------
    token : str
        Token in authorization header, by default
        Depends( OAuth2PasswordBearer(tokenUrl=f"{USER_URL}{TOKEN_URL}") )

    Raises
    ------
    fastapi.HTTPException
        If token is invalid.
    fastapi.HTTPException
        If token is expired.

    """
    try:
        jwt.decode(token, TOKEN_SECRET_KEY, algorithms=[TOKEN_ALGORITHM])
        # TODO check if user is in database
    except jwt.DecodeError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is invalid",
        ) from error
    except jwt.ExpiredSignatureError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is expired",
        ) from error
