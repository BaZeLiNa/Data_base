# app/dao/user_dao.py

from typing import Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.user import User


class UserDAO(GeneralDAO):
    _domain_type = User

    # Додайте інші методи DAO за необхідності

    def find_by_email(self, email: str) -> User:
        """
        Find user by email.
        :param email: Email of the user
        :return: User object
        """
        return self._session.query(self._domain_type).filter_by(email=email).first()

    # Додайте інші методи за необхідності
