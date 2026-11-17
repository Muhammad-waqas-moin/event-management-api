"""SQLAlchemy database models (tables)."""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column
from db import Base
# datetime: Python ka date+time type (event ki date ke liye)
# DateTime, Integer, String, Text: column ke types. Integer = poora number, String = chhota text (limit ke saath), Text = lamba text
# Mapped, mapped_column: SQLAlchemy ke tools jo column define karte hain
# from db import Base: wahi Base jo humne db.py mein banaya tha. Isi se table “registered” hoti hai


class Event(Base):
    __tablename__ ="events"
    #class Event(Base): Event class, jo Base se judi hai, yani yeh ek table hai
    # __tablename__ = "events": PostgreSQL mein table ka asli naam events hoga
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    event_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    max_capacity: Mapped[int] = mapped_column(Integer, nullable=False)