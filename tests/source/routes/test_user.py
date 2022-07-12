from fastapi import status

from tests.utils import ClientForTest


class TestUserRoute(ClientForTest):
    # TODO separate tests by responsibility
    def test_create_route(self) -> None:
        test_email = "test@email.com"
        response = self.test_client.post(
            self.api.url_path_for("user-create"),
            data={"email": test_email, "password": "password"},
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert (
            response.json()["detail"]
            == f"Email {test_email} registered successfully."
        )

    def test_create_duplicate_error(self) -> None:
        test_email = "test2@email.com"
        self.test_client.post(
            self.api.url_path_for("user-create"),
            data={"email": test_email, "password": "password"},
        )
        response = self.test_client.post(
            self.api.url_path_for("user-create"),
            data={"email": test_email, "password": "password"},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert (
            response.json()["detail"]
            == f"Email {test_email} is already registered."
        )

    # TODO parametrize
    def test_create_email_error(self) -> None:
        response = self.test_client.post(
            self.api.url_path_for("user-create"),
            data={"email": "", "password": "password"},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "field required"

    # TODO parametrize
    def test_create_password_error(self) -> None:
        response = self.test_client.post(
            self.api.url_path_for("user-create"),
            data={"email": "test@email.com", "password": ""},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "field required"

    # TODO mock decouple call
    def test_token_route(self) -> None:
        self.test_client.post(
            self.api.url_path_for("user-create"),
            data={"email": "test_token@email.com", "password": "123456"},
        )
        response = self.test_client.post(
            self.api.url_path_for("user-token"),
            data={"username": "test_token@email.com", "password": "123456"},
        )
        assert response.status_code == status.HTTP_200_OK
        assert "access_code" in response.json()

    # TODO parametrize
    def test_token_email_error(self) -> None:
        response = self.test_client.post(
            self.api.url_path_for("user-token"),
            data={"username": "", "password": "123456"},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "field required"

    # TODO parametrize
    def test_token_password_error(self) -> None:
        response = self.test_client.post(
            self.api.url_path_for("user-token"),
            data={"username": "test@email.com", "password": ""},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "field required"

    def test_token_authentication_error(self) -> None:
        response = self.test_client.post(
            self.api.url_path_for("user-token"),
            data={"username": "test@email.com", "password": "not_right"},
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json()["detail"] == "Email and/or password incorrect"
