# user_controller.py
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import user_service

class UserController(GeneralController):
    """
    Realisation of User controller.
    """
    _service = user_service

    def get_users_after_id(self, user_id: int) -> List[object]:
        """
        Gets User objects from the database table with field 'id' >= user_id
        using Service layer as DTO objects.
        :param user_id: id value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_users_after_id(user_id)))

    def get_users_with_role_filter(self, role_filter: str) -> List[object]:
        """
        Gets User objects from the database table with field 'role' >= role_filter
        using Service layer as DTO objects.
        :param role_filter: role value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_users_with_role_filter(role_filter)))
