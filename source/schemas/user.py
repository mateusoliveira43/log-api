"""User pydantic schemas."""
# pylint: disable=too-few-public-methods

from __future__ import annotations

from fastapi import Form
from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    EmailStr,
    constr,
)

from source.database.models import CHARACTER_LIMIT


class UserForm(BaseModel):
    """User form schema."""

    email: EmailStr
    password: constr(min_length=6, max_length=CHARACTER_LIMIT)

    @classmethod
    def form(
        cls,
        email: EmailStr = Form(...),
        password: constr(min_length=6, max_length=CHARACTER_LIMIT) = Form(...),
    ) -> UserForm:
        """
        Generate form for endpoints.

        Parameters
        ----------
        email : EmailStr, optional
            User email, by default Form(...)
        password : constr, optional
            User password, by default Form(...)

        Returns
        -------
        UserForm
            Form for endpoints.

        """
        return cls(email=email, password=password)


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
