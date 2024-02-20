# from datetime import datetime

# users = []

# class User:
#     ALLOWED_GROUPS = {"user", "premium", "admin"}

#     def __init__(self, user_id, first_name, last_name, birth_year, group):
#         self.id = user_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self._birth_year = birth_year
#         self._group = None 

#         self.group = group

#     @property
#     def group(self):
#         return self._group

#     @group.setter
#     def group(self, value):
#         if value not in self.ALLOWED_GROUPS:
#             raise ValueError(f"Invalid group: {value}. Allowed values: {self.ALLOWED_GROUPS}")
#         self._group = value

#     @property
#     def age(self):
#         current_year = datetime.now().year
#         return current_year - self._birth_year

#     @property
#     def as_dict(self):
#         return {
#             "id": self.id,
#             "firstName": self.first_name,
#             "lastName": self.last_name,
#             "age": self.age,
#             "group": self.group
#         }

# def create(user_data):
#     user_id = len(users) + 1
#     user = User(
#         user_id,
#         user_data["firstName"],
#         user_data["lastName"],
#         user_data["birthYear"],
#         user_data["group"]
#     )
#     users.append(user)
#     return user

# def get_all():
#     return [user.as_dict for user in users]

# create({"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"})
# create({"firstName": "Jane", "lastName": "Smith", "birthYear": 1985, "group": "premium"})
# create({"firstName": "Bob", "lastName": "Johnson", "birthYear": 2000, "group": "admin"})

# print(get_all())
