"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.dao import transaction_dao
from my_project.auth.service.general_service import GeneralService


class TransactionService(GeneralService):
    """
    Realisation of Transaction service.
    """
    _dao = transaction_dao

    def get_transactions_after_id(self, in_id: int) -> List[object]:
        """
        Gets Transaction objects from the database table with field 'id' >= in_id.
        :param in_id: id value
        :return: list of all objects
        """
        return self._dao.get_transactions_after_id(in_id)

    def get_transactions_for_user(self, user_id: int) -> List[object]:
        """
        Gets Transaction objects from the database table for a specific user.
        :param user_id: user_id value
        :return: list of all objects
        """
        return self._dao.get_transactions_for_user(user_id)

    # Додайте інші методи, які необхідні для обробки бізнес-логіки пов'язаної із сутністю
