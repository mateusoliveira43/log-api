"""Customer manipulation functions."""

from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from source.database.models import Customer


# TODO remove database session as a parameter from all objects
# Use a context manager where necessary and mock its engine in the tests
def check_email_availability(email: str, database_session: Session) -> None:
    """
    Check if email is available to store a new customer in the service.

    Parameters
    ----------
    email : str
        Email to be checked.
    database_session : sqlalchemy.orm.session.Session
        Service database session.

    Raises
    ------
    fastapi.HTTPException
        If email is already registered in the service.

    """
    if database_session.query(Customer).filter_by(email=email).first():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Email {email} is already registered.",
        )


def get_customer_by_email(email: str, database_session: Session) -> Customer:
    """
    Get customer by email.

    Parameters
    ----------
    email : str
        Email of the customer.
    database_session : sqlalchemy.orm.session.Session
        Service database session.

    Returns
    -------
    Customer
        Customer associate to the email.

    Raises
    ------
    fastapi.HTTPException
        If there no customer associated to the email in the service.

    """
    customer: Optional[Customer] = (
        database_session.query(Customer).filter_by(email=email).first()
    )
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Customer with email {email} is not registered.",
        )
    return customer


def get_customer_available(
    email: str, is_active: bool, message: str, database_session: Session
) -> Customer:
    """
    Get customer available by status.

    Parameters
    ----------
    email : str
        Email of the customer.
    is_active : bool
        Customer status: True if is active, False otherwise.
    message : str
        Message to pass if the customer is not available.
    database_session : sqlalchemy.orm.session.Session
        Service database session.

    Returns
    -------
    Customer
        Customer associate to the email and availability.

    Raises
    ------
    fastapi.HTTPException
        If the customer is not available.

    """
    customer = get_customer_by_email(
        email=email, database_session=database_session
    )
    if customer.is_active != is_active:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=message,
        )
    return customer
