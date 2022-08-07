"""Event pydantic schemas."""
# pylint: disable=too-few-public-methods

from datetime import datetime

from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    EmailStr,
    constr,
)

from source.database.models import CHARACTER_LIMIT
from source.schemas import BaseFormModel


# @create_form
class EventForm(BaseFormModel):
    """Event form schema."""

    email: EmailStr
    type_: constr(min_length=1, max_length=CHARACTER_LIMIT)  # type: ignore


class EventModel(BaseModel):
    """Event schema."""

    customer: EmailStr
    type_: constr(min_length=1, max_length=CHARACTER_LIMIT)  # type: ignore
    registered_at: datetime
