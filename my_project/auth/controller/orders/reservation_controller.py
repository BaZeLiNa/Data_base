# reservation_controller.py
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import reservation_service

class ReservationController(GeneralController):
    """
    Realisation of Reservation controller.
    """
    _service = reservation_service

    def get_reservations_after_id(self, reservation_id: int) -> List[object]:
        """
        Gets Reservation objects from the database table with field 'id' >= reservation_id
        using Service layer as DTO objects.
        :param reservation_id: id value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_reservations_after_id(reservation_id)))

    def get_reservations_with_status_filter(self, status_filter: str) -> List[object]:
        """
        Gets Reservation objects from the database table with field 'status' == status_filter
        using Service layer as DTO objects.
        :param status_filter: status value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_reservations_with_status_filter(status_filter)))
