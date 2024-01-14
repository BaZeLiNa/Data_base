"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.dao import hotel_dao
from my_project.auth.service.general_service import GeneralService


class HotelService(GeneralService):
    """
    Realisation of Hotel service.
    """
    _dao = hotel_dao
