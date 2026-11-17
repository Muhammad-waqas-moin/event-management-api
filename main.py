# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def home():
#     return {"message": "Hello Event API World"}

from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
import models  
import services
from db import Base, engine,get_db
from schemas import EventCreate, EventResponse, EventUpdate, RegistrationCreate,RegistrationResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Create database tables on startup if they do not exist."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Corporate Event Management API",
    description="Internal event system for Acme Corp.",
    version="1.0.0",
    lifespan=lifespan,
)

@app.post(
    "/events",
    response_model=EventResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Events"],
    summary="Create a new event",
)
async def create_event(data: EventCreate, db: AsyncSession = Depends(get_db)):
    """Create a new event."""
    return await services.create_event(db, data)

@app.get(
    "/events",
    response_model=list[EventResponse],
    tags=["Events"],
    summary="Retrieve all events",
)
async def list_events(db: AsyncSession = Depends(get_db)):
    """Return all events."""
    return await services.get_events(db)


@app.get(
    "/events/{event_id}",
    response_model=EventResponse,
    tags=["Events"],
    summary="Retrieve a specific event",
)
async def read_event(event_id: int, db: AsyncSession = Depends(get_db)):
    """Return one event, or 404 if it does not exist."""
    event = await services.get_event(db, event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@app.put(
    "/events/{event_id}",
    response_model=EventResponse,
    tags=["Events"],
    summary="Update an existing event",
)
async def update_event(event_id: int, data: EventUpdate, db: AsyncSession = Depends(get_db)):
    """Update an event, or return 404 if it does not exist."""
    event = await services.update_event(db, event_id, data)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@app.delete(
    "/events/{event_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Events"],
    summary="Delete an event",
)
async def delete_event(event_id: int, db: AsyncSession = Depends(get_db)):
    """Delete an event, or return 404 if it does not exist."""
    deleted = await services.delete_event(db, event_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Event not found")

@app.post(
    "/events/{event_id}/registrations",
    response_model=RegistrationResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Registrations"],
    summary="Register for an event",
)
async def register_for_event(
    event_id: int, data: RegistrationCreate, db: AsyncSession = Depends(get_db)
):
    """Register an employee. Returns 404 if the event is missing, 409 if duplicate or full."""
    try:
        return await services.register_for_event(db, event_id, data)
    except services.EventNotFoundError:
        raise HTTPException(status_code=404, detail="Event not found")
    except services.DuplicateRegistrationError:
        raise HTTPException(status_code=409, detail="Employee is already registered for this event")
    except services.EventFullError:
        raise HTTPException(status_code=409, detail="Event has reached its maximum capacity")


@app.get(
    "/events/{event_id}/registrations",
    response_model=list[RegistrationResponse],
    tags=["Registrations"],
    summary="View all registrations for an event",
)
async def list_registrations(event_id: int, db: AsyncSession = Depends(get_db)):
    """Return all registrations of an event, or 404 if the event does not exist."""
    try:
        return await services.get_registrations(db, event_id)
    except services.EventNotFoundError:
        raise HTTPException(status_code=404, detail="Event not found")


@app.delete(
    "/registrations/{registration_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Registrations"],
    summary="Cancel a registration",
)
async def cancel_registration(registration_id: int, db: AsyncSession = Depends(get_db)):
    """Cancel a registration, or return 404 if it does not exist."""
    cancelled = await services.cancel_registration(db, registration_id)
    if not cancelled:
        raise HTTPException(status_code=404, detail="Registration not found")