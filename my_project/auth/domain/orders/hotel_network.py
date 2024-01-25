from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class HotelNetworks(db.Model, IDto):
    __tablename__ = 'hotel_networks'

    hotel_id = db.Column(db.Integer, db.ForeignKey("hotels.hotel_id"), primary_key=True)
    network_id = db.Column(db.Integer, db.ForeignKey("networks.network_id"), primary_key=True)

    hotel = db.relationship("Hotels", overlaps="hotel_networks")
    network = db.relationship("Networks", overlaps="hotel_networks")

    def __repr__(self) -> str:
        return f"Hotel networks({self.network_id}, {self.hotel_id})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'HotelNetworks':
        obj = HotelNetworks(
            hotel_id=dto_dict.get("hotel_id"),
            network_id=dto_dict.get("network_id"),
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "hotel_id": self.hotel_id,
            "network_id": self.network_id,
        }
