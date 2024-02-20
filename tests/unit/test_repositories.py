from src.repositories import UserRepository
from src.repositories import users

from src.users import User

import pytest


@pytest.fixture()
def repository() -> UserRepository:
    return UserRepository()


def test_raises_on_create_method(
    repository: UserRepository,
) -> None:
    user_data = {"id": 0, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}
    with pytest.raises(NotImplementedError):
        repository.create(user_data)


def test_stores_title_in_books_list(
    repository: UserRepository,
) -> None:
    user = User(2, "John", "Doe", 1990, "user")
    repository.create(user)
    assert {user.firstName == "John"} in users
