from fastapi import status

from tests.utils import ClientForTest


class TestDocsRoute(ClientForTest):
    def test_status_code(self) -> None:
        response = self.test_client.get("/docs")
        assert response.status_code == status.HTTP_200_OK
