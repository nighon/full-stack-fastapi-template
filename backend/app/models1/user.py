from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import BigInteger, Column, ForeignKey, String, Boolean
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


# Database Models
class User(Base):
    __tablename__ = "user"

    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    full_name = Column(String(255), nullable=True)

    items = relationship("Item", back_populates="owner", cascade="all, delete")


class Item(Base):
    __tablename__ = "item"

    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    owner_id = Column(INTEGER(unsigned=True), ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User", back_populates="items")


# Pydantic Schemas
class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = None


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=40)
    full_name: str | None = None


class UserUpdate(UserBase):
    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=8, max_length=40)


class UserUpdateMe(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None


class UpdatePassword(BaseModel):
    current_password: str = Field(min_length=8, max_length=40)
    new_password: str = Field(min_length=8, max_length=40)


class UserPublic(UserBase):
    id: int


class UsersPublic(BaseModel):
    data: list[UserPublic]
    count: int


class ItemBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    title: str | None = Field(default=None, min_length=1, max_length=255)


class ItemPublic(ItemBase):
    id: int
    owner_id: int


class ItemsPublic(BaseModel):
    data: list[ItemPublic]
    count: int


class Message(BaseModel):
    message: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str | None = None


class NewPassword(BaseModel):
    token: str
    new_password: str = Field(min_length=8, max_length=40)
