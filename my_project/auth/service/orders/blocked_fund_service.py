"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.dao import blocked_fund_dao
from my_project.auth.service.general_service import GeneralService


class BlockedFundService(GeneralService):
    """
    Realisation of BlockedFund service.
    """
    _dao = blocked_fund_dao
