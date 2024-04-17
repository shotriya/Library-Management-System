# user_management.py

import json

class User:
    def __init__(self, name, user_id):
        self._name = name
        self._user_id = user_id
        self._borrowed_books = []

    @property
    def name(self):
        return self._name

    @property
    def user_id(self):
        return self._user_id

    @property
    def borrowed_books(self):
        return self._borrowed_books

class UserManager:
    def __init__(self, filename='users.json'):
        self._filename = filename
        self._users = []
        self.load_users()

    def load_users(self):
        try:
            with open(self._filename, 'r') as f:
                data = json.load(f)
                self._users = [User(**user) for user in data]
        except FileNotFoundError:
            pass

    def save_users(self):
        with open(self._filename, 'w') as f:
            json.dump([user.__dict__ for user in self._users], f, indent=4)

    def add_user(self, name, user_id):
        if any(user.user_id == user_id for user in self._users):
            raise ValueError("User ID already exists in the library.")
        new_user = User(name, user_id)
        self._users.append(new_user)
        self.save_users()

    def find_user(self, user_id):
        for user in self._users:
            if user.user_id == user_id:
                return user
        return None
