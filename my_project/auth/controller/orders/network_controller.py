from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import network_service
from my_project.auth.service.orders.network_service import NetworkService


class NetworkController(GeneralController):
    """
    Realisation of Network controller.
    """
    _service = network_service

    def __init__(self):
        super().__init__()
        self._service = NetworkService()
