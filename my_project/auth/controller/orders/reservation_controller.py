from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import reservation_service
from my_project.auth.service.orders.reservation_service import ReservationService


class ReservationController(GeneralController):
    """
    Realisation of Reservation controller.
    """
    _service = reservation_service

