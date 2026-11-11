from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import models  # noqa: F401 - registers SQLAlchemy models with Base.metadata
from app.database import Base, engine
from app.routers import auth_router, students_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    # For this learning project; use Alembic migrations for production deployments.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Student Management API",
    description="A learning API with PostgreSQL/SQLite persistence, JWT authentication, and owner-scoped student CRUD.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "service": "Student Management API"}


app.include_router(auth_router)
app.include_router(students_router)
