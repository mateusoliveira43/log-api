"""Utils for tests."""

import tempfile
from typing import Generator
from unittest import TestCase

from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.future import Engine
from sqlalchemy.orm import Session, sessionmaker

from source.__main__ import log_api
from source.database.models import LogApiBase
from source.dependencies.authentication import check_authentication
from source.dependencies.database import get_database_session


class ClientForTest(TestCase):
    """create client to test the api routes using unittest.TestCase."""

    engine: Engine
    session: Session
    api: FastAPI
    test_client: TestClient

    @classmethod
    def setUpClass(cls) -> None:
        """Run before the class tests."""
        cls.engine = create_engine(
            f"sqlite:///{tempfile.mkstemp()[1]}",
            connect_args={"check_same_thread": False},
        )
        cls.session = sessionmaker(
            autocommit=False, autoflush=False, bind=cls.engine
        )()
        LogApiBase.metadata.create_all(cls.engine)

        def override_get_database_session() -> Generator[Session, None, None]:
            try:
                yield cls.session
            finally:
                cls.session.close()

        log_api.dependency_overrides[
            get_database_session
        ] = override_get_database_session

        def override_check_authentication() -> None:
            """Override authentication for tests."""

        log_api.dependency_overrides[
            check_authentication
        ] = override_check_authentication

        cls.api = log_api
        cls.test_client = TestClient(cls.api)

    @classmethod
    def tearDownClass(cls) -> None:
        """Run after the class tests."""
        LogApiBase.metadata.drop_all(cls.engine)
