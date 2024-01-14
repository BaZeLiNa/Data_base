# app/domain/reservation.py

from typing import Dict, Any


class Reservation:
    def __init__(self, reservation_id, user_id, hotel_id, room_number, checkin_date, checkout_date):
        self.reservation_id = reservation_id
        self.user_id = user_id
        self.hotel_id = hotel_id
        self.room_number = room_number
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "reservation_id": self.reservation_id,
            "user_id": self.user_id,
            "hotel_id": self.hotel_id,
            "room_number": self.room_number,
            "checkin_date": self.checkin_date,
            "checkout_date": self.checkout_date,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Reservation':
        return Reservation(
            reservation_id=dto_dict.get("reservation_id"),
            user_id=dto_dict.get("user_id"),
            hotel_id=dto_dict.get("hotel_id"),
            room_number=dto_dict.get("room_number"),
            checkin_date=dto_dict.get("checkin_date"),
            checkout_date=dto_dict.get("checkout_date"),
        )
