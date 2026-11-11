from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models import Student, User
from app.schemas import StudentCreate, StudentOut, StudentUpdate, Token, UserCreate, UserOut
from app.security import create_access_token, hash_password, verify_password

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])
students_router = APIRouter(prefix="/students", tags=["Students"])

DbSession = Annotated[Session, Depends(get_db)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@auth_router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: DbSession):
    existing = db.scalar(select(User).where(User.email == payload.email))
    if existing:
        raise HTTPException(status_code=409, detail="An account with this email already exists")
    user = User(email=payload.email, hashed_password=hash_password(payload.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@auth_router.post("/login", response_model=Token)
def login(form: Annotated[OAuth2PasswordRequestForm, Depends()], db: DbSession):
    user = db.scalar(select(User).where(User.email == form.username))
    if user is None or not verify_password(form.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return Token(access_token=create_access_token(str(user.id)))


@students_router.post("", response_model=StudentOut, status_code=status.HTTP_201_CREATED)
def create_student(payload: StudentCreate, db: DbSession, user: CurrentUser):
    student = Student(**payload.model_dump(), owner_id=user.id)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


@students_router.get("", response_model=list[StudentOut])
def list_students(db: DbSession, user: CurrentUser):
    return db.scalars(select(Student).where(Student.owner_id == user.id).order_by(Student.id)).all()


@students_router.get("/{student_id}", response_model=StudentOut)
def get_student(student_id: int, db: DbSession, user: CurrentUser):
    student = db.scalar(select(Student).where(Student.id == student_id, Student.owner_id == user.id))
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@students_router.put("/{student_id}", response_model=StudentOut)
def update_student(student_id: int, payload: StudentUpdate, db: DbSession, user: CurrentUser):
    student = db.scalar(select(Student).where(Student.id == student_id, Student.owner_id == user.id))
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    for field, value in payload.model_dump().items():
        setattr(student, field, value)
    db.commit()
    db.refresh(student)
    return student


@students_router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: DbSession, user: CurrentUser):
    student = db.scalar(select(Student).where(Student.id == student_id, Student.owner_id == user.id))
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return None
