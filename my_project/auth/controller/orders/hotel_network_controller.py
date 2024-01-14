# hotel_network_controller.py
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import hotel_network_service

class HotelNetworkController(GeneralController):
    """
    Realisation of HotelNetwork controller.
    """
    _service = hotel_network_service

    def get_hotel_networks_after_id(self, network_id: int) -> List[object]:
        """
        Gets HotelNetwork objects from the database table with field 'id' >= network_id
        using Service layer as DTO objects.
        :param network_id: id value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_hotel_networks_after_id(network_id)))

    def get_hotel_networks_with_name_filter(self, name_filter: str) -> List[object]:
        """
        Gets HotelNetwork objects from the database table with name filter using Service layer as DTO objects.
        :param name_filter: first letters of name
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_hotel_networks_with_name_filter(name_filter)))
