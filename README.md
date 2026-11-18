# Corporate Event Management API

A REST API for Acme Corp's internal event system, built with **FastAPI**, **PostgreSQL** and **SQLAlchemy 2.0 (async)**. Employees' events can be created and managed, and attendees can register for them.

## Features

- Event CRUD (create, list, get, update, delete)
- Event registration, listing and cancellation
- Business rules: no duplicate registrations, capacity limit, no registration for non-existent events
- Pydantic validation and proper HTTP status codes (200, 201, 204, 404, 409, 422)
- Fully asynchronous database access
- Auto-generated API docs (Swagger UI)

## Tech Stack

Python 3.11+, FastAPI, SQLAlchemy 2.0 (async), asyncpg, PostgreSQL, Pydantic

## Project Structure

| File          | Purpose                                       |
| ------------- | --------------------------------------------- |
| `db.py`       | Database connection and configuration         |
| `models.py`   | SQLAlchemy database models                    |
| `schemas.py`  | Pydantic schemas for validation and responses |
| `services.py` | Business logic and database operations        |
| `main.py`     | API endpoints and application entry point     |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Muhammad-waqas-moin/event-management-api.git
cd event-management-api
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Database Configuration

1. Install and start PostgreSQL.
2. Create an empty database:

```sql
CREATE DATABASE event_db;
```

3. Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

4. Edit `.env` and set your own PostgreSQL username and password:

```
DATABASE_URL=postgresql+asyncpg://USERNAME:PASSWORD@localhost:5432/event_db
```

Tables are created automatically when the application starts.

## Running the Application

```bash
uvicorn main:app --reload
```

Open the interactive API documentation at: http://127.0.0.1:8000/docs

## API Endpoints

### Events

| Method | Endpoint       | Description               |
| ------ | -------------- | ------------------------- |
| POST   | `/events`      | Create a new event        |
| GET    | `/events`      | Retrieve all events       |
| GET    | `/events/{id}` | Retrieve a specific event |
| PUT    | `/events/{id}` | Update an event           |
| DELETE | `/events/{id}` | Delete an event           |

### Registrations

| Method | Endpoint                     | Description                         |
| ------ | ---------------------------- | ----------------------------------- |
| POST   | `/events/{id}/registrations` | Register for an event               |
| GET    | `/events/{id}/registrations` | View all registrations for an event |
| DELETE | `/registrations/{id}`        | Cancel a registration               |

## Status Codes

| Code | Meaning                                 |
| ---- | --------------------------------------- |
| 200  | Successful retrieval or update          |
| 201  | Resource created                        |
| 204  | Successful deletion                     |
| 404  | Event or registration not found         |
| 409  | Duplicate registration or event is full |
| 422  | Invalid request data                    |

## Author

Muhammad Waqas Moin
