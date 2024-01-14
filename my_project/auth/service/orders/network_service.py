"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.dao import network_dao
from my_project.auth.service.general_service import GeneralService


class NetworkService(GeneralService):
    """
    Realisation of Network service.
    """
    _dao = network_dao

    def get_networks_with_capacity(self, min_capacity: int) -> List[object]:
        """
        Gets Network objects from the database table with total capacity greater than or equal to min_capacity.
        :param min_capacity: minimum total capacity value
        :return: list of all objects
        """
        return self._dao.get_networks_with_capacity(min_capacity)

    # Додайте інші методи, які необхідні для обробки бізнес-логіки пов'язаної із сутністю
