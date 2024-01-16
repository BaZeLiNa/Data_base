from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import location_service
from my_project.auth.service.orders.location_service import LocationService


class LocationController(GeneralController):
    """
    Realisation of Location controller.
    """
    _service = location_service

    def __init__(self):
        super().__init__()
        self._service = LocationService()
