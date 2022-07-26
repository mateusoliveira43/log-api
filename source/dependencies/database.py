"""Service database session."""

from typing import Generator

from sqlalchemy.engine import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker
from uvicorn.config import logger

from source.settings import get_database_settings


def get_database_session() -> Generator[Session, None, None]:
    """
    Get service database session.

    Yields
    ------
    Generator[sqlalchemy.orm.session.Session, None, None]
        Service database session.

    """
    try:
        session: Session = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=create_engine(get_database_settings()),
        )()
        yield session
    except SQLAlchemyError as error:
        logger.error(str(error.orig).strip())  # pylint: disable=no-member
    finally:
        session.close()
