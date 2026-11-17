# """Database connection and configuration."""
# import os # Python ka built-in tool, computer ki settings (environment variables) parhne ke liye

# from dotenv import load_dotenv # .env file ko parhne wala function
# from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine#“sessions” banane wali factory, create_async_engine # database se asli connection banata hai
# from sqlalchemy.orm import DeclarativeBase #tables banane ke liye parent class


# """
# load_dotenv(): .env file kholkar uski lines Python ko de deta hai
# os.getenv("DATABASE_URL"): us naam ki value nikalta hai
# if not DATABASE_URL:: agar value mili hi nahi, to saaf error do. Beginners ke liye yeh bohat madadgar hai, warna baad mein ajeeb error aate"""

# # load environment variables from .env file
# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
# if not DATABASE_URL:
#     raise RuntimeError("DATABASE_URL is not set")


# # Engine = the real connection to PostgreSQL
# engine = create_async_engine(DATABASE_URL, echo=False)

# # Session factory = creates a "conversation" with the database
# AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)    

# class Base(DeclarativeBase):
#     async def get_db():
#         async with AsyncSessionLocal() as session:
#              yield session
            
"""Database connection and configuration."""
import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

#load enviromennt varaviables from .env file
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

# Engine = the real connection to PostgreSQL
engine =  create_async_engine(DATABASE_URL, echo=False)

# Session factory = creates a "conversation" with the database
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    """Parent class: every database model inherits from this."""


async def get_db():
    """Give each request its own database session, then close it."""
    async with AsyncSessionLocal() as session:
        yield session