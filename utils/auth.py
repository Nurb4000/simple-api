# utils/auth.py

import hashlib

class Auth:
    def __init__(self, username="admin", password="password"):
        self.username = username
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

    def authenticate(self, username, password):
        return (username == self.username) and (hashlib.sha256(password.encode()).hexdigest() == self.password_hash)