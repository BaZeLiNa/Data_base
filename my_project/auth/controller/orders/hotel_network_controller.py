from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import hotel_network_service
from my_project.auth.service.orders.hotel_network_service import HotelNetworkService


class HotelNetworkController(GeneralController):
    """
    Realisation of HotelNetwork controller.
    """
    _service = hotel_network_service

    def __init__(self):
        super().__init__()
        self._service = HotelNetworkService()
