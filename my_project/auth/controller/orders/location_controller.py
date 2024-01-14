# location_controller.py
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import location_service

class LocationController(GeneralController):
    """
    Realisation of Location controller.
    """
    _service = location_service

    def get_locations_after_id(self, location_id: int) -> List[object]:
        """
        Gets Location objects from the database table with field 'id' >= location_id using Service layer as DTO objects.
        :param location_id: id value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_locations_after_id(location_id)))

    def get_locations_with_name_filter(self, name_filter: str) -> List[object]:
        """
        Gets Location objects from the database table with name filter using Service layer as DTO objects.
        :param name_filter: first letters of name
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_locations_with_name_filter(name_filter)))
