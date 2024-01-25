from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import hotel_service


class HotelController(GeneralController):
    """
    Realisation of Hotel controller.
    """
    _service = hotel_service

    def __init__(self):
        super().__init__()

    def find_rooms_in_hotel(self, hotel_id: int):
        """
        Find all rooms in a hotel by hotel_id
        """
        return self._service.find_rooms_in_hotel(hotel_id)

    def find_reservations_in_hotels(self, hotel_id: int):
        return self._service.find_reservations_in_hotels(hotel_id)

    def find_hotels_with_reviews(self, hotel_id: int):
        return self._service.find_hotels_with_reviews(hotel_id)

    def find_hotels_with_networks(self, hotel_id: int):
        return self._service.find_hotels_with_networks(hotel_id)
