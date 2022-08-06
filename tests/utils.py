"""Utils for tests."""

import functools
import inspect
import tempfile
from typing import Any, Callable
from unittest import TestCase
from unittest.mock import patch

from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.future import Engine
from sqlalchemy.orm import Session, sessionmaker

from source.__main__ import log_api
from source.database.models import LogApiBase
from source.dependencies.authentication import check_authentication


class ClientForTest(TestCase):
    """create client to test the api routes using unittest.TestCase."""

    engine: Engine
    session: Session
    api: FastAPI
    test_client: TestClient

    def __init_subclass__(cls) -> None:
        """Init class that inherits from ClientForTest."""
        cls.engine = create_engine(
            f"sqlite:///{tempfile.mkstemp()[1]}",
            connect_args={"check_same_thread": False},
        )
        for name, method in inspect.getmembers(cls, inspect.isfunction):
            setattr(cls, name, cls.override_database(method))
        for name, method in inspect.getmembers(cls, inspect.ismethod):
            setattr(cls, name, cls.override_database(method))

    @classmethod
    def override_database(cls, func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Override function to use test database.

        Parameters
        ----------
        func : Callable[..., ReturnT]
            Function to be override.

        Returns
        -------
        Callable[..., ReturnT]
            Overridden function.

        """

        @functools.wraps(func)
        def wrap(*args: Any, **kwargs: Any) -> Any:
            with patch(
                "source.dependencies.database.DATABASE_ENGINE", cls.engine
            ):
                return func(*args, **kwargs)

        return wrap

    @classmethod
    def setUpClass(cls) -> None:
        """Run before the class tests."""
        cls.session = sessionmaker(
            autocommit=False, autoflush=False, bind=cls.engine
        )()
        LogApiBase.metadata.create_all(cls.engine)

        cls.api = log_api

        def override_check_authentication() -> None:
            """Override authentication for tests."""

        cls.api.dependency_overrides[
            check_authentication
        ] = override_check_authentication

        cls.test_client = TestClient(cls.api)

    @classmethod
    def tearDownClass(cls) -> None:
        """Run after the class tests."""
        LogApiBase.metadata.drop_all(cls.engine)
