# FastAPI + PostgreSQL Learning Project

A starter repository for learning how to connect a Python FastAPI application to PostgreSQL through SQLAlchemy.

## Current repository status

This repository is an **early-stage learning prototype**, not yet a production-ready CRUD service.

- `main.py` creates a FastAPI application and a SQLAlchemy engine.
- `studenty.py` contains an unfinished draft of student database operations.
- Database models, schemas, session lifecycle, authentication, migrations, automated tests, and deployment are not yet complete.

The README intentionally describes the current code rather than presenting planned features as already implemented.

## Technology

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn
- psycopg2

## Setup

### 1. Clone

```bash
git clone https://github.com/alisafdarraza737-sketch/FastAPi-postgre.git
cd FastAPi-postgre
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the current starter dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

### 4. Configure PostgreSQL

Create a local PostgreSQL database. The current `main.py` contains a placeholder connection URL:

```python
DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/YOUR_DATABASE"
```

Replace the placeholders locally before running the database connection. Never commit real credentials. The next backend iteration should move this value into an environment variable and load it from a local `.env` file.

### 5. Run the API

```bash
uvicorn main:app --reload
```

API documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Next engineering milestones

1. Create a modular `app/` package with database configuration and dependency injection.
2. Add SQLAlchemy models and Pydantic request/response schemas.
3. Implement validated student CRUD endpoints and consistent 404/409 responses.
4. Add password hashing, JWT authentication, and protected routes.
5. Add Alembic migrations and environment-based configuration.
6. Add pytest coverage using an isolated test database.
7. Add Docker configuration and a deployment guide.

## Author

**Ali Safdar Raza** · [GitHub](https://github.com/alisafdarraza737-sketch) · [LinkedIn](https://www.linkedin.com/in/alisafdar-raza-07984b390/)
