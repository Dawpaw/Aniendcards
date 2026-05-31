# Aniendcards

A website to browse anime endcards, navigate through titles and artists, and find everything in one place.

## Stack

- **Frontend:** SvelteKit + Tailwind CSS v4
- **Backend:** FastAPI + SQLAlchemy
- **Database:** PostgreSQL

## Running with Docker

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

Then start everything:

```bash
docker compose up
```

| Service  | URL                         |
|----------|-----------------------------|
| Frontend | http://localhost:5173        |
| Backend  | http://localhost:8000        |
| API Docs | http://localhost:8000/docs   |

## Local Development

**Backend:**
```bash
cd backend
uv run fastapi dev src/main.py
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```