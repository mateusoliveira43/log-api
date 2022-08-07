"""User related endpoints."""

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from source.database.functions.user import authenticate_user, register_user
from source.dependencies.authentication import create_authentication_token
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
) -> Message:
    """
    Create a user endpoint.

    Parameters
    ----------
    user : UserForm
        User's email and password, by default Depends(UserForm.form)

    Returns
    -------
    Message
        Success message.

    """
    register_user(user=user)
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
) -> Token:
    """
    Create a user token endpoint.

    Parameters
    ----------
    user : OAuth2PasswordRequestForm
        User's username (email) and password, by default Depends()

    Returns
    -------
    Token
        Authentication token.

    """
    authenticate_user(form_data=user)
    authentication_token: Token = create_authentication_token(user.username)
    return authentication_token
