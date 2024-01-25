from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Guests(db.Model, IDto):
    __tablename__ = 'guests'

    guest_id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __repr__(self):
        return f"Guest(guest_id={self.guest_id}, reservation_id={self.reservation_id}, name={self.name}, email={self.email})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Guests':
        obj = Guests(
            guest_id=dto_dict.get("guest_id"),
            reservation_id=dto_dict.get("reservation_id"),
            name=dto_dict.get("name"),
            email=dto_dict.get("email"),
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "guest_id": self.guest_id,
            "reservation_id": self.reservation_id,
            "name": self.name,
            "email": self.email,
        }
