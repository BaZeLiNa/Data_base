"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.dao import review_dao
from my_project.auth.service.general_service import GeneralService


class ReviewService(GeneralService):
    """
    Realisation of Review service.
    """
    _dao = review_dao

    def get_reviews_after_id(self, in_id: int) -> List[object]:
        """
        Gets Review objects from the database table with field 'id' >= in_id.
        :param in_id: id value
        :return: list of all objects
        """
        return self._dao.get_reviews_after_id(in_id)

    def get_reviews_with_rating(self, rating: int) -> List[object]:
        """
        Gets Review objects from the database table with a specific rating.
        :param rating: rating value
        :return: list of all objects
        """
        return self._dao.get_reviews_with_rating(rating)

    # Додайте інші методи, які необхідні для обробки бізнес-логіки пов'язаної із сутністю
