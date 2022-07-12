"""Message pydantic schemas."""
# pylint: disable=too-few-public-methods

from pydantic import BaseModel  # pylint: disable=no-name-in-module


class Message(BaseModel):
    """Message schema."""

    detail: str
