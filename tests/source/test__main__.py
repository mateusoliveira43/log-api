"""Test main file."""

from fastapi import status

from tests.utils import ClientForTest


class TestDocsRoute(ClientForTest):
    # noqa: D101 pylint: disable=missing-class-docstring

    def test_status_code(self) -> None:
        # noqa: D102 pylint: disable=missing-function-docstring
        response = self.test_client.get("/docs")
        assert response.status_code == status.HTTP_200_OK
