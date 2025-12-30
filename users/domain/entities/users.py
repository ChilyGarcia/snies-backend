from domain.exceptions.user_exception import InvalidUserException


class User:
    def __init__(self, id: int | None, name: str, email: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

        self._validate_email()

    def _validate_email(self):
        if not self.email or "@" not in self.email:
            raise InvalidUserException("Invalid email")
