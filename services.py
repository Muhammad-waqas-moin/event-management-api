from sqlalchemy import select, func  # database se data mangwane k tool (sql k salect)
from models import Event,  Registration # hamari table wali class
from sqlalchemy.ext.asyncio import AsyncSession 
from schemas import EventUpdate , EventCreate, RegistrationCreate, RegistrationResponse # hamari schema wali class
from sqlalchemy.exc import IntegrityError

async def create_event(db: AsyncSession, data: EventCreate) -> Event:
    """Create and save a new event."""
    event = Event(**data.model_dump()) #schema ko dictionary bana deta hai
    db.add(event)
    await db.commit()# database mein save karta hai
    await db.refresh(event) #database se dobara load karo, taake naya id (jo database ne banaya) mil jaye
    return event


async def get_events(db: AsyncSession) -> list[Event]:
    """Return all events ordered by date."""
    result = await db.execute(select(Event).order_by(Event.event_date))
    return list(result.scalars().all())

# select(Event): “Event table se sab rows do”
# .order_by(Event.event_date): date ke hisaab se tarteeb
# db.execute(...): query database ko bhejo
# result.scalars().all(): jawab ko Event objects ki list mein badal do

async def get_event(db: AsyncSession, event_id: int) -> Event | None:
    """Return one event, or None if it does not exist."""
    return await db.get(Event, event_id)

# db.get(Event, event_id): primary key (id) se seedha ek row dhoondo
# Agar nahi mili to None wapas aata hai. Isi None se main.py 404 banayega


async def update_event(db: AsyncSession, event_id: int, data: EventUpdate) -> Event | None:
    """Update an event. Returns None if the event does not exist."""
    event = await db.get(Event, event_id)
    if event is None:
        return None
    for field, value in data.model_dump().items():
        setattr(event, field, value)
    await db.commit()
    await db.refresh(event)
    return event

async def delete_event(db: AsyncSession, event_id: int) -> bool:
    """Delete an event. Returns False if the event does not exist."""
    event = await db.get(Event, event_id)
    if event is None:
        return False
    await db.delete(event)
    await db.commit()
    return True

class EventNotFoundError(Exception):
    """Raised when the requested event does not exist."""


class DuplicateRegistrationError(Exception):
    """Raised when an employee is already registered for the event."""


class EventFullError(Exception):
    """Raised when the event has reached its maximum capacity."""

async def register_event(db:AsyncSession, event_id: int, data: RegistrationCreate)->Registration:
    """Register an employee for an event, enforcing all business rules.""" 
    # Rule : the event must exist
    event = await db.get(Event, event_id)
    if event is None:
        raise EventNotFoundError  
      
    # Rule : no duplicate registration for the same event
    existing= await  db.execute(select(Registration).where(
            Registration.event_id == event_id,
            Registration.employee_email == data.employee_email,
        ))
    if existing.scalar_one_or_none() is not None:
        raise DuplicateRegistrationError

    #rule: the event must not be full
    count = await db.scalar(
        select(func.count()).select_from(Registration).where(Registration.event_id == event_id)
    )
    if count >= event.max_capacity:
        raise EventFullError

    
    registration = Registration(event_id=event_id, **data.model_dump())
    db.add(registration)
    try:
        await db.commit()
    except IntegrityError:
        # Two identical requests at the same moment: the database unique constraint catches it
        await db.rollback()
        raise DuplicateRegistrationError
    await db.refresh(registration)
    return registration 


async def get_registrations(db: AsyncSession, event_id: int) -> list[Registration]:
    """Return all registrations of an event. Raises EventNotFoundError if it does not exist."""
    event = await db.get(Event, event_id)
    if event is None:
        raise EventNotFoundError
    result = await db.execute(
        select(Registration)
        .where(Registration.event_id == event_id)
        .order_by(Registration.registered_at)
    )
    return list(result.scalars().all())

async def cancel_registration(db: AsyncSession, registration_id: int) -> bool:
    """Cancel a registration. Returns False if it does not exist."""
    registration = await db.get(Registration, registration_id)
    if registration is None:
        return False
    await db.delete(registration)
    await db.commit()
    return True