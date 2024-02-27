from my_project.auth.dao import review_dao
from my_project.auth.service.general_service import GeneralService


class ReviewService(GeneralService):
    """
    Realisation of Review service.
    """
    _dao = review_dao
