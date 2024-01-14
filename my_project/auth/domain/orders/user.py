from typing import Dict, Any


class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'User':
        return User(
            user_id=dto_dict.get("user_id"),
            username=dto_dict.get("username"),
            email=dto_dict.get("email"),
        )
