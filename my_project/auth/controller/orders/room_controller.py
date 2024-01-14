# room_controller.py
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import room_service


class RoomController(GeneralController):
    """
    Realisation of Room controller.
    """
    _service = room_service

    def get_rooms_after_id(self, room_id: int) -> List[object]:
        """
        Gets Room objects from the database table with field 'id' >= room_id using Service layer as DTO objects.
        :param room_id: id value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_rooms_after_id(room_id)))

    def get_rooms_with_capacity_filter(self, capacity_filter: int) -> List[object]:
        """
        Gets Room objects from the database table with field 'capacity' >= capacity_filter using Service layer as DTO objects.
        :param capacity_filter: capacity value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_rooms_with_capacity_filter(capacity_filter)))
