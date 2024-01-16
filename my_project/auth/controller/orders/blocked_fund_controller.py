
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import blocked_fund_service


class BlockedFundController(GeneralController):
    """
    Realisation of BlockedFund controller.
    """
    _service = blocked_fund_service
