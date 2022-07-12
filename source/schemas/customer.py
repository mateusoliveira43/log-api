"""Customer pydantic schemas."""
# pylint: disable=too-few-public-methods

from __future__ import annotations

from fastapi import Form
from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    EmailStr,
    constr,
)

from source.database.models import CHARACTER_LIMIT


class CustomerForm(BaseModel):
    """Customer form schema."""

    name: constr(min_length=1, max_length=CHARACTER_LIMIT)
    email: EmailStr

    @classmethod
    def form(
        cls,
        name: constr(min_length=1, max_length=CHARACTER_LIMIT) = Form(...),
        email: EmailStr = Form(...),
    ) -> CustomerForm:
        """
        Generate form for endpoints.

        Parameters
        ----------
        name : constr, optional
            Customer name, by default Form(...)
        email : EmailStr, optional
            Customer email, by default Form(...)

        Returns
        -------
        CustomerForm
            Form for endpoint.

        """
        return cls(name=name, email=email)
