"""Customer related endpoints."""

from fastapi import APIRouter, Depends, Form, status
from pydantic import EmailStr  # pylint: disable=no-name-in-module
from sqlalchemy.orm import Session

from source.database.functions.customer import (
    check_email_availability,
    get_customer_available,
)
from source.database.functions.event import (
    add_creation_event,
    add_status_event,
)
from source.dependencies.authentication import check_authentication
from source.dependencies.database import get_database_session
from source.schemas.customer import CustomerForm
from source.schemas.message import Message

router = APIRouter(
    prefix="/customer",
    tags=["Customer"],
    dependencies=[Depends(check_authentication)],
)


@router.post(
    "/create",
    name="customer-create",
    status_code=status.HTTP_201_CREATED,
    response_model=Message,
)
async def create_customer(
    customer: CustomerForm = Depends(CustomerForm.form),
    database_session: Session = Depends(get_database_session),
) -> Message:
    """
    Create a customer endpoint.

    Parameters
    ----------
    customer : CustomerForm, optional
        User's email and password, by default Depends(CustomerForm.form)
    database_session : Session, optional
        Service database session, by default Depends(get_database_session)

    Returns
    -------
    Message
        Success message.

    """
    check_email_availability(
        email=customer.email, database_session=database_session
    )
    add_creation_event(
        name=customer.name,
        email=customer.email,
        database_session=database_session,
    )
    return Message(detail="Customer registered successfully.")


@router.post(
    "/deactivate",
    name="customer-deactivate",
    status_code=status.HTTP_200_OK,
    response_model=Message,
)
async def deactivate_customer(
    email: EmailStr = Form(...),
    database_session: Session = Depends(get_database_session),
) -> Message:
    """
    Deactivate a customer endpoint.

    Parameters
    ----------
    email : EmailStr, optional
        User's email, by default Form(...)
    database_session : Session, optional
        Service database session, by default Depends(get_database_session)

    Returns
    -------
    Message
        Success message.

    """
    customer = get_customer_available(
        email=email,
        is_active=True,
        message=f"Customer with email {email} is already deactivated.",
        database_session=database_session,
    )
    add_status_event(
        customer=customer, status=False, database_session=database_session
    )
    return Message(detail="Customer deactivated successfully.")


@router.post(
    "/activate",
    name="customer-activate",
    status_code=status.HTTP_200_OK,
    response_model=Message,
)
async def activate_customer(
    email: EmailStr = Form(...),
    database_session: Session = Depends(get_database_session),
) -> Message:
    """
    Activate a customer endpoint.

    Parameters
    ----------
    email : EmailStr, optional
        User's email, by default Form(...)
    database_session : Session, optional
        Service database session, by default Depends(get_database_session)

    Returns
    -------
    Message
        Success message.

    """
    customer = get_customer_available(
        email=email,
        is_active=False,
        message=f"Customer with email {email} is already activated.",
        database_session=database_session,
    )
    add_status_event(
        customer=customer, status=True, database_session=database_session
    )
    return Message(detail="Customer activated successfully.")
