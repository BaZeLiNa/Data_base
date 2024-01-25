from typing import Dict, Any
from my_project.db import db
from my_project.auth.domain.i_dto import IDto


class Networks(db.Model, IDto):
    __tablename__ = "networks"

    network_id = db.Column(db.Integer, primary_key=True)
    network_name = db.Column(db.String(255))

    hotels = db.relationship('Hotels', secondary='hotel_networks', overlaps="network")

    def __repr__(self) -> str:
        return f"Network({self.network_id}, {self.network_name})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Networks':
        obj = Networks(
            network_id=dto_dict.get('network_id'),
            network_name=dto_dict.get('network_name'),
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "network_id": self.network_id,
            "network_name": self.network_name,
        }
