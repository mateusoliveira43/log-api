"""Customer related endpoints."""

from fastapi import APIRouter, Depends, Form, status
from pydantic import EmailStr  # pylint: disable=no-name-in-module

from source.database.functions.customer import (
    check_email_availability,
    get_customer_available,
)
from source.database.functions.event import (
    add_creation_event,
    add_status_event,
)
from source.dependencies.authentication import check_authentication
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
) -> Message:
    """
    Create a customer endpoint.

    Parameters
    ----------
    customer : CustomerForm
        User's email and password, by default Depends(CustomerForm.form)

    Returns
    -------
    Message
        Success message.

    """
    check_email_availability(email=customer.email)
    add_creation_event(
        name=customer.name,
        email=customer.email,
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
) -> Message:
    """
    Deactivate a customer endpoint.

    Parameters
    ----------
    email : pydantic.networks.EmailStr
        User's email, by default Form(...)

    Returns
    -------
    Message
        Success message.

    """
    customer = get_customer_available(
        email=email,
        is_active=True,
        message=f"Customer with email {email} is already deactivated.",
    )
    add_status_event(customer=customer, status=False)
    return Message(detail="Customer deactivated successfully.")


@router.post(
    "/activate",
    name="customer-activate",
    status_code=status.HTTP_200_OK,
    response_model=Message,
)
async def activate_customer(
    email: EmailStr = Form(...),
) -> Message:
    """
    Activate a customer endpoint.

    Parameters
    ----------
    email : pydantic.networks.EmailStr
        User's email, by default Form(...)

    Returns
    -------
    Message
        Success message.

    """
    customer = get_customer_available(
        email=email,
        is_active=False,
        message=f"Customer with email {email} is already activated.",
    )
    add_status_event(customer=customer, status=True)
    return Message(detail="Customer activated successfully.")
