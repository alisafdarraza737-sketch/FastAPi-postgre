# FastAPI + PostgreSQL Student Management API

A learning backend built with **FastAPI, SQLAlchemy 2, Pydantic, PostgreSQL, and JWT authentication**. It provides account registration/login and authenticated, user-scoped student CRUD endpoints.

## Features implemented

- FastAPI application with Swagger and ReDoc documentation
- SQLAlchemy 2 ORM models for users and students
- PostgreSQL support, with SQLite as the default local development database
- Pydantic validation for email, age, and field lengths
- Password hashing using Argon2 through pwdlib
- JWT bearer-token authentication
- Authenticated student create, list, read, update, and delete endpoints
- Each account can access only its own student records
- Basic health endpoint and pytest test

## Project structure

```text
FastAPi-postgre/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── dependencies.py
│   ├── models.py
│   ├── routers.py
│   ├── schemas.py
│   └── security.py
├── tests/
│   └── test_health.py
├── .env.example
├── .gitignore
├── main.py
└── requirements.txt
```

## Requirements

- Python 3.10+
- PostgreSQL for a persistent shared database (SQLite is used by default locally)

## Installation

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

### 3. Install packages

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env`. For local development, the default SQLite URL works without additional setup.

For PostgreSQL, set:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/YOUR_DATABASE
SECRET_KEY=YOUR_LONG_RANDOM_SECRET
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Use a long, randomly generated secret key and never commit `.env` or real credentials.

### 5. Start the API

```bash
uvicorn main:app --reload
```

The local server runs at `http://127.0.0.1:8000`.

## API endpoints

| Method | Endpoint | Authentication | Purpose |
|---|---|---|---|
| GET | `/` | No | Health check |
| POST | `/auth/register` | No | Create an account |
| POST | `/auth/login` | No | Obtain a JWT access token |
| POST | `/students` | Bearer token | Create a student |
| GET | `/students` | Bearer token | List your students |
| GET | `/students/{student_id}` | Bearer token | Read one of your students |
| PUT | `/students/{student_id}` | Bearer token | Update one of your students |
| DELETE | `/students/{student_id}` | Bearer token | Delete one of your students |

### Authentication flow

1. Register with `POST /auth/register`.
2. Log in through `POST /auth/login` using form fields `username` (your email) and `password`.
3. Copy the returned `access_token`.
4. In Swagger UI, click **Authorize** and enter the bearer token, or send it as `Authorization: Bearer YOUR_TOKEN`.

### Example student payload

```json
{
  "name": "Ayesha Khan",
  "email": "ayesha@example.com",
  "age": 21,
  "course": "Information Technology"
}
```

## API documentation

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Run tests

```bash
pytest
```

## Important production notes

This is a learning project, not a production-hardened service. Before production use:

- Replace `Base.metadata.create_all` with Alembic migrations.
- Set a strong secret in a managed environment variable.
- Configure HTTPS, CORS, rate limiting, logging, and monitoring.
- Add integration tests using an isolated test database.
- Review token revocation/refresh strategy and account lifecycle controls.
- Use managed PostgreSQL backups and least-privilege database credentials.

## Author

**Ali Safdar Raza**

- GitHub: [@alisafdarraza737-sketch](https://github.com/alisafdarraza737-sketch)
- LinkedIn: [Ali Safdar Raza](https://www.linkedin.com/in/alisafdar-raza-07984b390/)
