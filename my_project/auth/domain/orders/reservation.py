from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Reservations(db.Model, IDto):
    __tablename__ = 'reservations'

    reservation_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.hotel_id'))
    room_number = db.Column(db.Integer)
    checkin_date = db.Column(db.Date)
    checkout_date = db.Column(db.Date)

    hotel = db.relationship('Hotels', back_populates='reservations')
    user = db.relationship('Users')

    idx_reservation_userid = db.Index('idx_reservation_userid', user_id)

    def __repr__(self) -> str:
        return (f"(Reservation(reservation_id={self.reservation_id},"
                f" user_id={self.user_id}, hotel_id={self.hotel_id}, "
                f"room_number={self.room_number}, checkin_date={self.checkin_date},"
                f" checkout_date={self.checkout_date})")

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Reservations':
        obj = Reservations(
            reservation_id=dto_dict.get("reservation_id"),
            user_id=dto_dict.get("user_id"),
            hotel_id=dto_dict.get("hotel_id"),
            room_number=dto_dict.get("room_number"),
            checkin_date=dto_dict.get("checkin_date"),
            checkout_date=dto_dict.get("checkout_date"),
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "reservation_id": self.reservation_id,
            "user_id": self.user_id,
            "hotel_id": self.hotel_id,
            "room_number": self.room_number,
            "checkin_date": self.checkin_date,
            "checkout_date": self.checkout_date,
        }
