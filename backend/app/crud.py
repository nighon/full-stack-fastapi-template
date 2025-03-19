import uuid
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession
# from sqlmodel import Session, select

# from app.core.security import get_password_hash, verify_password
from app.models import User
from app.schema.request import UserCreate
# from app.schemas import UserCreate
# from app.models import Item, ItemCreate, User, UserCreate, UserUpdate


async def create_user(*, session: AsyncSession, user_create: UserCreate) -> User:
    # db_obj = User.model_validate(
    #     user_create, update={"hashed_password": get_password_hash(user_create.password)}
    # )
    # db_obj = User.model_validate(user_create)
    db_obj = User(**user_create.model_dump())
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj


# def update_user(*, session: AsyncSession, db_user: User, user_in: UserUpdate) -> Any:
#     user_data = user_in.model_dump(exclude_unset=True)
#     extra_data = {}
#     if "password" in user_data:
#         password = user_data["password"]
#         hashed_password = get_password_hash(password)
#         extra_data["hashed_password"] = hashed_password
#     db_user.sqlmodel_update(user_data, update=extra_data)
#     session.add(db_user)
#     session.commit()
#     session.refresh(db_user)
#     return db_user


# async def get_user_by_email(*, session: AsyncSession, email: str) -> User | None:
#     statement = select(User).where(User.email == email)
#     session_user = (await session.execute(statement)).first()
#     return session_user


# def authenticate(*, session: Session, email: str, password: str) -> User | None:
#     db_user = get_user_by_email(session=session, email=email)
#     if not db_user:
#         return None
#     if not verify_password(password, db_user.hashed_password):
#         return None
#     return db_user


# def create_item(*, session: Session, item_in: ItemCreate, owner_id: uuid.UUID) -> Item:
#     db_item = Item.model_validate(item_in, update={"owner_id": owner_id})
#     session.add(db_item)
#     session.commit()
#     session.refresh(db_item)
#     return db_item
