from my_project.auth.dao import network_dao
from my_project.auth.service.general_service import GeneralService


class NetworkService(GeneralService):
    """
    Realisation of Network service.
    """
    _dao = network_dao
