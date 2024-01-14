# app/dao/reservation_dao.py

from typing import Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.reservation import Reservation


class ReservationDAO(GeneralDAO):
    _domain_type = Reservation

    # Додайте інші методи DAO за необхідності

    def find_by_user_id(self, user_id: int) -> List[Reservation]:
        """
        Find reservations for a specific user.
        :param user_id: ID of the user
        :return: List of Reservation objects
        """
        return self._session.query(self._domain_type).filter_by(user_id=user_id).all()

    # Додайте інші методи за необхідності
