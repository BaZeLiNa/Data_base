"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.dao.orders import reservation_dao
from my_project.auth.service.general_service import GeneralService


class ReservationService(GeneralService):
    """
    Realisation of Reservation service.
    """
    _dao = reservation_dao

    def get_reservations_after_id(self, in_id: int) -> List[object]:
        """
        Gets Reservation objects from the database table with field 'id' >= in_id.
        :param in_id: id value
        :return: list of all objects
        """
        return self._dao.get_reservations_after_id(in_id)

    def get_reservations_for_user(self, user_id: int) -> List[object]:
        """
        Gets Reservation objects from the database table for a specific user.
        :param user_id: user_id value
        :return: list of all objects
        """
        return self._dao.get_reservations_for_user(user_id)

    # Додайте інші методи, які необхідні для обробки бізнес-логіки пов'язаної із сутністю
