"""Customer pydantic schemas."""
# pylint: disable=too-few-public-methods

from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    EmailStr,
    constr,
)

from source.database.models import CHARACTER_LIMIT
from source.schemas import create_form


@create_form
class CustomerForm(BaseModel):
    """Customer form schema."""

    name: constr(min_length=1, max_length=CHARACTER_LIMIT)  # type: ignore
    email: EmailStr
