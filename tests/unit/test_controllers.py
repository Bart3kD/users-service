from unittest.mock import Mock

import pytest

from src.controllers import UserController
from src.repositories import UserRepository

from src.users import User


@pytest.fixture
def repository() -> Mock:
    return Mock(UserRepository)


@pytest.fixture
def controller(repository: Mock) -> UserController:
    return UserController(
        repository=repository
    )


def test_user_controller_can_be_instantiated(
        controller: UserController,
) -> None:
    assert isinstance(controller, UserController)


def test_raises_on_create_method(
        controller: UserController,
        repository: Mock,
) -> None:
    user_data = {"id": 0, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}
    repository.create.side_effect = NotImplementedError
    with pytest.raises(NotImplementedError):
        controller.create(user_data)


def test_pass_user_data_to_repository(
        controller: UserController,
        repository: Mock,
) -> None:
    user_data = {"id": 0, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}
    controller.create(user_data)
    repository.create.assert_called_with(user_data)


def test_raises_on_get_all_method(
        controller: UserController,
        repository: Mock,
) -> None:
    repository.get_all.side_effect = NotImplementedError
    with pytest.raises(NotImplementedError):
        controller.get_all()


def test_raises_on_get_by_id_method(
        controller: UserController,
        repository: Mock,
) -> None:
    user_id = 1
    repository.get_by_id.side_effect = NotImplementedError
    with pytest.raises(NotImplementedError):
        controller.get_by_id(user_id)


def test_pass_get_by_id_data_to_repository(
        controller: UserController,
        repository: Mock,
) -> None:
    user_id = 1
    controller.get_by_id(user_id)
    repository.get_by_id.assert_called_with(user_id)


def test_raises_on_update_method(
        controller: UserController,
        repository: Mock,
) -> None:
    user_id = 1
    user_data = {"id": 3, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}
    repository.update.side_effect = NotImplementedError
    with pytest.raises(NotImplementedError):
        controller.update(user_id, user_data)


def test_pass_update_data_to_repository(
        controller: UserController,
        repository: Mock,
) -> None:
    user_id = 1
    user_data = {"id": 3, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}
    controller.update(user_id, user_data)
    repository.update.assert_called_with(user_id, user_data)


def test_raises_on_delete_method(
        controller: UserController,
        repository: Mock,
) -> None:
    user_id = 1
    repository.delete.side_effect = NotImplementedError
    with pytest.raises(NotImplementedError):
        controller.delete(user_id)


def test_pass_delete_data_to_repository(
        controller: UserController,
        repository: Mock,
) -> None:
    user_id = 1
    controller.delete(user_id)
    repository.delete.assert_called_with(user_id)