from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import review_service
from my_project.auth.service.orders.review_service import ReviewService


class ReviewController(GeneralController):
    """
    Realisation of Review controller.
    """
    _service = review_service

    def __init__(self):
        super().__init__()
        self._service = ReviewService()
