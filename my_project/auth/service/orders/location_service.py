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
