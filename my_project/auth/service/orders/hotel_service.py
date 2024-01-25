"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from my_project.auth.dao import hotel_dao
from my_project.auth.service.general_service import GeneralService


class HotelService(GeneralService):
    """
    Realisation of Hotel service.
    """
    _dao = hotel_dao

    def find_rooms_in_hotel(self, hotel_id: int):
        """
        Find all rooms in a hotel by hotel_id
        """
        return self._dao.find_rooms_in_hotel(hotel_id)

    def find_reservations_in_hotels(self, hotel_id: int):
        return self._dao.find_reservations_in_hotels(hotel_id)

    def find_hotels_with_reviews(self, hotel_id: int):
        return self._dao.find_hotels_with_reviews(hotel_id)

    def find_hotels_with_networks(self, hotel_id: int):
        return self._dao.find_hotels_with_networks(hotel_id)
