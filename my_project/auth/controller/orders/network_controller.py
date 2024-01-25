from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import network_service


class NetworkController(GeneralController):
    """
    Realisation of Network controller.
    """
    _service = network_service

    def __init__(self):
        super().__init__()

    def find_hotels_in_network(self, network_id: int):
        self._service.find_hotels_in_network(network_id)
