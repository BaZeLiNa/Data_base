# app/domain/hotel_network.py

from typing import Dict, Any


class HotelNetwork:
    def __init__(self, hotel_id, network_id):
        self.hotel_id = hotel_id
        self.network_id = network_id

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "hotel_id": self.hotel_id,
            "network_id": self.network_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'HotelNetwork':
        return HotelNetwork(
            hotel_id=dto_dict.get("hotel_id"),
            network_id=dto_dict.get("network_id"),
        )
