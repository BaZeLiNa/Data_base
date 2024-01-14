# network_controller.py
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import network_service

class NetworkController(GeneralController):
    """
    Realisation of Network controller.
    """
    _service = network_service

    def get_networks_after_id(self, network_id: int) -> List[object]:
        """
        Gets Network objects from the database table with field 'id' >= network_id
        using Service layer as DTO objects.
        :param network_id: id value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_networks_after_id(network_id)))

    def get_networks_with_name_filter(self, name_filter: str) -> List[object]:
        """
        Gets Network objects from the database table with field 'name' >= name_filter
        using Service layer as DTO objects.
        :param name_filter: name value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_networks_with_name_filter(name_filter)))
