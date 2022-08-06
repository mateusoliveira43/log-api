"""Customer manipulation functions."""

from typing import Optional

from fastapi import HTTPException, status

from source.database.models import Customer
from source.dependencies.database import get_database_session


def check_email_availability(email: str) -> None:
    """
    Check if email is available to store a new customer in the service.

    Parameters
    ----------
    email : str
        Email to be checked.

    Raises
    ------
    fastapi.HTTPException
        If email is already registered in the service.

    """
    with get_database_session() as database_session:
        if database_session.query(Customer).filter_by(email=email).first():
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Email {email} is already registered.",
            )


def get_customer_by_email(email: str) -> Customer:
    """
    Get customer by email.

    Parameters
    ----------
    email : str
        Email of the customer.

    Returns
    -------
    Customer
        Customer associate to the email.

    Raises
    ------
    fastapi.HTTPException
        If there no customer associated to the email in the service.

    """
    with get_database_session() as database_session:
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
    email: str, is_active: bool, message: str
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

    Returns
    -------
    Customer
        Customer associate to the email and availability.

    Raises
    ------
    fastapi.HTTPException
        If the customer is not available.

    """
    customer = get_customer_by_email(email=email)
    if customer.is_active != is_active:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=message,
        )
    return customer
