from typing import Generic, List, TypeVar
from pydantic import BaseModel, Field

T = TypeVar('T')


class PageResponse(BaseModel, Generic[T]):
    total: int
    data: List[T]


# Shared properties
class UserBase(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    # email: EmailStr = Field(unique=True, index=True, max_length=255)
    # is_active: bool = True
    # is_superuser: bool = False
    # full_name: str | None = Field(default=None, max_length=255)


# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: int
    name: str


# class UsersPublic(BaseModel):
#     data: list[UserPublic]
#     count: int
