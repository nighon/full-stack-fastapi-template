from typing import Generic, List, TypeVar
from pydantic import BaseModel, Field
# from sqlmodel import Field, Relationship, SQLModel
# from typing import Generic

# tt = Generic(T)
T = TypeVar('T')

class PageResponse(BaseModel, Generic[T]):
    total: int
    data: List[T]
    # data: list[tt]

# Shared properties
class UserBase(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    # email: EmailStr = Field(unique=True, index=True, max_length=255)
    # is_active: bool = True
    # is_superuser: bool = False
    # full_name: str | None = Field(default=None, max_length=255)


# Properties to receive via API on creation
class UserCreate(BaseModel):
    name: str = Field(...)
    # something_else: str = Field(min_length=2, max_length=4)
    # password: str = Field(min_length=8, max_length=40)


# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: int
    name: str


# class UsersPublic(BaseModel):
#     data: list[UserPublic]
#     count: int
