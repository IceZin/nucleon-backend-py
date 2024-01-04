from sqlalchemy import ForeignKey, Sequence, func
from sqlalchemy.orm import (
    Mapped,
    DeclarativeBase,
    mapped_column,
)

from uuid import UUID
from datetime import datetime

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(server_default=func.next_value(Sequence('users_table_id_seq')))
    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str]
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    verified: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now())


class Session(Base):
    __tablename__ = "sessions"
    id: Mapped[int] = mapped_column(server_default=func.next_value(Sequence('sessions_table_id_seq')))
    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    user_uuid: Mapped[UUID] = mapped_column(ForeignKey(User.uuid))
    active: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now())
    expires_at: Mapped[datetime]
