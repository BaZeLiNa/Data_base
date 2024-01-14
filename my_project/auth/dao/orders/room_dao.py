# app/dao/room_dao.py

from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.room import Room

class RoomDAO(GeneralDAO):
    _domain_type = Room

    # Додайте інші методи DAO за необхідності

    def find_by_hotel(self, hotel_id: int) -> List[Room]:
        """
        Find rooms in a specific hotel.
        :param hotel_id: ID of the hotel
        :return: List of Room objects
        """
        return self._session.query(self._domain_type).filter_by(hotel_id=hotel_id).all()

    def find_by_room_type(self, room_type: str) -> List[Room]:
        """
        Find rooms by their type.
        :param room_type: Type of the room
        :return: List of Room objects
        """
        return self._session.query(self._domain_type).filter_by(room_type=room_type).all()

    # Додайте інші методи за необхідності
