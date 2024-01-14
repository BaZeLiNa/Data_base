"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.dao import room_dao
from my_project.auth.service.general_service import GeneralService


class RoomService(GeneralService):
    """
    Realisation of Room service.
    """
    _dao = room_dao

    def get_rooms_in_hotel(self, hotel_id: int) -> List[object]:
        """
        Gets Room objects from the database table located in a specific hotel.
        :param hotel_id: hotel_id value
        :return: list of all objects
        """
        return self._dao.get_rooms_in_hotel(hotel_id)

    def get_rooms_with_capacity(self, min_capacity: int) -> List[object]:
        """
        Gets Room objects from the database table with capacity greater than or equal to min_capacity.
        :param min_capacity: minimum capacity value
        :return: list of all objects
        """
        return self._dao.get_rooms_with_capacity(min_capacity)

    # Додайте інші методи, які необхідні для обробки бізнес-логіки пов'язаної із сутністю
