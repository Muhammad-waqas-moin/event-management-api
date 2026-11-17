from sqlalchemy import select # database se data mangwane k tool (sql k salect)
from models import Event # hamari table wali class
from sqlalchemy.ext.asyncio import AsyncSession 
from schemas import EventUpdate , EventCreate# hamari schema wali class

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