# review_controller.py
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import review_service

class ReviewController(GeneralController):
    """
    Realisation of Review controller.
    """
    _service = review_service

    def get_reviews_after_id(self, review_id: int) -> List[object]:
        """
        Gets Review objects from the database table with field 'id' >= review_id
        using Service layer as DTO objects.
        :param review_id: id value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_reviews_after_id(review_id)))

    def get_reviews_with_rating_filter(self, rating_filter: int) -> List[object]:
        """
        Gets Review objects from the database table with field 'rating' >= rating_filter
        using Service layer as DTO objects.
        :param rating_filter: rating value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_reviews_with_rating_filter(rating_filter)))
