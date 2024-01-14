# app/domain/room.py

from typing import Dict, Any


class Room:
    def __init__(self, room_number, hotel_id, room_type, price):
        self.room_number = room_number
        self.hotel_id = hotel_id
        self.room_type = room_type
        self.price = price

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "room_number": self.room_number,
            "hotel_id": self.hotel_id,
            "room_type": self.room_type,
            "price": self.price,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Room':
        return Room(
            room_number=dto_dict.get("room_number"),
            hotel_id=dto_dict.get("hotel_id"),
            room_type=dto_dict.get("room_type"),
            price=dto_dict.get("price"),
        )
