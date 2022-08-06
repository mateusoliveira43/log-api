"""Service database session."""

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session, sessionmaker

from source.settings import get_database_settings

DATABASE_ENGINE = create_engine(get_database_settings())


def get_database_session() -> Session:
    """
    Get service database session.

    Returns
    -------
    sqlalchemy.orm.session.Session
        Service database session.

    """
    return sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=DATABASE_ENGINE,
    )()
