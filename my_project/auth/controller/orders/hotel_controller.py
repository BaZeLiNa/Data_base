from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import hotel_service


class HotelController(GeneralController):
    """
    Realisation of Hotel controller.
    """
    _service = hotel_service

    def __init__(self):
        super().__init__()
