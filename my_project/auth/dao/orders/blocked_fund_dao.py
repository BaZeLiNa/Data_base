# app/dao/blocked_fund_dao.py

from typing import Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.blocked_fund import BlockedFunds


class BlockedFundDAO(GeneralDAO):
    _domain_type = BlockedFunds


