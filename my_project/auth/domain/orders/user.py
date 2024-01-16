from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Users(db.Model, IDto):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __repr__(self) -> str:
        return f"User({self.user_id}, {self.username}, {self.email})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Users':
        obj = Users(
            user_id=dto_dict.get("user_id"),
            username=dto_dict.get("username"),
            email=dto_dict.get("email"),
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
        }
