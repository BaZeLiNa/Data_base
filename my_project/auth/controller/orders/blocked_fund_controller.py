# blocked_fund_controller.py
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import blocked_fund_service

class BlockedFundController(GeneralController):
    """
    Realisation of BlockedFund controller.
    """
    _service = blocked_fund_service

    def get_blocked_funds_after_id(self, blocked_fund_id: int) -> List[object]:
        """
        Gets BlockedFund objects from the database table with field 'id' >= blocked_fund_id
        using Service layer as DTO objects.
        :param blocked_fund_id: id value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_blocked_funds_after_id(blocked_fund_id)))

    def get_blocked_funds_with_amount_filter(self, amount_filter: float) -> List[object]:
        """
        Gets BlockedFund objects from the database table with field 'amount' >= amount_filter
        using Service layer as DTO objects.
        :param amount_filter: amount value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_blocked_funds_with_amount_filter(amount_filter)))
