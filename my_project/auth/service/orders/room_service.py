from my_project.auth.dao import room_dao
from my_project.auth.service.general_service import GeneralService


class RoomService(GeneralService):
    """
    Realisation of Room service.
    """
    _dao = room_dao
