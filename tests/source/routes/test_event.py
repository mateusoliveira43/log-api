from fastapi import status

from source.database.models import Customer
from tests.utils import ClientForTest


class TestEventRoute(ClientForTest):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.session.add(Customer(name="test", email="test@email.com"))
        cls.session.add(
            Customer(name="test", email="test2@email.com", is_active=False)
        )
        cls.session.commit()

    def test_create_route(self) -> None:
        response = self.test_client.post(
            self.api.url_path_for("event-create"),
            data={"email": "test@email.com", "type_": "test"},
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["detail"] == "Event Registered successfully."

    def test_create_status_error(self) -> None:
        response = self.test_client.post(
            self.api.url_path_for("event-create"),
            data={"email": "test2@email.com", "type_": "test"},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert (
            response.json()["detail"]
            == "Customer with email test2@email.com is not active."
        )

    # TODO parametrize
    def test_create_email_error(self) -> None:
        test_email = "not_in_database@email.com"
        response = self.test_client.post(
            self.api.url_path_for("event-create"),
            data={"email": test_email, "type_": "test"},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert (
            response.json()["detail"]
            == f"Customer with email {test_email} is not registered."
        )

    # TODO parametrize
    def test_create_password_error(self) -> None:
        response = self.test_client.post(
            self.api.url_path_for("event-create"),
            data={"email": "test2@email.com", "type_": ""},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "field required"


class TestEventListRoute(ClientForTest):
    def test_list_empty_route(self) -> None:
        response = self.test_client.get(
            self.api.url_path_for("event-list"),
        )
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 0

    def test_list_route(self) -> None:
        self.test_client.post(
            self.api.url_path_for("customer-create"),
            data={"email": "test@email.com", "name": "test"},
        )
        self.test_client.post(
            self.api.url_path_for("customer-deactivate"),
            data={"email": "test@email.com", "name": "test"},
        )
        response = self.test_client.post(
            self.api.url_path_for("customer-activate"),
            data={"email": "test@email.com", "name": "test"},
        )
        response = self.test_client.get(
            self.api.url_path_for("event-list"),
        )
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 3
