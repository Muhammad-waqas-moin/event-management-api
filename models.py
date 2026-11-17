"""SQLAlchemy database models (tables)."""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey,UniqueConstraint ,func
from sqlalchemy.orm import Mapped, mapped_column
from db import Base
# uniqueConstraint: table mein duplication rukhne k liye # foreign key: 2 tables ko connect karte hain
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

class Registration(Base):
     """Represents one employee's registration for one event."""
     __tablename__ = "registrations" 
      # One employee can register only once per event (enforced by the database too)
     __table_args__ = (UniqueConstraint("event_id", "employee_email", name="uq_event_employee"),)  
     
     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
     event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id", ondelete="CASCADE"), nullable=False, index=True
     )
     employee_name: Mapped[str] = mapped_column(String(150), nullable=False)
     employee_email: Mapped[str] = mapped_column(String(255), nullable=False)
     registered_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now()) 