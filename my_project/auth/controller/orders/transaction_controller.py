# transaction_controller.py
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import transaction_service

class TransactionController(GeneralController):
    """
    Realisation of Transaction controller.
    """
    _service = transaction_service

    def get_transactions_after_id(self, transaction_id: int) -> List[object]:
        """
        Gets Transaction objects from the database table with field 'id' >= transaction_id
        using Service layer as DTO objects.
        :param transaction_id: id value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_transactions_after_id(transaction_id)))

    def get_transactions_with_type_filter(self, type_filter: str) -> List[object]:
        """
        Gets Transaction objects from the database table with field 'type' == type_filter
        using Service layer as DTO objects.
        :param type_filter: type value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_transactions_with_type_filter(type_filter)))
