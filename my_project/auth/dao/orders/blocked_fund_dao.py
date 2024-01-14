# app/dao/blocked_fund_dao.py

from typing import Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.blocked_fund import BlockedFund


class BlockedFundDAO(GeneralDAO):
    _domain_type = BlockedFund

    # Додайте інші методи DAO за необхідності

    def find_by_user_id(self, user_id: int) -> List[BlockedFund]:
        """
        Find blocked funds for a specific user.
        :param user_id: ID of the user
        :return: List of BlockedFund objects
        """
        return self._session.query(self._domain_type).filter_by(user_id=user_id).all()

    # Додайте інші методи за необхідності
