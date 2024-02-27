# app/dao/review_dao.py

from typing import Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.review import Reviews


class ReviewDAO(GeneralDAO):
    _domain_type = Reviews

    # Додайте інші методи DAO за необхідності
