from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator,EmailStr

class EventBase(BaseModel):
    title: str = Field(... ,min_length=1, max_length=200, examples =["Pyhton Workshop"])
    description: str | None = Field(None, examples =["Beginners friendly session"])
    event_date: datetime = Field(..., examples=["2026-11-20T10:00:00"])
    location: str = Field(...,min_length=1 , max_length=255 ,examples=["New York"])
    max_capacity: int = Field(...,gt=0, examples=[50])

    #Abhi " " spcese ka title min_length=1 pass kar dega. Usay rokne ke liye
    @field_validator("title","location")
    @classmethod
    def must_not_be_blank(cls, value:str)->str:
        value = value.strip()
        if not value:
            raise ValueError("must not be blank")
        return value

class EventCreate(EventBase):
    """Request body for POST /events."""


class EventUpdate(EventBase):
    """Request body for PUT /events/{id}."""


class EventResponse(EventBase):
    """What the API sends back to the client."""

    id: int
    model_config = ConfigDict(from_attributes=True)    


class RegistrationCreate(BaseModel):
    """Request body for POST /events/{id}/registrations."""
    employee_name: str = Field(..., min_length=1, max_length=150, examples=["waqas Khan"])
    employee_email: EmailStr = Field(..., examples=["waqas.khan@acme.com"])  
    @field_validator("employee_name")
    @classmethod
    def name_must_be_not_blank(cls, value:str)->str:
        """Reject names that contain only spaces."""
        value = value.strip()
        if not value:
            raise ValueError("must not be empty")
        return value 
    @field_validator("employee_email")
    @classmethod
    def lowercase_email(cls, value: str) -> str:
        """Store emails in lowercase so Ali@acme.com and ali@acme.com count as the same person."""
        return value.lower()

class RegistrationResponse(BaseModel):
    """What the API sends back for a registration."""

    id: int
    event_id: int
    employee_name: str
    employee_email: str
    registered_at: datetime
    model_config = ConfigDict(from_attributes=True)    

   