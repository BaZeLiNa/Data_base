# app/dao/user_dao.py

from typing import Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.user import Users


class UserDAO(GeneralDAO):
    _domain_type = Users

    # Додайте інші методи DAO за необхідно
