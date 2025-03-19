# from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import String

# from sqlmodel import Field, Relationship, SQLModel
# from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


# class UserRegister(SQLModel):
#     email: EmailStr = Field(max_length=255)
#     password: str = Field(min_length=8, max_length=40)
#     full_name: str | None = Field(default=None, max_length=255)


# # Properties to receive via API on update, all are optional
# class UserUpdate(UserBase):
#     email: EmailStr | None = Field(default=None, max_length=255)  # type: ignore
#     password: str | None = Field(default=None, min_length=8, max_length=40)


# class UserUpdateMe(SQLModel):
#     full_name: str | None = Field(default=None, max_length=255)
#     email: EmailStr | None = Field(default=None, max_length=255)


# class UpdatePassword(SQLModel):
#     current_password: str = Field(min_length=8, max_length=40)
#     new_password: str = Field(min_length=8, max_length=40)


# Database model, database table inferred from class name
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    # id: Mapped[int] = Field(default=None, sa_column=Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True))
    # hashed_password: str
    # items: list["Item"] = Relationship(back_populates="owner", cascade_delete=True)

    def __repr__(self) -> str:
        # return super().__repr__()
        return f'{self.__class__.__name__}(id={self.id!r}, name={self.name!r})'


# # Properties to return via API, id is always required
# class UserPublic(UserBase):
#     id: int


# class UsersPublic(SQLModel):
#     data: list[UserPublic]
#     count: int


# # Shared properties
# class ItemBase(SQLModel):
#     title: str = Field(min_length=1, max_length=255)
#     description: str | None = Field(default=None, max_length=255)


# # Properties to receive on item creation
# class ItemCreate(ItemBase):
#     pass


# # Properties to receive on item update
# class ItemUpdate(ItemBase):
#     title: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore


# # Database model, database table inferred from class name
# class Item(ItemBase, table=True):
#     id: int = Field(default=None, sa_column=Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True))
#     title: str = Field(max_length=255)
#     owner_id: int = Field(
#         sa_column=Column(INTEGER(unsigned=True), ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
#     )
#     owner: User | None = Relationship(back_populates="items")


# # Properties to return via API, id is always required
# class ItemPublic(ItemBase):
#     id: int
#     owner_id: int


# class ItemsPublic(SQLModel):
#     data: list[ItemPublic]
#     count: int


# # Generic message
# class Message(SQLModel):
#     message: str


# # JSON payload containing access token
# class Token(SQLModel):
#     access_token: str
#     token_type: str = "bearer"


# # Contents of JWT token
# class TokenPayload(SQLModel):
#     sub: str | None = None


# class NewPassword(SQLModel):
#     token: str
#     new_password: str = Field(min_length=8, max_length=40)
