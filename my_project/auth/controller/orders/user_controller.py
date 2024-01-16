from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import user_service
from my_project.auth.service.orders.user_service import UserService


class UserController(GeneralController):
    """
    Realisation of User controller.
    """
    _service = UserService()

    def __init__(self):
        super().__init__()
