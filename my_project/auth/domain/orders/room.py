# app/domain/room.py

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Rooms(db.Model, IDto):
    __tablename__ = 'rooms'

    room_number = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer)  # foreign key
    room_type = db.Column(db.String(255))
    price = db.Column(db.Integer)

    def __repr__(self):
        return (f"Room(room_number={self.room_number}, hotel_id={self.hotel_id},"
                f" room_type={self.room_type}, price={self.price})")

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Rooms':
        obj = Rooms(
            room_number=dto_dict.get("room_number"),
            hotel_id=dto_dict.get("hotel_id"),
            room_type=dto_dict.get("room_type"),
            price=dto_dict.get("price"),
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "room_number": self.room_number,
            "hotel_id": self.hotel_id,
            "room_type": self.room_type,
            "price": self.price,
        }
