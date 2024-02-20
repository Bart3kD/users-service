from src.repositories import UserRepository
from src.repositories import users

from src.users import User

import pytest


@pytest.fixture()
def repository() -> UserRepository:
    return UserRepository()


def test_users_repository_returns_users(repository: UserRepository,) -> None:
    actual = repository.get_all()
    assert actual == users


def test_users_repository_returns_user_by_id(repository: UserRepository,) -> None:
    repository.create({"firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"})
    actual = repository.get_by_id(3).as_dict
    assert actual == users[0].as_dict


def test_users_repository_returns_updated_user(repository: UserRepository,) -> None:
    repository.create({"firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"})
    user_id = 3
    user_data = {"id": 3, "firstName": "Amanda", "lastName": "Sing", "birthYear": 1992, "group": "user"}
    actual = repository.update(user_id, user_data).as_dict
    assert actual == users[0].as_dict


def test_users_repository_deletes_user(repository: UserRepository,) -> None:
    repository.create({"firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"})
    user_id = 3
    actual = repository.delete(user_id)
    assert actual == True