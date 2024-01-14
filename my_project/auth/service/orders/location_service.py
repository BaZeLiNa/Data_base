"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.dao import location_dao
from my_project.auth.service.general_service import GeneralService


class LocationService(GeneralService):
    """
    Realisation of Location service.
    """
    _dao = location_dao

    def get_locations_in_network(self, network_id: int) -> List[object]:
        """
        Gets Location objects from the database table that belong to a specific network.
        :param network_id: network_id value
        :return: list of all objects
        """
        return self._dao.get_locations_in_network(network_id)

    # Додайте інші методи, які необхідні для обробки бізнес-логіки пов'язаної із сутністю
