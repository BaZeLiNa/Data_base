"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.dao import hotel_network_dao
from my_project.auth.service.general_service import GeneralService


class HotelNetworkService(GeneralService):
    """
    Realisation of HotelNetwork service.
    """
    _dao = hotel_network_dao

    def get_networks_with_min_hotels(self, min_hotels: int) -> List[object]:
        """
        Gets HotelNetwork objects from the database table with at least min_hotels associated.
        :param min_hotels: minimum number of hotels associated
        :return: list of all objects
        """
        return self._dao.get_networks_with_min_hotels(min_hotels)

    # Додайте інші методи, які необхідні для обробки бізнес-логіки пов'язаної із сутністю
