# room_controller.py
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import room_service
from my_project.auth.service.orders.room_service import RoomService


class RoomController(GeneralController):
    """
    Realisation of Room controller.
    """
    _service = RoomService()

    def __init__(self):
        super().__init__()
