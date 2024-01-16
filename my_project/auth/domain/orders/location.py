from typing import Dict, Any
from my_project.auth.domain.i_dto import IDto

from my_project.db import db


class Locations(db.Model, IDto):
    __tablename__ = "locations"

    location_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255))
    country = db.Column(db.String(255))

    def __repr__(self) -> str:
        return f"Location({self.location_id}, {self.city}, {self.country})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'location_id': self.location_id,
            'city': self.city,
            'country': self.country
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Locations':
        obj = Locations(
            location_id=dto_dict.get('location_id'),
            city=dto_dict.get('city'),
            country=dto_dict.get('country')
        )
        return obj
