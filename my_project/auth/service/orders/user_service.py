from my_project.auth.dao import user_dao
from my_project.auth.service.general_service import GeneralService


class UserService(GeneralService):
    """
    Realisation of User service.
    """
    _dao = user_dao

    def find_users_with_blocked_funds(self, user_id: int):
        return self._dao.find_users_with_blocked_funds(user_id)

    def find_users_with_transactions(self, user_id: int):
        return self._dao.find_users_with_transactions(user_id)

    def find_users_with_reviews(self, user_id: int):
        return self._dao.find_users_with_reviews(user_id)

    def find_users_with_reservations(self, user_id: int):
        return self._dao.find_users_with_reservations(user_id)
