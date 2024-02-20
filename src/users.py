from datetime import datetime
import json

class User:
    ALLOWED_GROUPS = {"user", "premium", "admin"}

    def __init__(self, user_id, first_name, last_name, birth_year, group):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self._group = None 

        self.group = group

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        if value not in self.ALLOWED_GROUPS:
            raise ValueError(f"Invalid group: {value}. Allowed values: {self.ALLOWED_GROUPS}")
        self._group = value

    @property
    def age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year

    @property
    def as_dict(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "age": self.age,
            "group": self.group
        }