# app/domain/network.py

from typing import Dict, Any


class Network:
    def __init__(self, network_id, network_name):
        self.network_id = network_id
        self.network_name = network_name

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "network_id": self.network_id,
            "network_name": self.network_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Network':
        return Network(
            network_id=dto_dict.get("network_id"),
            network_name=dto_dict.get("network_name"),
        )
