from sqlalchemy import select, exists
from sqlalchemy.orm import (
    Session as PgSession,
)
from sqlalchemy.exc import SQLAlchemyError

from uuid import UUID, uuid4

from . import engine, User, Session


class UserQueries:
    @staticmethod
    def get_by_uuid(uuid: str) -> User:
        with PgSession(engine) as session:
            query = select(User).where(User.uuid == uuid)
            result = session.execute(query).first()
            return result[0]
        
    @staticmethod
    def get_by_username(username: str) -> User:
        with PgSession(engine) as session:
            query = select(User).where(User.username == username)
            result = session.execute(query).first()
            return result[0]
        

class SessionQueries:
    @staticmethod
    def get_by_uuid(uuid: str) -> Session:
        with PgSession(engine) as session:
            query = select(Session).where(Session.uuid == uuid)
            result = session.execute(query).first()

            if result:
                return result[0]
            else:
                return None
            
    @staticmethod
    def check_uuid(uuid: str) -> bool:
        with PgSession(engine) as session:
            return session.query(exists().where(Session.uuid == uuid)).scalar()
            
    @staticmethod
    def insert(session: Session) -> UUID:
        with PgSession(engine) as pg_session:
            uuid = uuid4()

            while SessionQueries.check_uuid(uuid):
                uuid = uuid4()

            session.uuid = uuid
            pg_session.add(session)

            try:
                pg_session.commit()
            except SQLAlchemyError as e:
                print(e)
                return None
            finally:
                return uuid