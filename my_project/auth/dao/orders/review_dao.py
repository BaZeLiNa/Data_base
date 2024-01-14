# app/dao/review_dao.py

from typing import Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.review import Review


class ReviewDAO(GeneralDAO):
    _domain_type = Review

    # Додайте інші методи DAO за необхідності

    def find_by_hotel_id(self, hotel_id: int) -> List[Review]:
        """
        Find reviews for a specific hotel.
        :param hotel_id: ID of the hotel
        :return: List of Review objects
        """
        return self._session.query(self._domain_type).filter_by(hotel_id=hotel_id).all()

    # Додайте інші методи за необхідності
