"""User pydantic schemas."""
# pylint: disable=too-few-public-methods

from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    EmailStr,
    constr,
)

from source.database.models import CHARACTER_LIMIT
from source.schemas import BaseFormModel


class UserForm(BaseFormModel):
    """User form schema."""

    email: EmailStr
    password: constr(min_length=6, max_length=CHARACTER_LIMIT)  # type: ignore


class JWTToken(BaseModel):
    """
    JWT token schema.

    With:
    - Issued at (iat) time
    - Expiration (exp) time
    - Subject (sub)

    """

    iat: float
    exp: float
    sub: EmailStr


class Token(BaseModel):
    """Token schema."""

    access_code: str
    type_: str = "bearer"
