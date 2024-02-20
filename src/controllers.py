from src.repositories import UserRepository

class UserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def create(self, user_data) -> None:
        return self._repository.create(user_data)

    def get_all(self) -> None:
        return self._repository.get_all()

    def get_by_id(self, user_id) -> None:
        return self._repository.get_by_id(user_id)

    def update(self, user_id, user_data) -> None:
        return self._repository.update(user_id, user_data)

    def delete(self, user_id) -> None:
        return self._repository.delete(user_id)
