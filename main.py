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
from schemas import EventCreate, EventResponse, EventUpdate


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
   