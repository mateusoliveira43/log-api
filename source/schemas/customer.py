"""Customer pydantic schemas."""
# pylint: disable=too-few-public-methods

from pydantic import EmailStr, constr  # pylint: disable=no-name-in-module

from source.database.models import CHARACTER_LIMIT
from source.schemas import BaseFormModel


class CustomerForm(BaseFormModel):
    """Customer form schema."""

    name: constr(min_length=1, max_length=CHARACTER_LIMIT)  # type: ignore
    email: EmailStr
