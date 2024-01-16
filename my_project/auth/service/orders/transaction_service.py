from my_project.auth.dao import transaction_dao
from my_project.auth.service.general_service import GeneralService


class TransactionService(GeneralService):
    """
    Realisation of Transaction service.
    """
    _dao = transaction_dao
