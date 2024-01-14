"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.dao import user_dao  # Замініть на відповідний DAO для кожної сутності
from my_project.auth.service.general_service import GeneralService  # Замініть на відповідний GeneralService для кожної сутності


class UserService(GeneralService):  # Замініть на відповідний клас сервісу для кожної сутності
    """
    Realisation of User service.
    """
    _dao = user_dao  # Замініть на відповідний DAO для кожної сутності

    def get_users_after_id(self, in_id: int) -> List[object]:
        """
        Gets User objects from the database table with field 'id' >= in_id.
        :param in_id: id value
        :return: list of all objects
        """
        return self._dao.get_users_after_id(in_id)

    def get_users_with_name_filter(self, name_filter: str) -> List[object]:
        """
        Gets User objects from the database table with a name filter.
        :param name_filter: first letters of name
        :return: list of all objects
        """
        return self._dao.get_users_with_name_filter(name_filter)

    # Додайте інші методи, які необхідні для обробки бізнес-логіки пов'язаної із сутністю
