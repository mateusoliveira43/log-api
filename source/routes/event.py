"""Event related endpoints."""

from typing import List, Optional

from fastapi import APIRouter, Depends, status

from source.database.functions.customer import get_customer_available
from source.database.functions.event import add_custom_event, get_event_list
from source.dependencies.authentication import check_authentication
from source.schemas.event import EventForm, EventModel
from source.schemas.message import Message

router = APIRouter(
    prefix="/event",
    tags=["Event"],
    dependencies=[Depends(check_authentication)],
)


@router.post(
    "/create",
    name="event-create",
    status_code=status.HTTP_201_CREATED,
    response_model=Message,
)
async def create_event(
    event: EventForm = Depends(EventForm.form),  # type: ignore
) -> Message:
    """
    Create a event endpoint.

    Parameters
    ----------
    event : EventForm
        Customer email and event type, by default Depends(EventForm.form)

    Returns
    -------
    Message
        Success message.

    """
    customer = get_customer_available(
        email=event.email,
        is_active=True,
        message=f"Customer with email {event.email} is not active.",
    )
    add_custom_event(customer=customer, type_=event.type_)
    return Message(detail="Event Registered successfully.")


@router.get(
    "/",
    name="event-list",
    status_code=status.HTTP_200_OK,
    response_model=List[Optional[EventModel]],
)
async def list_event() -> List[Optional[EventModel]]:
    """
    List the events stored in the service endpoint.

    Returns
    -------
    List[Optional[EventModel]]
        The events stored in the service.

    """
    return get_event_list()
