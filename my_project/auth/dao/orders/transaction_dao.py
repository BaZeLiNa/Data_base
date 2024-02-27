# app/dao/transaction_dao.py

from typing import Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.transaction import Transactions


class TransactionDAO(GeneralDAO):
    _domain_type = Transactions



