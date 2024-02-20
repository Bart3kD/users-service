from src.main import app, get_all_users, get_user_by_id, create_user, update_user
from unittest import patch
import pytest

STATUS_OK = 200
CREATED = 201
NO_CONTENT = 204
BAD_REQUEST = 400
NOT_FOUND = 404


@pytest.fixture
def user_data():
    users = [
        {"id": 0, "firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"},
        {"id": 1, "firstName": "Jane", "lastName": "Smith", "birthYear": 1985, "group": "premium"},
        {"id": 2, "firstName": "Bob", "lastName": "Johnson", "birthYear": 2000, "group": "admin"}
    ]
    return users


@pytest.fixture
def input_user_data():
    return {"id": 0, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"},


def test_get_users_endpoint_returns_200(user_data) -> None:
    with patch("src.main.user_controller") as mock:
        mock.get_all.return_value = user_data

    actual = get_all_users(user_data)
    assert actual.status_code == STATUS_OK


def test_get_users_endpoint_returns_404() -> None:
    with patch("src.main.user_controller") as mock:
        mock.get_all.return_value = {}

    actual = get_all_users({})
    assert actual.status_code == NOT_FOUND


def test_get_user_by_id_endpoint_returns_200(user_data) -> None:
    with patch("src.main.user_controller") as mock:
        mock.get_by_id.return_value = user_data

    actual = get_user_by_id(0)
    assert actual.status_code == STATUS_OK


def test_get_user_by_id_endpoint_uses_right_id(user_data) -> None:
    with patch("src.main.user_controller") as mock:
        mock.get_by_id.return_value = user_data

    get_user_by_id(0)
    mock.get_by_id.assert_called_with(0)


def test_get_user_by_id_endpoint_returns_404() -> None:
    with patch("src.main.user_controller") as mock:
        mock.get_by_id.return_value = {}

    actual = get_user_by_id(0)
    assert actual.status_code == NOT_FOUND


def test_post_users_endpoint_returns_201(input_user_data) -> None:
    with app.test_request_context(json=input_user_data):
        actual = create_user()
    assert actual.status_code == CREATED


def test_post_users_endpoint_returns_400() -> None:
    with app.test_request_context(json={}):
        actual = create_user()
    assert actual.status_code == BAD_REQUEST


def test_post_users_endpoint_returns_right_data(input_user_data) -> None:
    with app.test_request_context(json=input_user_data):
        actual = create_user()
    assert actual.data == input_user_data


def test_patch_users_endpoint_returns_200(user_data) -> None:
    with app.test_request_context(json=user_data):
        actual = update_user()


def test_delete_user_endpoint() -> None:
    client = app.test_client()

    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}

    create_response = client.post("/users", json=user_data)
    assert create_response.status_code == STATUS_OK

    created_user_id = create_response.json.get("id")

    actual = client.delete(f"/users/{created_user_id}")
    assert actual.status_code == NO_CONTENT
