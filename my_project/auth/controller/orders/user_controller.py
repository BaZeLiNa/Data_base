from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import user_service


class UserController(GeneralController):
    """
    Realisation of User controller.
    """
    _service = user_service

    def __init__(self):
        super().__init__()

    def find_users_with_blocked_funds(self, user_id: int):
        return self._service.find_users_with_blocked_funds(user_id)

    def find_users_with_transactions(self, user_id: int):
        return self._service.find_users_with_transactions(user_id)

    def find_users_with_reviews(self, user_id: int):
        return self._service.find_users_with_reviews(user_id)

    def find_users_with_reservations(self, user_id: int):
        return self._service.find_users_with_reservations(user_id)
