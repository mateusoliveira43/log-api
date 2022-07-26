"""Object-Relational mapping (ORM) models."""
# pylint: disable=too-few-public-methods

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

CHARACTER_LIMIT = 255

LogApiBase = declarative_base()


class User(LogApiBase):  # type: ignore
    """ORM model for user table."""

    __tablename__ = "USER"
    id_ = Column("USER_ID", Integer, primary_key=True)
    email = Column("USER_EMAIL", String(CHARACTER_LIMIT), unique=True)
    hashed_password = Column("USER_HASHED_PASSWORD", String)


class Customer(LogApiBase):  # type: ignore
    """ORM model for customer table."""

    __tablename__ = "CUSTOMER"
    id_ = Column("CUSTOMER_ID", Integer, primary_key=True)
    name = Column("CUSTOMER_NAME", String(CHARACTER_LIMIT))
    email = Column("CUSTOMER_EMAIL", String(CHARACTER_LIMIT), unique=True)
    is_active = Column("CUSTOMER_IS_ACTIVE", Boolean, default=True)

    events = relationship("Event", backref="customer")


class Event(LogApiBase):  # type: ignore
    """ORM model for event table."""

    __tablename__ = "EVENT"
    id_ = Column("EVENT_ID", Integer, primary_key=True)
    customer_id = Column(
        "CUSTOMER_ID", Integer, ForeignKey("CUSTOMER.CUSTOMER_ID")
    )
    type_ = Column("EVENT_TYPE", String(255))
    registered_at = Column("EVENT_REGISTERED_AT", DateTime, default=func.now())
