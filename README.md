# URL Shortener

A simple URL shortening API built with **FastAPI** and **SQLite**.

The project takes a long URL, generates a unique short ID, stores the URL mapping in a database, and redirects users to the original URL when the short URL is accessed.

## Features

- Create shortened URLs
- Generate random short IDs
- Store URL mappings in SQLite
- Redirect short URLs to their original URLs
- Return `404 Not Found` when a short URL does not exist
- SQLAlchemy ORM for database operations

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Pydantic
- uv

## Project Structure

```text
url-shortener/
├── main.py
├── database.py
├── schemas.py
├── services.py
├── pyproject.toml
└── README.md
```

### File Responsibilities

- `main.py` — API endpoints and application logic
- `database.py` — Database configuration, SQLAlchemy model and database sessions
- `schemas.py` — Pydantic request schemas
- `services.py` — Short ID generation

## API Endpoints

### Create Short URL

**POST** `/urls`

Request:

```json
{
  "url": "https://www.example.com"
}
```

Response:

```json
"Ab3xQ"
```

### Redirect to Original URL

**GET** `/{short_id}`

Example:

```text
GET /Ab3xQ
```

The API redirects the user to the original URL.

If the short ID does not exist:

```json
{
  "detail": "URL not found"
}
```

## Running the Project

Clone the repository and install the dependencies:

```bash
uv sync
```

Start the development server:

```bash
uv run uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Example Workflow

```text
Long URL
   ↓
POST /urls
   ↓
Generate short ID
   ↓
Store URL + short ID in SQLite
   ↓
Return short ID
   ↓
GET /{short_id}
   ↓
Find original URL
   ↓
Redirect to original URL
```

## Purpose

This project was built as a learning project to practice:

- FastAPI
- REST API fundamentals
- Pydantic
- SQLAlchemy
- SQLite
- Dependency Injection with `Depends`
- Database sessions
- HTTP redirects
- Basic project structure
- Git and GitHub workflow
