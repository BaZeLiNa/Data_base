"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from my_project.auth.dao import location_dao
from my_project.auth.service.general_service import GeneralService


class LocationService(GeneralService):
    """
    Realisation of Location service.
    """
    _dao = location_dao

    def find_hotels_in_location(self, location_id: int):
        """
        Find all hotels in a location by location_id
        """
        return self._dao.find_hotels_in_location(location_id)
