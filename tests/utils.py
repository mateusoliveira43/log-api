from unittest import TestCase

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from source.__main__ import log_api
from source.database.models import LogApiBase
from source.dependencies.authentication import check_authentication
from source.dependencies.database import get_database_session
from tests import TESTS_FOLDER

DATABASE_FOR_TESTS = TESTS_FOLDER / "test.db"


class ClientForTest(TestCase):
    """create client to test the api routes using unittest.TestCase."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.engine = create_engine(
            f"sqlite:///{DATABASE_FOR_TESTS}",
            connect_args={"check_same_thread": False},
        )
        cls.session: Session = sessionmaker(
            autocommit=False, autoflush=False, bind=cls.engine
        )()
        LogApiBase.metadata.create_all(cls.engine)

        def override_get_database_session() -> Session:
            try:
                yield cls.session
            finally:
                cls.session.close()

        log_api.dependency_overrides[
            get_database_session
        ] = override_get_database_session

        def override_check_authentication() -> None:
            pass

        log_api.dependency_overrides[
            check_authentication
        ] = override_check_authentication

        cls.api = log_api
        cls.test_client = TestClient(cls.api)

    @classmethod
    def tearDownClass(cls) -> None:
        LogApiBase.metadata.drop_all(cls.engine)


class DatabaseForTest(TestCase):
    """Create database session for tests using unittest.TestCase."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.engine = create_engine(
            "sqlite:///:memory:", connect_args={"check_same_thread": False}
        )
        cls.session: Session = sessionmaker(
            autocommit=False, autoflush=False, bind=cls.engine
        )()
        LogApiBase.metadata.create_all(cls.engine)

    @classmethod
    def tearDownClass(cls) -> None:
        LogApiBase.metadata.drop_all(cls.engine)
