# Aniendcards — Backend

FastAPI + SQLAlchemy backend for the Aniendcards database.

## Stack

- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** PostgreSQL
- **Package manager:** uv

## Local Development

**Prerequisites:** Python 3.13+, uv

```bash
uv run fastapi dev src/main.py
```

The API will be available at http://localhost:8000 and the interactive docs at http://localhost:8000/docs.

## TODO

- ~~Authentication~~
  - ~~User and roles models~~
  - ~~Token authentication~~
  - ~~Add dependencies for create and delete endpoints~~
  - ~~Move user creation to another service~~
- ~~Server Error handling~~
- Image object storage
  - File upload endpoint
  - File resizing and compression
  - Image object storage saving and retrieval
- Deployment
- Fix delete rules in the orm
  
