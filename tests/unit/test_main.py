from src.main import app, get_all_users, get_user_by_id, create_user, update_user, delete_user
from unittest.mock import patch
import pytest
from src.users import User

STATUS_OK = 200
CREATED = 201
NO_CONTENT = 204
BAD_REQUEST = 400
NOT_FOUND = 404


@pytest.fixture
def user_data():
    users = [User(0, "John", "Doe", 1990, "user"),
             User(1, "John", "Doe", 1990, "user"),
             User(2, "John", "Doe", 1990, "user")]
    return users


@pytest.fixture
def user():
    return User(2, "John", "Doe", 1990, "user")


@pytest.fixture
def input_user_data():
    return {"id": 0, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}



def test_get_users_endpoint_returns_200(user_data) -> None:
    with patch("src.main.user_controller") as mock:
        mock.get_all.return_value = user_data

    actual = get_all_users()
    assert actual.status_code == STATUS_OK


def test_get_user_by_id_endpoint_returns_200(user) -> None:
    with patch("src.main.user_controller") as mock:
        mock.get_by_id.return_value = user
        actual = get_user_by_id(0)

    assert actual.status_code == STATUS_OK


def test_get_user_by_id_endpoint_uses_right_id(user) -> None:
    with patch("src.main.user_controller") as mock:
        mock.get_by_id.return_value = user
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
    with app.test_request_context(json={"id": 0, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "ur"}):
        actual = create_user()
    assert actual.status_code == BAD_REQUEST


def test_patch_users_endpoint_returns_200(user) -> None:
    with patch("src.controllers.UserController") as mock_controller:
        mock_controller.get_by_id.return_value = user

        with app.test_request_context(json={"id": 3, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}):
            actual = update_user(2)

    assert actual.status_code == STATUS_OK


def test_patch_users_endpoint_returns_400_when_wrong_id(user) -> None:
    with patch("src.controllers.UserController") as mock_controller:
        mock_controller.get_by_id.return_value = user

        with app.test_request_context(json={"id": 3, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}):
            actual = update_user(0)

    assert actual.status_code == BAD_REQUEST


def test_patch_users_endpoint_returns_400_when_wrong_group(user) -> None:
    with patch("src.controllers.UserController") as mock_controller:
        mock_controller.get_by_id.return_value = user

        with app.test_request_context(json={"id": 3, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "ur"}):
            actual = update_user(0)

    assert actual.status_code == BAD_REQUEST

# def test_patch_users_endpoint_returns_right_value(user) -> None:
#     with patch("src.controllers.UserController") as mock_controller:
#         mock_controller.return_value.get_by_id.return_value = user

#         with app.test_request_context(json={"id": 3, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}):
#             actual = update_user(0)

#     assert actual.get_json() == [User(3, "Ame", "Thing", 29, "user").as_dict]


def test_delete_user_endpoint_returns_204(user) -> None:
    with patch("src.controllers.UserController") as mock_controller:
        mock_controller.get_by_id.return_value = user
    
    actual = delete_user(2)
    assert actual.status_code == NO_CONTENT


def test_delete_user_endpoint_returns_404(user) -> None:
    with patch("src.controllers.UserController") as mock_controller:
        mock_controller.get_by_id.return_value = user
    
    actual = delete_user(0)
    assert actual.status_code == NOT_FOUND
