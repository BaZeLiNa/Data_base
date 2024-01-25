from typing import Dict, Any
from my_project.db import db
from my_project.auth.domain.i_dto import IDto


class Hotels(db.Model, IDto):
    __tablename__ = 'hotels'

    hotel_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    rating = db.Column(db.Integer)

    networks = db.relationship('Networks', secondary='hotel_networks', back_populates='hotels', overlaps='hotel')
    location = db.relationship('Locations', back_populates='hotels')
    rooms = db.relationship('Rooms', back_populates='hotel')
    reservations = db.relationship('Reservations', back_populates='hotel')
    reviews = db.relationship('Reviews', back_populates='hotel')

    idx_hotel_rating = db.Index('idx_hotel_rating', rating)

    def __repr__(self) -> str:
        return f"Hotel({self.hotel_id}, {self.name}, {self.location_id}, {self.raiting})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Hotels':
        obj = Hotels(
            hotel_id=dto_dict.get('hotel_id'),
            name=dto_dict.get('name'),
            location_id=dto_dict.get('location_id'),
            rating=dto_dict.get('rating'),
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'location_id': self.location_id,
            'rating': self.rating
        }
