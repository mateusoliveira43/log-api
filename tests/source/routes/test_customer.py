from fastapi import status

from tests.utils import ClientForTest


class TestCustomerRoute(ClientForTest):
    def test_create_route(self) -> None:
        response = self.test_client.post(
            self.api.url_path_for("customer-create"),
            data={"email": "test@email.com", "name": "test"},
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["detail"] == "Customer registered successfully."

    def test_create_duplicate_error(self) -> None:
        test_email = "test2@email.com"
        self.test_client.post(
            self.api.url_path_for("customer-create"),
            data={"email": test_email, "name": "test"},
        )
        response = self.test_client.post(
            self.api.url_path_for("customer-create"),
            data={"email": test_email, "name": "test"},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert (
            response.json()["detail"]
            == f"Email {test_email} is already registered."
        )

    # TODO parametrize
    def test_create_email_error(self) -> None:
        response = self.test_client.post(
            self.api.url_path_for("customer-create"),
            data={"email": "", "name": "test"},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "field required"

    # TODO parametrize
    def test_create_password_error(self) -> None:
        response = self.test_client.post(
            self.api.url_path_for("customer-create"),
            data={"email": "test@email.com", "name": ""},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "field required"

    def test_deactivate_route(self) -> None:
        self.test_client.post(
            self.api.url_path_for("customer-create"),
            data={"email": "test3@email.com", "name": "test"},
        )
        response = self.test_client.post(
            self.api.url_path_for("customer-deactivate"),
            data={"email": "test3@email.com", "name": "test"},
        )
        assert response.status_code == status.HTTP_200_OK
        assert (
            response.json()["detail"] == "Customer deactivated successfully."
        )

    def test_deactivate_error(self) -> None:
        test_email = "test4@email.com"
        self.test_client.post(
            self.api.url_path_for("customer-create"),
            data={"email": test_email, "name": "test"},
        )
        self.test_client.post(
            self.api.url_path_for("customer-deactivate"),
            data={"email": test_email, "name": "test"},
        )
        response = self.test_client.post(
            self.api.url_path_for("customer-deactivate"),
            data={"email": test_email, "name": "test"},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert (
            response.json()["detail"]
            == f"Customer with email {test_email} is already deactivated."
        )

    def test_activate_route(self) -> None:
        self.test_client.post(
            self.api.url_path_for("customer-create"),
            data={"email": "test5@email.com", "name": "test"},
        )
        self.test_client.post(
            self.api.url_path_for("customer-deactivate"),
            data={"email": "test5@email.com", "name": "test"},
        )
        response = self.test_client.post(
            self.api.url_path_for("customer-activate"),
            data={"email": "test5@email.com", "name": "test"},
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["detail"] == "Customer activated successfully."

    def test_activate_error(self) -> None:
        test_email = "test6@email.com"
        self.test_client.post(
            self.api.url_path_for("customer-create"),
            data={"email": test_email, "name": "test"},
        )
        response = self.test_client.post(
            self.api.url_path_for("customer-activate"),
            data={"email": test_email, "name": "test"},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert (
            response.json()["detail"]
            == f"Customer with email {test_email} is already activated."
        )
