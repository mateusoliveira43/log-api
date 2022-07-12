"""Event pydantic schemas."""
# pylint: disable=too-few-public-methods

from __future__ import annotations

from datetime import datetime

from fastapi import Form
from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    EmailStr,
    constr,
)

from source.database.models import CHARACTER_LIMIT


class EventForm(BaseModel):
    """Event form schema."""

    email: EmailStr
    type_: constr(min_length=1, max_length=CHARACTER_LIMIT)

    @classmethod
    def form(
        cls,
        email: EmailStr = Form(...),
        type_: constr(min_length=1, max_length=CHARACTER_LIMIT) = Form(...),
    ) -> EventForm:
        """
        Generate form for endpoints.

        Parameters
        ----------
        email : EmailStr, optional
            Customer associated to event email, by default Form(...)
        type_ : constr, optional
            Type of the event, by default Form(...)

        Returns
        -------
        EventForm
            Form for endpoint.

        """
        return cls(email=email, type_=type_)


class EventModel(BaseModel):
    """Event schema."""

    customer: EmailStr
    type_: constr(min_length=1, max_length=CHARACTER_LIMIT)
    registered_at: datetime
