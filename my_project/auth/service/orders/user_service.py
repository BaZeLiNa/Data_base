from my_project.auth.dao import user_dao
from my_project.auth.service.general_service import GeneralService


class UserService(GeneralService):
    """
    Realisation of User service.
    """
    _dao = user_dao
