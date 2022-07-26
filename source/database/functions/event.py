"""Event manipulation functions."""

from typing import List, Optional

from sqlalchemy.orm import Session

from source.database.models import Customer, Event
from source.schemas.event import EventModel


def add_creation_event(
    name: str,
    email: str,
    database_session: Session,
) -> None:
    """
    Add a customer registration event to the service.

    Parameters
    ----------
    name : str
        Name of the customer.
    email : str
        Email of the customer
    database_session : sqlalchemy.orm.session.Session
        Service database session.

    """
    created_customer = Customer(
        name=name,
        email=email,
    )
    creation_event = Event(
        type_="Customer Registration", customer=created_customer
    )
    database_session.add_all([created_customer, creation_event])
    database_session.commit()


def add_status_event(
    customer: Customer,
    status: bool,
    database_session: Session,
) -> None:
    """
    Add a status event to the service.

    Parameters
    ----------
    customer : Customer
        Customer associated with the event.
    status : bool
        Customer status: True if is active, False otherwise.
    database_session : sqlalchemy.orm.session.Session
        Service database session.

    """
    customer.is_active = status
    type_ = "Customer Activation" if status else "Customer Deactivation"
    status_event = Event(type_=type_, customer=customer)
    database_session.add_all([customer, status_event])
    database_session.commit()


def add_custom_event(
    customer: Customer,
    type_: str,
    database_session: Session,
) -> None:
    """
    Add a custom event to the service.

    Parameters
    ----------
    customer : Customer
        Customer associated with the event.
    type_ : str
        Type of the event.
    database_session : sqlalchemy.orm.session.Session
        Service database session.

    """
    database_session.add(Event(type_=type_, customer=customer))
    database_session.commit()


def get_event_list(
    database_session: Session,
) -> List[Optional[EventModel]]:
    """
    Get the event list of the service.

    Parameters
    ----------
    database_session : sqlalchemy.orm.session.Session
        Service database session.

    Returns
    -------
    List[Optional[EventModel]]
        List of all events stored in the service.

    """
    return [
        EventModel(
            customer=event.customer.email,
            type_=event.type_,
            registered_at=event.registered_at,
        )
        for event in database_session.query(Event).all()
    ]
