# AI Usage Documentation

## Tools and Models

- **Tool:** Claude (Anthropic), via the claude.ai chat interface
- **Model:** [sonnet 5.5 medium]
- **Other tools:** None

## Configuration

- Web chat with default settings, no custom system prompt
- Conversation language: Roman Urdu mixed with English
- The AI was used as a step-by-step teacher: it explained each concept, then each file in small parts, and I typed and ran the code myself

## How AI Was Used

I am a beginner in FastAPI, PostgreSQL and Git, so I used AI to learn and build the project in stages:

1. Understanding the assignment PDF and splitting the work into two days
2. Learning concepts: REST, HTTP methods, status codes, async/await, ORM, dependency injection, Git branching
3. Environment setup: Python venv, PostgreSQL (Postgres.app), Git and GitHub
4. Writing and explaining each file: `db.py`, `models.py`, `schemas.py`, `services.py`, `main.py`
5. Registration feature and its business rules
6. Debugging errors (for example an import error caused by a missing function in `db.py`)
7. Writing the README

## Prompts Used

1. Shared the assignment PDF and asked for a beginner-friendly, step-by-step 50% plan, with no topic skipped and the frontend skipped
2. Asked which Python version to use and how a checker would run a local PostgreSQL project
3. Asked for the plan again in smaller beginner-friendly stages with every line explained
4. Asked which code goes into which file
5. Asked how `AsyncSession` gets the session from `db.py`
6. Asked how to test each endpoint in Swagger
7. Asked whether local PostgreSQL or Neon is better for this assignment
8. Asked for the registrations feature (model, schemas, services, endpoints)
9. Error-fixing prompts (venv typo, `get_db` import error, git status questions)

The full list with exact wording is in `docs/ai-chat-history.md`.

## What I Understood and Did Myself

- I typed the code myself file by file, ran every stage and tested every endpoint in Swagger
- I can explain the flow: `main.py` (routes) -> `schemas.py` (validation) -> `services.py` (logic) -> `models.py` -> PostgreSQL
- I fixed my own mistakes, such as a test-file typo and a missing function in `db.py`
- I understand the three business rules and where each is enforced

## Chat History

See `docs/ai-chat-history.md`.
