from typing import Dict, Any

from my_project import db


class Hotels(db.Model):
    tablename = "hotels"

    hotel_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    # location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    rating = db.Column(db.Integer)

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
