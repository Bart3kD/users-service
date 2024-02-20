from src.users import User

users = []


class UserRepository:
    def create(self, user_data):
        user_id = len(users) + 1
        user = User(
            user_id,
            user_data["firstName"],
            user_data["lastName"],
            user_data["birthYear"],
            user_data["group"]
        )
        users.append(user)
        return user

    def get_all(self):
        return users.as_dict

    def get_by_id(self, user_id):
        for user in users:
            if user.id == user_id:
                return user.as_dict
        return None

    def update(self, user_id, user_data):
        user = self.get_by_id(user_id)
        if user:
            user.first_name = user_data.get("firstName", user.first_name)
            user.last_name = user_data.get("lastName", user.last_name)
            user.birth_year = user_data.get("birthYear", user.birth_year)

            if "group" in user_data:
                user.group = user_data["group"]

            return user
        return None

    def delete(self, user_id):
        user = self.get_by_id(user_id)
        if user:
            users.remove(user)
            return True
        return False
