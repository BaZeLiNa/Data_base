# transaction_controller.py
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import transaction_service
from my_project.auth.service.orders.transaction_service import TransactionService


class TransactionController(GeneralController):
    """
    Realisation of Transaction controller.
    """
    _service = TransactionService()
    
    def __init__(self):
        super().__init__()
