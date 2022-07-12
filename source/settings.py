"""Service settings."""

from decouple import config

DAY_IN_MINUTES = 24 * 60
USER_URL = "/user"
TOKEN_URL = "/token"
TOKEN_SECRET_KEY = config("TOKEN_SECRET_KEY")
TOKEN_ALGORITHM = "HS256"
TOKEN_EXPIRATION_TIME = DAY_IN_MINUTES


def get_database_settings() -> str:
    """
    Get database settings to instantiate a SQLAlchemy engine.

    Database settings in the format ::

        dialect+driver://username:password@host:port/database_name

    where:

    - dialect: SQLAlchemy dialect, in lowercase
    - driver: Python Database API Specification (DBAPI), in lowercase
    - username: username of the database
    - password: password of the username
    - host: host of the database
    - port: port of the database
    - database_name: name of the database

    Returns
    -------
    str
        Database settings.

    """
    dialect = "postgresql"
    driver = "psycopg2"
    username = config("USER_NAME")
    password = config("USER_NAME")
    host = config("DATABASE_HOST")
    port = config("DATABASE_PORT", cast=int)
    database_name = config("DATABASE_HOST")

    return (
        f"{dialect}+{driver}://"
        f"{username}:{password}@{host}:{port}/{database_name}"
    )
