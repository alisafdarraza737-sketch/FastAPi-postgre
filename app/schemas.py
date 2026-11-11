from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserOut(BaseModel):
    id: int
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class StudentBase(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    email: EmailStr
    age: int = Field(ge=1, le=120)
    course: str = Field(min_length=1, max_length=120)


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    pass


class StudentOut(StudentBase):
    id: int
    owner_id: int
    model_config = ConfigDict(from_attributes=True)
